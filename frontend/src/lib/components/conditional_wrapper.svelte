<script lang="ts">
    export let condition: boolean = false;
    export let tag: string = "a";
</script>

{#if condition && tag}
    <svelte:element this={tag} {...$$restProps}>
        <slot></slot>
    </svelte:element>
{:else}
    <slot></slot>
{/if}