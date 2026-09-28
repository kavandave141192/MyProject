import axios from "axios"
import { ACCESS_TOKEN } from "./constants"

// api is your Axios configuration for communicating with Django.
//  api.post(...)you're basically saying:"React, send a POST request to my Django backend."

const api=axios.create(
    {
        baseURL:import.meta.env.VITE_API_URL
    }
)
// Think of an interceptor as a checkpoint that every request passes through before Axios sends it.
// Your code says:

// React wants to make API request
//              ↓
//        Axios interceptor
//              ↓
//      Check localStorage
//              ↓
//      Is access token there?
//              ↓
//       Add Authorization header
//              ↓
//         Send to Django

// This is why you don't have to manually add the JWT to every request.

api.interceptors.request.use(
    // config represents the configuration of the Axios request.
    (config)=>{
        const token=localStorage.getItem(ACCESS_TOKEN)
        if(token){
            config.headers.Authorization=`Bearer ${token}`
        }
        return config
    },
    (error)=>{
        return Promise.reject(error)
    }
)
export default api