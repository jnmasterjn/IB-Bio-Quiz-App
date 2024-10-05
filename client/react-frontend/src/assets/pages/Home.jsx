import {Link} from "react-router-dom";

function Home(){

    const name = localStorage.getItem('name')

    return(
        <>
        <div className="box">
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

        </div>
        </div>
        </>
    )
}

export default Home 