<script lang="ts">
	import { Line } from 'svelte-chartjs';
	import {
		Chart as ChartJS,
		Title,
		Tooltip,
		Legend,
		LineElement,
		LinearScale,
		PointElement,
		CategoryScale,
		Colors
	} from 'chart.js';

	ChartJS.register(
		Title,
		Tooltip,
		Legend,
		LineElement,
		LinearScale,
		PointElement,
		CategoryScale,
		Colors
	);

	export const title: string = 'Chart';
	export let datasets: any;
	export let labels: string[];

	$: data = {
		labels,
		datasets
	};
</script>

<div>
	<Line
		{data}
		{title}
		options={{
			responsive: true,
			animation: false,
			maintainAspectRatio: false,
			line: {
				pointScale: 0
			},
			scales: {
				x: { display: false }
			}
		}}
		height="300rem"
	/>
</div>
