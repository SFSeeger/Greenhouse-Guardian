import type { PageLoad } from './$types';
import { PUBLIC_API_URL } from '$env/static/public';
import { error } from '@sveltejs/kit';
import { authToken } from '../../../auth';
import { get } from 'svelte/store';

export const ssr = false;

const get_data = async (svelte_fetch: (url: URL, options?: RequestInit) => Promise<Response>, url: URL) => {
    const response = await svelte_fetch(url, {headers: {'Content-Type': 'application/json', "Authorization": "Token " + get(authToken)}});
    if (!response.ok) {
        if(response.status === 401) {
            error(401, await response.json().then(req_data => req_data.detail));
        };
        error(response.status, await response.text());
    };
    return await response.json();
}

export const load: PageLoad = (async ({fetch, params}) => {
    return {
        device: await get_data(fetch, new URL(`device/${params.id}/`, PUBLIC_API_URL)),
        plants: await get_data(fetch, new URL(`plant/list?device=${params.id}`, PUBLIC_API_URL)),
    };
})