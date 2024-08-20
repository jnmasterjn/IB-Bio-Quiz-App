import React from 'react'
import { Navigate } from 'react-router-dom'
import {useAuth} from './Auth.jsx'

const ProtectedRoute = ({ element }) => {
    const { isLoggedIn } = useAuth() // Get the login state from the auth context

    return isLoggedIn ? element: <Navigate to = "/signin"/>// Redirect to /signin if not logged in
};

export default ProtectedRoute;

