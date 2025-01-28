import ReactDOM from 'react-dom/client'
import React from 'react'
import { AuthProvider } from './assets/authentication/Auth'
import ProtectedRoute from './assets/authentication/ProtectRoute'
import NavBar from './assets/component/Nav'
import Game from './assets/pages/Game'
import Leaderboard from './assets/pages/Leaderboard'
import Result from './assets/pages/Result'
import Rule from './assets/pages/Rule'
import Contact from './assets/pages/Contact'
import Review from './assets/pages/Review'
import About from './assets/pages/About'
import Nothing from './assets/pages/Nothing'


import { createBrowserRouter, RouterProvider } from 'react-router-dom' // import routing components
import Signin from './assets/pages/Signin' // import Signin page component
import Signup from './assets/pages/Signup' // import Signup page component
import Home from './assets/pages/Home' // import Home page component

// define the router configuration
const myrouter = createBrowserRouter([

  {path:"",
    element: <Nothing/>},

  {path:"signin", // signin route
    element: <Signin/>},

  {path:"signup", // signup route
    element: <Signup/>},

  {path:"home", // protected home route
    element: <ProtectedRoute element ={<Home/>}/>},

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
  }, 

  {
    path: "review",
    element:<ProtectedRoute element ={<Review/>}/>

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