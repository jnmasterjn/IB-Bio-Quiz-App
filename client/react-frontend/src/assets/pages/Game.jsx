import {quiz} from "../../api.services/api"
import { useState, useEffect } from "react"



function Game(){

    const [questions, SetQuestions] = useState([])
    const [CurrentQuestionIndex, SetCurrentQuestionIndex] = useState(0) //keep track of the current question's index, start with [0]
    const [selected, SetSelected] = useState(null)
    const [isCorrect, SetIsCorrect] = useState(null)
    

    useEffect( () => {
        quiz()
            .then( (serverresponse) => {
                const RandomQuestion = FisherShuffle(serverresponse.data) 
                //creates a new object based on q
                const QuestionWithShuffleOptions = RandomQuestion.map( q => ({
                    ...q, 
                    options: FisherShuffle([q.optionOne, q.optionTwo, q.optionThree]) //This adds a property named options in the new object.
                }))
                SetQuestions(QuestionWithShuffleOptions) //this question object now contains the shuffle options too

            })
            .catch( (error) => {
                console.error(error)
            })
    },[]
    ) //renders once element mounts, fetch data from server


    function FisherShuffle(array){
        let i = array.length-1 //the last index

        for (; i > 0;i--){ 
            const j = Math.floor(Math.random() * (i + 1));
            [array[i],array[j]] = [array[j],array[i]]
        }
        return array
    }

    if (questions.length === 0){
        return(
            <div>Loading....</div>
        )
    }      

    const currentQuestion = questions[CurrentQuestionIndex] //very important line

    //ensure the question and options are already defined before rendering it to user
    if (!currentQuestion || !currentQuestion.options) {
        return <div>Loading question...</div>;
    }

    const HandleUserAnswer = (selectedAnswer) => {
        if (selectedAnswer === currentQuestion.answer){
            SetIsCorrect(true)
        }else{
            SetIsCorrect(false)
        }
    }


    return (
        <div>
            <h1>Game Page</h1>
            <h2>Question: {currentQuestion.question}</h2>
            {currentQuestion.options.map((option, index) => (
                <button key={index} onClick={() => HandleUserAnswer(option)}>
                    {option}
                </button>
            ))}
            {isCorrect === true && <p style ={{color:'green'}}>Correct!</p>}
            {isCorrect === false && <p style ={{color:'red'}}>Failed</p>}
        </div>
    );
}

export default Game