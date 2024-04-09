type SlimSelectOption = {
	value: string;
	text: string;
};
type SlimSelectOptgroup = {
	label: string;
	options: SlimSelectOption[];
};
export type SlimSelectData = SlimSelectOption[] | SlimSelectOptgroup[];
