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

export const user = writable(browser && JSON.parse(localStorage.getItem('user') || '{}') || "");
user.subscribe(value => {
    if(!browser) return;
    if(value) {
        localStorage.setItem('user', JSON.stringify(value));
    } else {
        localStorage.removeItem('user');
    }
});