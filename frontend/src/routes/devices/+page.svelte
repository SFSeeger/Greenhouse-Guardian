<script lang="ts">
    import type { PageData } from './$types';
    import Card from '$lib/components/card.svelte';
    
    export let data: PageData;
</script>

<h1>Devices</h1>
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-1">
    {#each data.devices as device}
        <Card title={device.name} href="/device/{device.id}">
            {device.name}
        </Card>
    {/each}
</div>
