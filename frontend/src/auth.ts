import { writable } from "svelte/store";
import { browser } from "$app/environment"


export const authToken = writable(browser && localStorage.getItem('authToken') || '');
authToken.subscribe(value => {
    if(!browser) return;
    if(value) {
        localStorage.setItem('authToken', value);
    } else {
        localStorage.removeItem('authToken');
    }
});