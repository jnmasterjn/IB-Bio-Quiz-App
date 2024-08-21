import {quiz} from "../../api.services/api"
import { useState, useEffect } from "react"



function Game(){

    const [questions, SetQuestions] = useState([])
    const [CurrentQuestion, SetCurrentQuestion] = useState(0)
    const [selected, SetSelected] = useState(null)
    const [isCorrect, SetIsCorrect] = useState(null)
    

    useEffect( () => {
        quiz()
            .then( (serverresponse) => {
                SetQuestions(serverresponse.data)
            })
            .catch( (error) => {
                console.error(error)
            })
    },[]
    )

    return(
    <div>
        <h1>Game Page</h1>
        {questions.map((quiz, index) => (
            <div key={index}>
                <h2>{quiz.question} ?</h2>  {/* This accesses and renders the question text */}
                <button>{quiz.optionOne}</button>  {/* This renders the first option */}
                <button>{quiz.optionTwo}</button>  {/* This renders the second option */}
                <button>{quiz.optionThree}</button>  {/* This renders the third option */}
            </div>
        ))}
    </div>
);
}

export default Game