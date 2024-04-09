export type PlantEntry = {
	id: number;
	plant: number;
	humidity: number;
};

export type Entry = {
	id: number;
	device: number;
	humidity: number;
	temperature: number;
	plantentry_set: PlantEntry[];
	created_at: string;
	updated_at: string;
};
