import { useState } from "react"
import { useAuth } from "../authentication/Auth"

function NavBar(){

const { isLoggedIn } = useAuth()

const [Displaylogout, SetDisplayLogout] = useState(false)

const {logout} = useAuth()  //access the logout function

const HandleLogout = () => {
    logout()
    SetDisplayLogout(false)
}

return(
    <>
        <nav>
            <div>
                <ul>
                    <li><a href="/Home">Home</a></li>
                    <li><a href="/About">About</a></li>
                    <li><a href="/Contact">Contact</a></li>
                    <li><a href="/Review">Review</a></li>
                    <li><input type="image" src="https://cdn-icons-png.flaticon.com/512/1144/1144760.png" alt="pfp" onClick={ () => {SetDisplayLogout(!Displaylogout)}}/></li>
                </ul>
            </div>
        </nav>

        {/* if alr logged out the button won't show */}
        {(Displaylogout && isLoggedIn)? <div className="display-logout">
            <button onClick={HandleLogout}>Logout</button>
        </div>
            :<></>}

    </>
)
}

export default NavBar