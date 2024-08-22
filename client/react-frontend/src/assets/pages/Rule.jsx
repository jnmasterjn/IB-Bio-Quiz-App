import {Link} from "react-router-dom"

function Rule(){

    return(
        <>
        <h3>Hello Player</h3>
    <div>
        <h2>Welcome to the game! Here are the rules:</h2>
            <li><b>Time Limit:</b> You have 5 seconds to answer each question.</li>
                <br/>
            <li><b>Scoring:</b> You will earn 1 point for each correct answer.</li>
                <br/>
            <li><b>Rounds:</b> Each round consists of 10 questions.</li>
                <br/>
            <li><b>Starting the Game:</b> The game will begin immediately after you press the "Start Game" button, so be ready!</li>
                <br/>
    </div>


        <Link to='../game'><button>Start Game</button></Link>
        </>
    )
}

export default Rule