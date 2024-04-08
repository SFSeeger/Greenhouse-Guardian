// import type { Actions } from './$types';
// import { PUBLIC_API_INTERNAL_URL } from '$env/static/public';
// import { authToken } from '../../auth';

// export const actions: Actions = {
//     default: async ({fetch, request}) => {
//         const formData = await request.formData();
//         const username = formData.get('username');
//         const password = formData.get('password');

//         const res = await fetch(new URL("auth/login/", PUBLIC_API_INTERNAL_URL), {
//             method: 'POST',
//             headers: {
//                 'Content-Type': 'application/json',
//                 'Authorization': 'Basic ' + btoa(username + ':' + password)
//             },
//         });
//         if (!res.ok) {
//             return {
//                 success:false,
//                 message: await res.text(),
//                 token: null
//             };
//         }
//         const data = await res.json();
//         authToken.set(data.token);
//         return {
//             success:true,
//             token: data.token
//         };
//     }
// };