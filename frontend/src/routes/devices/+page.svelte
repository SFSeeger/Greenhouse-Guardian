<script lang="ts">
	import type { PageData } from './$types';
	import Card from '$lib/components/card.svelte';
	import Swal from 'sweetalert2';
	import { PUBLIC_API_URL } from '$env/static/public';
	import { authToken } from '../../auth';
	import type { Device } from '$lib/types/device';

	export let data: PageData;
	$: devices = data.devices;

	export const copyToClipboard = (text: string) => {
		navigator.clipboard.writeText(text);
	};

	const deleteDevice = (device: Device) => {
		const device_id = device.id;
		Swal.fire({
			title: `Delete ${device.name}?`,
			text: "You won't be able to revert this!",
			icon: 'warning',
			showCancelButton: true,
			confirmButtonColor: '#d33',
			cancelButtonColor: '#3085d6',
			confirmButtonText: 'Yes, delete it!',
			preConfirm: async () => {
				try {
					const res = await fetch(new URL(`device/${device_id}`, PUBLIC_API_URL), {
						method: 'DELETE',
						headers: {
							'Content-Type': 'application/json',
							Authorization: `Token ${$authToken}`
						}
					});
					if (!res.ok) {
						if (res.status == 400) {
							Swal.showValidationMessage(
								`Request failed: ${await res.json().then((req_data) => req_data.name)}`
							);
						} else {
							Swal.showValidationMessage(`Request failed: ${res.statusText}`);
						}
					}
				} catch (error) {
					Swal.showValidationMessage(`Request failed: ${error}`);
				}
			},
			allowOutsideClick: () => !Swal.isLoading()
		}).then((result) => {
			if (result.isConfirmed) {
				const device_index = devices.indexOf(device);
				devices.splice(device_index, 1);
				devices = devices;
				Swal.fire({
					title: 'Deleted!',
					text: 'Your device has been deleted.',
					icon: 'success'
				});
			}
		});
	};

	const createDevice = () => {
		Swal.fire({
			title: 'Create Device',
			input: 'text',
			inputAttributes: {
				autocapitalize: 'off',
				placeholder: 'Device Name'
			},
			showCancelButton: true,
			confirmButtonText: 'Create',
			showLoaderOnConfirm: true,
			preConfirm: async (deviceName) => {
				try {
					const res = await fetch(new URL('device/', PUBLIC_API_URL), {
						method: 'POST',
						headers: {
							'Content-Type': 'application/json',
							Authorization: `Token ${$authToken}`
						},
						body: JSON.stringify({ name: deviceName })
					});
					if (!res.ok) {
						if (res.status == 400) {
							Swal.showValidationMessage(
								`Request failed: ${await res.json().then((req_data) => req_data.name)}`
							);
						} else {
							Swal.showValidationMessage(`Request failed: ${res.statusText}`);
						}
					}
					return res.json();
				} catch (error) {
					Swal.showValidationMessage(`Request failed: ${error}`);
				}
			},
			allowOutsideClick: () => !Swal.isLoading()
		}).then((result) => {
			if (result.isConfirmed) {
				devices = [...devices, result.value];
				Swal.fire({
					title: 'Device Created',
					html: `
                            <strong> Keep this auth token save. You won't be able to access it again</strong>
                            <i>${result.value.token}</i>
                        `,
					icon: 'success',
					confirmButtonText: 'Ok'
				});
			}
		});
	};
</script>

<svelte:head>
    <title>Devices - Greenhouse Guardian</title> 
</svelte:head>

<div class="flex justify-between">
	<h1>Devices</h1>
	<button class="btn btn-primary" on:click={createDevice}>Create Device</button>
</div>
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-1">
	{#each devices as device}
		<Card title={device.name}>
			<a href="/device/{device.id}" class="btn btn-primary">View</a>
			<button class="btn btn-danger" on:click|self={() => deleteDevice(device)}>Delete</button>
		</Card>
	{/each}
</div>
