<script lang="ts">
	import Chart from '$lib/components/chart.svelte';
	import type { Entry } from '$lib/types/entry';
	import { onMount } from 'svelte';
	import type { PageData } from './$types';
	import { invalidateAll } from '$app/navigation';

	export let data: PageData;

	$: humanReadableLabels = data.entries.map((entry: Entry) =>
		new Date(entry.created_at).toLocaleString()
	);

	$: temperatureDataset = data.temperatureDataset;
	$: humidityDataset = data.humidityDataset;

	onMount(() => {
		const interval = setInterval(() => {
			invalidateAll();
		}, 1000);
		return () => {
			clearInterval(interval);
		};
	});
</script>

<h1>Dashboard</h1>
<div>
	<p>Welcome to the dashboard!</p>
</div>

<Chart title="Temperature" labels={humanReadableLabels} datasets={temperatureDataset} />

<Chart title="Humidity" labels={humanReadableLabels} datasets={humidityDataset} />
