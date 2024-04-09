import { PUBLIC_API_URL } from '$env/static/public';
import { simpleGet } from '$lib/utils';
import { get } from 'svelte/store';
import type { PageLoad } from './$types';
import { authToken } from '../../../auth';
import { error } from '@sveltejs/kit';

export const ssr = false;

const getWebhook = async (svelte_fetch: (url: URL, options?: RequestInit) => Promise<Response>) => {
	const response = await svelte_fetch(new URL('webhook/user/', PUBLIC_API_URL), {
		headers: { 'Content-Type': 'application/json', Authorization: 'Token ' + get(authToken) }
	});
	if (!response.ok) {
		if (response.status === 401) {
			error(401, await response.json().then((req_data) => req_data.detail));
		}
		return undefined;
	}
	return await response.json();
};

export const load = (async ({ fetch }) => {
	return {
		webhook: await getWebhook(fetch)
	};
}) satisfies PageLoad;
