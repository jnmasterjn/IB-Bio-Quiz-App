import ReactDOM from 'react-dom/client'
import React from 'react'
import Signin from './assets/pages/Signin'
import Signup from './assets/pages/Signup'
import Game from './assets/pages/Game'
import { createBrowserRouter, RouterProvider } from 'react-router-dom'
//need to download from terminal, it's a library

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
    path:"game",
    element: <Game/>
  }

])

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <RouterProvider router = {myrouter}/>
  </React.StrictMode>
)
