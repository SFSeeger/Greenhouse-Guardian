import { writable } from 'svelte/store';

export const filters = writable({ from: 60, device: [] });
