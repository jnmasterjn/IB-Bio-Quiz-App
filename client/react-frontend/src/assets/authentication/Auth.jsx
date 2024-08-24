import { createContext, useContext, useState, useEffect} from "react";

const AuthContext = createContext(null)

export const useAuth = () => useContext(AuthContext)

//AuthProvider manage isLoggedIn with the useState
export const AuthProvider = ({children}) => {
    
    const [isLoggedIn, setIsLoggedin] = useState(
        localStorage.getItem('isLoggedIn'=== 'true')
    )

    const login = () => {
        setIsLoggedin(true)
        localStorage.setItem('isLoggedIn', 'true') //Store login state in localStorage
    }

    const logout = () => {
        localStorage.removeItem('isLoggedIn')
        localStorage.removeItem('token')
        localStorage.removeItem('name') //remove name and token when logging out
        setIsLoggedin(false)
    }

    return(
        <AuthContext.Provider value={{ isLoggedIn, login, logout }}> 
            {children}
        </AuthContext.Provider>
        //When you call useAuth(), you get the isLoggedIn, login, and logout values from the context.
    )
}



