export type Plant = {
    id: number;
    name: string;
    device: number,
    humidity_limit_max: number | null,
    humidity_limit_min: number | null,
    created_at: string,
    updated_at: string,
};