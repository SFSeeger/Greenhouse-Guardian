<script lang="ts">
	import { PUBLIC_API_URL } from '$env/static/public';
	import InlineEditing from '$lib/components/inline_editing.svelte';
	import { get } from 'svelte/store';
	import type { PageData } from './$types';
	import { authToken } from '../../../auth';
	import { error } from '@sveltejs/kit';
	import { stringify } from 'postcss';
	import type { Plant } from '$lib/types/plant';

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

<h1>Device {data.device.name}</h1>
<div>
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

<div>
	{#each data.plants as plant}
		<h3 class="text-xl font-bold">Plant {plant.name}</h3>
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
	{/each}
</div>
