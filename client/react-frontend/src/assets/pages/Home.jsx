import {Link} from "react-router-dom";

function Home(){

    const name = localStorage.getItem('name')
    

    return(
        <>
        <h1>Home</h1>
        <h2>Welcome back, {name} ! </h2>
        <Link to='../game'><button>Game</button></Link>
        <Link to='../leaderboard'><button>LeaderBoard</button></Link>
        </>
    )
}

export default Home