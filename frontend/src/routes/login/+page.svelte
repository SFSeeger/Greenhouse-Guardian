<script lang="ts">
	import { goto } from '$app/navigation';
	import { PUBLIC_API_URL } from '$env/static/public';
	import { authToken, user } from '../../auth';
	import type { ActionData, PageData } from './$types';
	import { error } from '@sveltejs/kit';
	import guardianIcon from '$lib/assets/images/Greenhouse.svg'

	export let data: PageData;

	let formData = {
		username: '',
		password: ''
	};

	let errors: string[] = [];

	const login = async () => {
		const res = await fetch(new URL('auth/login/', PUBLIC_API_URL), {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
				Authorization: 'Basic ' + btoa(formData.username + ':' + formData.password)
			}
		});
		if (!res.ok) {
			if (res.status === 401) {
				await res
					.json()
					.then((req_data) => req_data.detail)
					.then((detail) => {
						errors = [errors, ...detail];
					});
			}
			error(res.status, await res.text());
		}
		const data = await res.json();
		authToken.set(data.token);
		user.set(data.user);
		goto(new URLSearchParams(window.location.search).get('redirect-to') || '/dashboard');
	};
</script>

<svelte:head>
    <title>Login - Greenhouse Guardian</title> 
</svelte:head>

{#each errors as error}
	<div
		class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative"
		role="alert"
	>
		<strong class="font-bold">Error!</strong>
		<span class="block sm:inline">{error}</span>
	</div>
{/each}

<div class="flex min-h-full flex-col justify-center px-6 py-12 lg:px-8">
	<div class="sm:mx-auto sm:w-full sm:max-w-sm">
		<img
			class="mx-auto h-auto w-20"
			src="{guardianIcon}"
			alt="Greenhouse guardian"
		/>
		<h2 class="mt-5 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900">
			Sign in to your account
		</h2>
	</div>

	<div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
		<form class="space-y-6" method="POST" on:submit|preventDefault={login}>
			<div>
				<label for="username" class="block text-sm font-medium leading-6 text-gray-900"
					>Username <span class="text-red-500">*</span></label
				>
				<div class="mt-2">
					<input
						id="username"
						name="username"
						type="username"
						autocomplete="username"
						required
						bind:value={formData.username}
					/>
				</div>
			</div>

			<div>
				<div class="flex items-center justify-between">
					<label for="password" class="block text-sm font-medium leading-6 text-gray-900"
						>Password <span class="text-red-500">*</span></label
					>
					<div class="text-sm">
						<a href="#" class="font-semibold text-indigo-600 hover:text-indigo-500"
							>Forgot password?</a
						>
					</div>
				</div>
				<div class="mt-2">
					<input
						id="password"
						name="password"
						type="password"
						autocomplete="current-password"
						required
						bind:value={formData.password}
					/>
				</div>
			</div>

			<div>
				<button
					type="submit"
					class="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
					>Sign in</button
				>
			</div>
		</form>
	</div>
</div>
