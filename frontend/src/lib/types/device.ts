export type Device = {
    id: number;
    name: string;
    user: number,
    temperature_limit_max: number | null,
    temperature_limit_min: number | null,
    humidity_limit_max: number | null,
    humidity_limit_min: number | null,
    created_at: string,
    updated_at: string,
};