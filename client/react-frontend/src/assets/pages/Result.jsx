import { useLocation, Link } from "react-router-dom"



function Result(){

    const location = useLocation() //get current location objext, include the state
    const { Score = 0 } = location.state || {} // Provide a default value of 0 if `state` is null or undefined


    return(
    <>
    <div className="box">
        <title>Result</title>
        
        <h1>Result: </h1>
        <div><h2>Congrats! Your Score is</h2></div>
        <h1>{Score}/10</h1>
        <h4>Score updated to database, please go to <Link to='../leaderboard'>Leaderboard</Link> page to see the rankings.</h4>
        
        <div className="result-button-box">
        <Link to='../rule'><button>Play Another Round</button></Link>
        <Link to='../home'><button>Home Page</button></Link>
        </div>

    </div>
    </>
    )
}

export default Result