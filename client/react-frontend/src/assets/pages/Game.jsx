import {quiz} from "../../api.services/api.jsx"
import { useState, useEffect } from "react"
import FisherShuffle from '../logic/Shuffle.js'
import {useNavigate, Link} from "react-router-dom";
import '../css/main.css'
import axios from 'axios';


function Game(){

    const name = localStorage.getItem('name')

    const API_URL = 'http://127.0.0.1:8000'

    const path = useNavigate()

    const [questions, SetQuestions] = useState([])
    const [CurrentQuestionIndex, SetCurrentQuestionIndex] = useState(0) //keep track of the current question's index, start with [0]
    const [hasAnswered, SetHasAnswered] = useState(false) //user can only answer each question once
    const [Score, SetScore] = useState(0)
    const [TimeLeft, SetTimeLeft] = useState(5) //5 seconds for each question
    const [AnswerMessage, SetAnswerMessage] = useState("")
    const [MessageColor, SetMessageColor] = useState('')
    const [IncorrectAnswers, SetIncorrectAnswers] = useState([])
    


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
            },2000)

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

    //main function
    const HandleUserAnswer = (selectedAnswer) => {

        if (hasAnswered === true){
            return
        } //if user alr answered this question, they can't answer again

         // Track incorrect answers
        let newIncorrectAnswers = [...IncorrectAnswers];

        if (selectedAnswer !== currentQuestion.answer) {
        // Save incorrect answer details
        newIncorrectAnswers.push({
            question: currentQuestion.question,
            correctAnswer: currentQuestion.answer,
            userAnswer: selectedAnswer,
        });
    }
        // Update state and localStorage
        SetIncorrectAnswers(newIncorrectAnswers);
        localStorage.setItem('incorrectAnswers', JSON.stringify(newIncorrectAnswers));

        if (selectedAnswer === currentQuestion.answer){
            
            SetScore(Score+1)

            SetMessageColor('green')
            SetAnswerMessage("CORRECT")
            
            console.log(MessageColor)

        }else{

            SetMessageColor('red')
            SetAnswerMessage(`WRONG, correct answer: ${currentQuestion.answer}`)
            
            console.log(MessageColor)
        }

        SetHasAnswered(true) //has answered the question, so can't press the buttons again
        
        setTimeout( () => {
        if (CurrentQuestionIndex < 9){ //10 questions per round
            SetCurrentQuestionIndex(CurrentQuestionIndex+1) 
            SetTimeLeft(5)
        }else{
            SubmitScore(Score) //send user score to the backend
            path('../result', {state: {Score}}) //pass Score as an object and use useLocation on the result page to use this data
        }
        SetHasAnswered(false)
        
        SetMessageColor("") //set color to empty string
        SetAnswerMessage("") //empty the message for next question


    },1000) //one second before next question
    }


    const SubmitScore = (score) => {

        const token = localStorage.getItem('token')

        return axios.post(`${API_URL}/score/`, 
        {score: score}, //score is the payload send to the backend function
            {
                headers: { 'Authorization': `Token ${token}`} //make sure user is logged in
            }
        ) 
        .then( (response) =>{
            console.log("success sending score", response.data)
        })

        .catch( (error) =>{
            if (error.response){
                console.log("failed sending score, response data:", error.response.data)
            }
            console.log("failed sending score", error)
        })
    }


    return (<>
    <div className="box">
        <div>
            <title>Game</title>
    
            <h4>Player: {name}</h4>
            <h4>Time Left: {TimeLeft}</h4>
            <h1>Question {CurrentQuestionIndex+1}</h1>

            <h2>{currentQuestion.question}</h2>
            {currentQuestion.options.map((option, index) => (
                <button key={index} 
                        onClick={() => HandleUserAnswer(option)}>
                    {option}
                </button>
            ))}
            
            <p style={{color: MessageColor}}>{AnswerMessage}</p>

        </div>
        <h5><Link to = '../home'>Quit Game</Link></h5>
    </div>
        </>
    );
}

export default Game