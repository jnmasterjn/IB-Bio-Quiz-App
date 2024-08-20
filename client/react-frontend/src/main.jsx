import ReactDOM from 'react-dom/client'
import React from 'react'
import Signin from './assets/pages/Signin'
import Signup from './assets/pages/Signup'
import Game from './assets/pages/Game'
import Leaderboard from './assets/pages/Dashboard'
import Home from './assets/pages/Home'
import { createBrowserRouter, RouterProvider } from 'react-router-dom'
import { AuthProvider } from './assets/authentication/Auth'
import ProtectedRoute from './assets/authentication/ProtectRoute'

const myrouter = createBrowserRouter([
  {
    path:"signin",
    element: <Signin/>
  },
  
  {
    path:"signup",
    element: <Signup/>
  },

  {
    path:"Home",
    element: <ProtectedRoute element ={<Home/>}/>
  },

  {
    path:"game",
    element: <ProtectedRoute element ={<Game/>}/>
  },

  {
    path:"Leaderboard",
    element: <ProtectedRoute element ={<Leaderboard/>}/>}
  

])

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
      <AuthProvider>
        <RouterProvider router = {myrouter}/>
      </AuthProvider>
  </React.StrictMode>
)
