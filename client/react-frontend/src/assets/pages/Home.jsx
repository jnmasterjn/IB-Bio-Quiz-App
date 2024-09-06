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
        <title>Home</title>
        <div>
            <h2>Welcome back, {name} ! </h2>
            <h3>
            Welcome to our fun and interactive biology trivia website. <br/>
            Dive into a world of fascinating questions about cells, animals, plants, and everything in between. <br/>
            Get ready to test your knowledge, learn cool facts, and have a blast along the way!
            </h3>
            <Link to='../rule'><button>Game</button></Link>
            <Link to='../leaderboard'><button>LeaderBoard</button></Link>

            <button onClick={HandleLogout}>Logout</button>
        </div>
        </>
    )
}

export default Home 