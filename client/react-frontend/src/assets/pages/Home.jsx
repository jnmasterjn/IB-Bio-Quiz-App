import {Link, useNavigate} from "react-router-dom";
import { useAuth } from "../authentication/Auth";

function Home(){

    const name = localStorage.getItem('name')

    const {logout} = useAuth()  //access the logout function
    const path = useNavigate()

    const HandleLogout = () => {
        logout()
        path('../Signin')
    }
    

    return(
        <>
        <div>
            <h1>Home</h1>
            <h2>Welcome back, {name} ! </h2>
            <Link to='../rule'><button>Game</button></Link>
            <Link to='../leaderboard'><button>LeaderBoard</button></Link>

            <button onClick={HandleLogout}>Logout</button>
        </div>
        </>
    )
}

export default Home 