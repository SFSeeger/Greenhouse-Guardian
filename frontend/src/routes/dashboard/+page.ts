import { PUBLIC_API_URL } from '$env/static/public';
import type { PageLoad } from './$types';
import { get } from 'svelte/store';
import type { Entry } from '$lib/types/entry';
import { simpleGet } from '$lib/utils';
import { filters } from './stores';
import type { Device } from '$lib/types/device';

export const ssr = false;

const createDeviceDatasets = (entries: Entry[], x_axis_labels: string[], devices: Device[]) => {
	const temperatureDataset: { label: string; data: number[] }[] = [];
	const humidityDataset: { label: string; data: number[] }[] = [];

	const deviceMap: Map<number, { temperature: number[]; humidity: number[] }> = new Map();
	entries.forEach((entry: Entry) => {
		if (!deviceMap.has(entry.device)) {
			deviceMap.set(entry.device, {
				temperature: new Array(x_axis_labels.length).fill(null),
				humidity: new Array(x_axis_labels.length).fill(null)
			});
		}
		const deviceValues = deviceMap.get(entry.device);
		const entryIdx = x_axis_labels.indexOf(entry.created_at);
		if (deviceValues) {
			deviceValues.temperature[entryIdx] = entry.temperature;
			deviceValues.humidity[entryIdx] = entry.humidity;
		}
	});
	deviceMap.forEach((value, key) => {
		const device = devices.find((device) => device.id === key);
		temperatureDataset.push({
			label: device?.name || `Device ${key}`,
			data: value.temperature
		});
		humidityDataset.push({
			label: device?.name || `Device ${key}`,
			data: value.humidity
		});
	});
	return [temperatureDataset, humidityDataset];
};

export const load: PageLoad = async ({ fetch }) => {
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
	const devices: Device[] = await simpleGet(fetch, new URL('device/list/', PUBLIC_API_URL));
	const [temperatureDataset, humidityDataset] = createDeviceDatasets(
		req_data,
		req_data.map((entry) => entry.created_at),
		devices
	);
	return {
		entries: req_data,
		temperatureDataset: temperatureDataset,
		humidityDataset: humidityDataset,
		devices: devices
	};
};
