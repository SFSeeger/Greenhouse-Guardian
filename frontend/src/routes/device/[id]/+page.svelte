<script lang="ts">
	import { PUBLIC_API_URL } from '$env/static/public';
	import Card from '$lib/components/card.svelte';
	import InlineEditing from '$lib/components/inline_editing.svelte';
	import type { Plant } from '$lib/types/plant';
	import plant_img from '$lib/assets/images/plant.jpg';
	import { error } from '@sveltejs/kit';
	import { get } from 'svelte/store';
	import { authToken } from '../../../auth';
	import type { PageData } from './$types';

	export let data: PageData;

	const saveDeviceValue = ({ detail: { name, value } }) => {
		fetch(new URL(`device/${data.device.id}/`, PUBLIC_API_URL), {
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
			response.json().then((res_data) => (data.device = res_data));
		});
	};

	const savePlantValue = (plantId: number) => {
		return ({ detail: { name, value } }) => {
			fetch(new URL(`plant/${plantId}/`, PUBLIC_API_URL), {
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
					return;
				}
				response.json().then((res_data) => {
					const plant = data.plants.find((p: Plant) => p.id === plantId);
					data.plants[data.plants.indexOf(plant)] = res_data;
				});
			});
		};
	};
</script>

<svelte:head>
	<title>Device {data.device.name} - Greenhouse Guardian</title>
</svelte:head>

<h1 class="text-xl font-bold">
	<InlineEditing
		value={data.device.name}
		name="name"
		on:inlineSubmit={saveDeviceValue}
		prefix="Device"
	/>
</h1>
<Card>
	<div class="mb-4">
		<p>
			Max Temperature: <InlineEditing
				value={data.device.temperature_limit_max}
				name="temperature_limit_max"
				on:inlineSubmit={saveDeviceValue}
			/>
		</p>
		<p>
			Minimum Temperature: <InlineEditing
				value={data.device.temperature_limit_min}
				name="temperature_limit_min"
				on:inlineSubmit={saveDeviceValue}
			/>
		</p>
		<p>
			Maximum Humidity: <InlineEditing
				value={data.device.humidity_limit_max}
				name="humidity_limit_max"
				on:inlineSubmit={saveDeviceValue}
			/>
		</p>
		<p>
			Minimum Humidity: <InlineEditing
				value={data.device.humidity_limit_min}
				name="humidity_limit_min"
				on:inlineSubmit={saveDeviceValue}
			/>
		</p>
	</div>
	<div class="grid grid-rows-4 grid-flow-col gap-2">
		{#each data.plants as plant}
			<Card>
				<h4 class="text-md font-bold">
					<InlineEditing
						value={plant.name}
						name="name"
						on:inlineSubmit={savePlantValue(plant.id)}
					/>
				</h4>
				<p>
					Maximum Humidity: <InlineEditing
						value={plant.humidity_limit_max}
						name="humidity_limit_max"
						on:inlineSubmit={savePlantValue(plant.id)}
					/>
				</p>
				<p>
					Minimum Humidity: <InlineEditing
						value={plant.humidity_limit_min}
						name="humidity_limit_min"
						on:inlineSubmit={savePlantValue(plant.id)}
					/>
				</p>
			</Card>
		{/each}
	</div>
</Card>
