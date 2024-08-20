import {useNavigate, Link} from "react-router-dom";

function Home(){
    return(
        <>
        <h1>Home</h1>
        <Link to='../game'><button>Game</button></Link>
        <Link to='../leaderboard'><button>LeaderBoard</button></Link>
        </>
    )
}

export default Home