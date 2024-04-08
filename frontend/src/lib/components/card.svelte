<script lang="ts">
	import ConditionalWrapper from './conditional_wrapper.svelte';
	export let title: string | undefined = undefined;
</script>

<div class="rounded-md border-2 border-gray-200 p-1">
	{#if title}
		<h5 class="text-lg font-bold">{title}</h5>
	{/if}
	<slot />
</div>
