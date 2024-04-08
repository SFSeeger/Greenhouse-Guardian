import type { PageLoad } from './$types';
import { PUBLIC_API_URL } from '$env/static/public';
import { error } from '@sveltejs/kit';
import { authToken } from '../../../auth';
import { get } from 'svelte/store';

export const ssr = false;

export const load: PageLoad = (async ({fetch, params}) => {
    const response = await fetch(new URL(`device/${params.id}/`, PUBLIC_API_URL), {headers: {'Content-Type': 'application/json', "Authorization": "Token " + get(authToken)}});
    if (!response.ok) {
        if(response.status === 401) {
            error(401, await response.json().then(req_data => req_data.detail));
        };
        error(response.status, await response.text());
    };
    const req_data = await response.json();
    return {
        device: req_data
    };
})