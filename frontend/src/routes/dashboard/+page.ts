import { PUBLIC_API_URL } from '$env/static/public';
import { error } from '@sveltejs/kit';
import type { PageLoad } from './$types';
import { get } from 'svelte/store';
import { authToken } from '../../auth';
import type { Entry } from '$lib/types/entry';
import { simpleGet } from '$lib/utils';
import { filters } from './stores';

export const ssr = false;

const createDeviceDatasets = (entries: Entry[], labels: string[]) => {
	const temperatureDataset: { label: string; data: number[] }[] = [];
	const humidityDataset: { label: string; data: number[] }[] = [];

	const deviceMap: Map<number, { temperature: number[]; humidity: number[] }> = new Map();
	entries.forEach((entry: Entry) => {
		if (!deviceMap.has(entry.device)) {
			deviceMap.set(entry.device, {
				temperature: new Array(labels.length).fill(null),
				humidity: new Array(labels.length).fill(null)
			});
		}
		const deviceValues = deviceMap.get(entry.device);
		const entryIdx = labels.indexOf(entry.created_at);
		if (deviceValues) {
			deviceValues.temperature[entryIdx] = entry.temperature;
			deviceValues.humidity[entryIdx] = entry.humidity;
		}
	});
	deviceMap.forEach((value, key) => {
		temperatureDataset.push({
			label: `${key}`,
			data: value.temperature
		});
		humidityDataset.push({
			label: `${key}`,
			data: value.humidity
		});
	});
	return [temperatureDataset, humidityDataset];
};

export const load: PageLoad = async ({ fetch, url }) => {
	const created_at_after_search_params = `created_at_after=${new Date(new Date().valueOf() - 1000 * 60 * get(filters).from).toISOString()}`;
	const devices_search_params =
		get(filters)
			.device.map((device) => `device=${device}`)
			.join('&') || '';
	const request_url = new URL(
		`entry/list/?${created_at_after_search_params}&${devices_search_params}`,
		PUBLIC_API_URL
	);
	const req_data: Entry[] = await simpleGet(fetch, request_url);
	const [temperatureDataset, humidityDataset] = createDeviceDatasets(
		req_data,
		req_data.map((entry) => entry.created_at)
	);
	return {
		entries: req_data,
		temperatureDataset: temperatureDataset,
		humidityDataset: humidityDataset,
		devices: await simpleGet(fetch, new URL('device/list/', PUBLIC_API_URL))
	};
};
