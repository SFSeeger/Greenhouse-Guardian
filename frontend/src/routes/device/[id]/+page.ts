import type { PageLoad } from './$types';
import { PUBLIC_API_URL } from '$env/static/public';
import { simpleGet } from '$lib/utils';

export const ssr = false;

export const load: PageLoad = async ({ fetch, params }) => {
	return {
		device: await simpleGet(fetch, new URL(`device/${params.id}/`, PUBLIC_API_URL)),
		plants: await simpleGet(fetch, new URL(`plant/list?device=${params.id}`, PUBLIC_API_URL))
	};
};
