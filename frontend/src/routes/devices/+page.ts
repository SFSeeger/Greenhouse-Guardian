import type { PageLoad } from './$types';
import { PUBLIC_API_URL } from '$env/static/public';
import { simpleGet } from '$lib/utils';

export const ssr = false;

export const load: PageLoad = async ({ fetch }) => {
	return {
		devices: await simpleGet(fetch, new URL('device/list/', PUBLIC_API_URL))
	};
};
