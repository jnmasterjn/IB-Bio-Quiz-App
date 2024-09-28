import ReactDOM from 'react-dom/client'
import React from 'react'
import Signin from './assets/pages/Signin'
import Signup from './assets/pages/Signup'
import Game from './assets/pages/Game'
import Leaderboard from './assets/pages/Leaderboard'
import Home from './assets/pages/Home'
import Result from './assets/pages/Result'
import Rule from './assets/pages/Rule'
import Contact from './assets/pages/Contact'
import About from './assets/pages/About'
import { createBrowserRouter, RouterProvider } from 'react-router-dom'
import { AuthProvider } from './assets/authentication/Auth'
import ProtectedRoute from './assets/authentication/ProtectRoute'
import NavBar from './assets/component/Nav'

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
    path:"home",
    element: <ProtectedRoute element ={<Home/>}/>
  },

  {
    path:"game",
    element:<ProtectedRoute element ={<Game/>}/>
  },

  {
    path:"leaderboard",
    element: <ProtectedRoute element ={<Leaderboard/>}/>
  },

  {
    path:"result",
    element: <ProtectedRoute element ={<Result/>}/>
  },

  {
    path:"Rule",
    element: <ProtectedRoute element ={<Rule/>}/>
  },

  {
    path: "about",
    element: <About/>
  },

  {
    path: "contact",
    element:<Contact/>
  }



  

])

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
      <AuthProvider>
      <NavBar/>
        <RouterProvider router = {myrouter}/>
      </AuthProvider>
  </React.StrictMode>
)
