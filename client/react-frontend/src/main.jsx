import ReactDOM from 'react-dom/client'
import React from 'react'
import Signin from './assets/pages/Signin'
import Signup from './assets/pages/Signup'
import Game from './assets/pages/Game'
import Leaderboard from './assets/pages/Leaderboard'
import Home from './assets/pages/Home'
import Result from './assets/pages/Result'
import Rule from './assets/pages/Rule'
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
    element:<Game/>
  },

  {
    path:"Leaderboard",
    element: <Leaderboard/>
  },

  {
    path:"Result",
    element: <ProtectedRoute element ={<Result/>}/>
  },

  {
    path:"Rule",
    element: <ProtectedRoute element ={<Rule/>}/>
  }

  

])

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
      <AuthProvider>
        <RouterProvider router = {myrouter}/>
      </AuthProvider>
  </React.StrictMode>
)
