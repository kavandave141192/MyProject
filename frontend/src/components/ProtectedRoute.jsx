import {Navigate} from "react-router-dom"
import {jwtDecode} from "jwt-decode"
import api from "../api"
import { ACCESS_TOKEN, REFRESH_TOKEN } from "../constants"
import { useState,useEffect } from "react"

// Your Django backend gives your React application a JWT.A JWT contains information such as an expiration time.
// Conceptually:
// JWT
// │
// ├── user information
// ├── issued time
// └── expiration time.....jwtDecode() allows React to read the payload of the JWT

function ProtectedRoute({children}){
    // children = <Home />

    const [isAuthorized,setIsAuthorized]=useState(null)
    //  null  → checking
    // true       → authorized
    // false      → not authorized

    useEffect(()=>{
        auth().catch(()=>setIsAuthorized(false))
    },[])
            // Load ProtectedRoute
            //        ↓
            // useEffect runs
            //        ↓
            // auth()
            //        ↓
            // Check authentication


    const refreshToken=async()=>{
        const refresh=localStorage.getItem(REFRESH_TOKEN)
        // React, give me the access token that we previously stored.

        try{
            const res=await api.post("api/token/refresh/",{refresh:refreshToken})
            // React
            // │
            // │ POST
            // │ refresh token
            // ▼
            // Django
            // /api/token/refresh/
            // │
            // ▼
            // TokenRefreshView
            // │
            // ▼
            // Validate refresh token
            // │
            // ▼
            // Create new access token

            if(res.status===200){
                localStorage.setItem(ACCESS_TOKEN,res.data.access)
                // Replace the old expired access token with the new access token returned by Django.

                setIsAuthorized(true)
            }
            else{
                setIsAuthorized(false)
            }

        }catch(error){
                console.log(error)
                setIsAuthorized(false)
        }
    }

    const auth=async()=>{
        const token=localStorage.getItem(ACCESS_TOKEN)
        if(!token){
            setIsAuthorized(false)
            return        }

                // User
                //  ↓
                //    /
                //  ↓
                // ProtectedRoute
                //  ↓
                // No access token
                //  ↓
                // isAuthorized = false
                //  ↓
                // /login

        const decoded=jwtDecode(token)
        const tokenExpiration=decoded.exp
        // Has the access token expired?

        const now=Date.now()/1000

        if(tokenExpiration<now){
            await refreshToken()
        }else{
            setIsAuthorized(true)
        }

    }
    if (isAuthorized===null){
        return <div>Loading....!!!</div>
    }

    return isAuthorized ? children:<Navigate to="/login" />
        //     IF isAuthorized is true
        //     → show children
        //     ELSE
        //     → redirect to /login

}
export default ProtectedRoute