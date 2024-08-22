import {Link} from "react-router-dom";

function Rule(){

    return(
        <>
        <h3>Hello Player</h3>
    <div>
        <h2>Welcome to the game! Here are the rules:</h2>
            <li>Time Limit: You have 5 seconds to answer each question.</li>
                <br/>
            <li>Scoring: You will earn 1 point for each correct answer.</li>
                <br/>
            <li>Rounds: Each round consists of 10 questions.</li>
                <br/>
            <li>Starting the Game: The game will begin immediately after you press the "Start Game" button, so be ready!</li>
                <br/>
    </div>


        <Link to='../game'><button>Game</button></Link>
        </>
    )
}

export default Rule