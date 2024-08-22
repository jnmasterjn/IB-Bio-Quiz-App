import {quiz} from "../../api.services/api.jsx"
import { useState, useEffect } from "react"
import FisherShuffle from '../logic/Shuffle.js'
import {useNavigate, Link} from "react-router-dom";
import '../css/Test.css'



function Game(){

    const path = useNavigate()

    const [questions, SetQuestions] = useState([])
    const [CurrentQuestionIndex, SetCurrentQuestionIndex] = useState(0) //keep track of the current question's index, start with [0]
    const [hasAnswered, SetHasAnswered] = useState(false) //user can only answer each question once
    const [Score, SetScore] = useState(0)
    const [TimeLeft, SetTimeLeft] = useState(5) //5 seconds for each question
    

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

    useEffect( () => {
        if (TimeLeft > 0){
            const timer = setTimeout( () => {
                SetTimeLeft(TimeLeft-1)
            },1000)

            return ()=> clearTimeout(timer) //clear the timer when components unmounts / timeLeft changes

            }else{
                HandleUserAnswer(null) //if the timer runs out
            } 
        },
        [TimeLeft])

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
            SetScore(Score+1)
        }else{
            console.log('incorrect')
        }

        SetHasAnswered(true) //has answered the question, so can't press the buttons again
        
        setTimeout( () => {
        if (CurrentQuestionIndex < 9){ //10 questions per round
            SetCurrentQuestionIndex(CurrentQuestionIndex+1) 
            SetTimeLeft(5)
        }else{
            path('../result', {state: {Score}}) //pass Score as an object and use useLocation on the result page to use this data
        }
        SetHasAnswered(false)
    },1000) //one seconds before next question
    }

    return (<>
        <div>
            <h4>Game Page</h4>
            <h4>Time Left: {TimeLeft}</h4>
            <h1>Question {CurrentQuestionIndex+1}</h1>
            <h2>{currentQuestion.question}</h2>
            {currentQuestion.options.map((option, index) => (
                <button key={index} onClick={() => HandleUserAnswer(option)}>
                    {option}
                </button>
            ))}
        </div>
        </>
    );
}

export default Game