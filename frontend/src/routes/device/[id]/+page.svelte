<script lang="ts">
	import type { PageData } from './$types';

	export let data: PageData;
</script>

<h1>Device {data.device.name}</h1>
<div>
	<p>Max Temperature: {data.device.temperature_limit_max}</p>
	<p>Minimum Temperature: {data.device.temperature_limit_min}</p>
	<p>Maximum Humidity: {data.device.humidity_limit_max}</p>
	<p>Minimum Humidity: {data.device.humidity_limit_max}</p>
</div>
