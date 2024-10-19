import {Link} from "react-router-dom";

function Home(){

    const name = localStorage.getItem('name')

    return(
        <>
        <div className="box">
        <title>Home</title>
        <div>
            <h2>Welcome back, {name} ! </h2>
        
            <Link to='../rule'><button>Game</button></Link>
            <Link to='../leaderboard'><button>LeaderBoard</button></Link>
            

        </div>
        </div>
        </>
    )
}

export default Home 