<script lang="ts">
	import Chart from '$lib/components/chart.svelte';
	import type { Entry } from '$lib/types/entry';
	import { onMount } from 'svelte';
	import type { PageData } from './$types';
	import { invalidateAll, replaceState } from '$app/navigation';
	import Select from 'svelte-select';
	import { filters } from './stores';
	import { get } from 'svelte/store';

	export let data: PageData;

	$: humanReadableLabels = data.entries.map((entry: Entry) =>
		new Date(entry.created_at).toLocaleString()
	);

	$: temperatureDataset = data.temperatureDataset;
	$: humidityDataset = data.humidityDataset;

	let from: string = get(filters).from;
	let devices: string[] = get(filters).device;

	const submitForm = () => {
		$filters = { from: from, device: devices.map((el) => el.value) || [] };
		invalidateAll();
	};

	let refreshInterval: string = '10';
	onMount(() => {
		const interval = setInterval(
			() => {
				invalidateAll();
			},
			1000 * parseInt(refreshInterval)
		);
		return () => {
			clearInterval(interval);
		};
	});
</script>

<h1>Dashboard</h1>
<div>
	<p>Welcome to the dashboard!</p>
</div>

<div class="flex gap-2">
	<form method="GET" on:change={submitForm}>
		<select name="from" id="query-from" on:change={submitForm} bind:value={from}>
			<option value={60}>1 hour ago</option>
			<option value={60 * 6}>6 hours ago</option>
			<option value={60 * 12}>12 hours ago</option>
			<option value={60 * 24}>24 hours ago</option>
			<option value={60 * 48}>48 hours ago</option>
		</select>
		<!-- <Select
			items={data.devices.map((el) => ({ value: el.id, label: el.name }))}
			multiple={true}
			on:change={submitForm}
			on:clear={submitForm}
			bind:value={devices}
		/> -->
	</form>
	<select name="refresh" id="refresh" bind:value={refreshInterval}>
		<option value="5">5s</option>
		<option value="10">10s</option>
		<option value="30">30s</option>
		<option value="60">1m</option>
	</select>
</div>

<Chart title="Temperature" labels={humanReadableLabels} datasets={temperatureDataset} />
<Chart title="Humidity" labels={humanReadableLabels} datasets={humidityDataset} />
