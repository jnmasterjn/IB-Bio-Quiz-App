import {quiz} from "../../api.services/api"
import { useState, useEffect } from "react"
import FisherShuffle from './Shuffle.js'



function Game(){

    const [questions, SetQuestions] = useState([])
    const [CurrentQuestionIndex, SetCurrentQuestionIndex] = useState(0) //keep track of the current question's index, start with [0]
    const [hasAnswered, SetHasAnswered] = useState(false)
    

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

    if (questions.length === 0){
        return(
            <div>Loading....</div>
        )
    }      

    let currentQuestion = questions[CurrentQuestionIndex] //very important line

    //ensure the question and options are already defined before rendering it to user
    if (!currentQuestion || !currentQuestion.options) {
        return <div>Loading question....</div>;
    }

    const HandleUserAnswer = (selectedAnswer) => {

        if (hasAnswered === true){
            return
        }


        if (selectedAnswer === currentQuestion.answer){
            console.log('correct')
        }else{
            console.log('incorrect')
        }

        SetHasAnswered(true) //has answered the question, so can't press the buttons again
        
        setTimeout( () => {
        if (CurrentQuestionIndex < questions.length-1){ //keep going to the next question when the questions are enough
            SetCurrentQuestionIndex(CurrentQuestionIndex+1) 
        }else{
            alert('Quiz Completed')
        }
        SetHasAnswered(false)
    },1000) //one seconds before next question
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
        </div>
    );
}

export default Game