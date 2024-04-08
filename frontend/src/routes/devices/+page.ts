import type { PageLoad } from './$types';
import { PUBLIC_API_URL } from '$env/static/public';
import { error } from '@sveltejs/kit';

export const prerender = 'auto';
export const ssr = false;

export const load: PageLoad = (async ({fetch, params}) => {
    const response = await fetch(new URL("device/list/", PUBLIC_API_URL), {headers: {'Content-Type': 'application/json'}});
    if (!response.ok) {
        if(response.status === 401) {
            error(401, await response.json().then(data => data.detail));
        };
        error(response.status, await response.text());
    };
    const data = await response.json();
    return {
        devices: data
    };
})