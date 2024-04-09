import { get } from 'svelte/store';
import { authToken } from '../auth';
import { error } from '@sveltejs/kit';

export const simpleGet = async (
	svelte_fetch: (url: URL, options?: RequestInit) => Promise<Response>,
	url: URL
) => {
	const response = await svelte_fetch(url, {
		headers: { 'Content-Type': 'application/json', Authorization: 'Token ' + get(authToken) }
	});
	if (!response.ok) {
		if (response.status === 401) {
			error(401, await response.json().then((req_data) => req_data.detail));
		}
		error(response.status, await response.text());
	}
	return await response.json();
};
