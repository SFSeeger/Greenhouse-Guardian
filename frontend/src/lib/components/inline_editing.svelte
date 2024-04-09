<script lang="ts">
	import { createEventDispatcher, onMount } from 'svelte';

	export let value: string | number,
		name: string,
		required = false;

	const dispatch = createEventDispatcher();
	let editing = false,
		original: string | number;

	onMount(() => {
		original = value;
	});

	function edit() {
		editing = true;
	}

	function submit() {
		if (value != original) {
			dispatch('inlineSubmit', { name, value });
		}
		editing = false;
	}

	function keydown(event: KeyboardEvent) {
		if (event.key == 'Escape') {
			event.preventDefault();
			value = original;
			editing = false;
		}
	}

	function focus(element: HTMLInputElement) {
		element.focus();
	}
</script>

{#if editing}
	<!-- svelte-ignore a11y-no-noninteractive-element-interactions -->
	<form on:submit|preventDefault={submit} on:keydown={keydown}>
		<input {name} bind:value on:blur={submit} {required} use:focus />
	</form>
{:else}
	<!-- svelte-ignore a11y-click-events-have-key-events -->
	<div on:click={edit}>
		{value}
	</div>
{/if}
