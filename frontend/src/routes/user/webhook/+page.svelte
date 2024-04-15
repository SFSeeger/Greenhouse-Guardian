<script lang="ts">
	import type { PageData } from './$types';
	import InlineEditing from '$lib/components/inline_editing.svelte';
	import { PUBLIC_API_URL } from '$env/static/public';
	import { get } from 'svelte/store';
	import { authToken } from '../../../auth';
	import { error } from '@sveltejs/kit';
	import Swal from 'sweetalert2';

	export let data: PageData;

	const saveWebhookValue = ({ detail: { name, value } }): void => {
		fetch(new URL(`webhook/${data.webhook.id}/`, PUBLIC_API_URL), {
			method: 'PATCH',
			headers: {
				'Content-Type': 'application/json',
				Authorization: 'Token ' + get(authToken)
			},
			body: JSON.stringify({
				[name]: value
			})
		}).then((response) => {
			if (!response.ok) {
				error(response.status, 'Failed to save value');
			}
			response.json().then((res_data) => (data.webhook = res_data));
		});
	};

	const createWebhook = () => {
		Swal.fire({
			title: 'Create Webhook',
			input: 'text',
			inputAttributes: {
				autocapitalize: 'off',
				placeholder: 'Webhook URL'
			},
			showCancelButton: true,
			confirmButtonText: 'Create',
			showLoaderOnConfirm: true,
			preConfirm: async (webhook_url) => {
				try {
					const res = await fetch(new URL('webhook/', PUBLIC_API_URL), {
						method: 'POST',
						headers: {
							'Content-Type': 'application/json',
							Authorization: `Token ${$authToken}`
						},
						body: JSON.stringify({ url: webhook_url })
					});
					if (!res.ok) {
						if (res.status == 400) {
							Swal.showValidationMessage(
								`Request failed: ${await res.json().then((req_data) => req_data)}`
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
				data.webhook = result.value;
				Swal.fire({
					title: 'Webhook Created',
					icon: 'success',
					confirmButtonText: 'Ok'
				});
			}
		});
	};
</script>

<svelte:head>
    <title>Webhook - Greenhouse Guardian</title> 
</svelte:head>

<h1>Webhook</h1>
{#if data.webhook}
	<p>
		Webhook URL: <InlineEditing
			value={data.webhook.url}
			name="url"
			on:inlineSubmit={saveWebhookValue}
		/>
	</p>
	<p>
		Webhook Message Prefix: <InlineEditing
			value={data.webhook.message_prefix}
			name="message_prefix"
			on:inlineSubmit={saveWebhookValue}
		/>
	</p>
{:else}
	<p>No webhook configured.</p>
	<button class="btn btn-primary" on:click={createWebhook}>Create Webhook?</button>
{/if}
