import { createContext, useContext, useState } from "react";

const AuthContext = createContext(null)

export const useAuth = () => useContext(AuthContext)

//AuthProvider manage isLoggedIn with the useState
export const AuthProvider = ({children}) => {
    
    const [isLoggedIn, setIsLoggedin] = useState(false)

    const login = () => {
        setIsLoggedin(true)
    }

    const logout = () => {
        setIsLoggedin(false)
    }

    return(
        <AuthContext.Provider value={{ isLoggedIn, login, logout }}> 
            {children}
        </AuthContext.Provider>
        //When you call useAuth(), you get the isLoggedIn, login, and logout values from the context.
    )
}


