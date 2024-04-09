import { PUBLIC_API_URL } from '$env/static/public';
import { error } from '@sveltejs/kit';
import type { PageLoad } from './$types';
import { get } from 'svelte/store';
import { authToken } from '../../auth';
import type { Entry } from '$lib/types/entry';

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

export const load: PageLoad = async ({ fetch }) => {
	const response = await fetch(new URL('entry/list/', PUBLIC_API_URL), {
		headers: { 'Content-Type': 'application/json', Authorization: 'Token ' + get(authToken) }
	});
	if (!response.ok) {
		if (response.status === 401) {
			error(401, await response.json().then((req_data) => req_data.detail));
		}
		error(response.status, await response.text());
	}
	const req_data: Entry[] = await response.json();
	const [temperatureDataset, humidityDataset] = createDeviceDatasets(
		req_data,
		req_data.map((entry) => entry.created_at)
	);
	return {
		entries: req_data,
		temperatureDataset: temperatureDataset,
		humidityDataset: humidityDataset
	};
};
