import {quiz} from "../../api.services/api.jsx"
import { useState, useEffect } from "react"
import FisherShuffle from '../logic/Shuffle.js'
import {useNavigate, Link} from "react-router-dom"
import '../css/main.css'
import axios from 'axios';

function Game(){

    const name = localStorage.getItem('name')

    const API_URL = 'http://127.0.0.1:8000'

    const path = useNavigate()

    const [questions, SetQuestions] = useState([]) // store quiz questions
    const [CurrentQuestionIndex, SetCurrentQuestionIndex] = useState(0) //  track current question's index
    const [hasAnswered, SetHasAnswered] = useState(false) // prevent multiple answers
    const [Score, SetScore] = useState(0) // user score
    const [TimeLeft, SetTimeLeft] = useState(30) // time left for each question
    const [AnswerMessage, SetAnswerMessage] = useState('') // feedback message
    const [MessageColor, SetMessageColor] = useState('') // feedback message color
    const [IncorrectAnswers, SetIncorrectAnswers] = useState([]) // track incorrect answers

    //so old incorrect answer don't get delete after a new game.
    useEffect(() => {
        const storedAnswers = JSON.parse(localStorage.getItem("incorrectAnswers"));
        if (storedAnswers) {
        SetIncorrectAnswers(storedAnswers);
        }
    }, []);

    useEffect( () => {
        quiz() //calls quiz() to fetch questions from server
            .then( (serverresponse) => {
                //shuffle the question using Fisher-Yates algorithm
                const RandomQuestion = FisherShuffle(serverresponse.data) 
                const QuestionWithShuffleOptions = RandomQuestion.map( q => ({
                    ...q, 
                    options: FisherShuffle([q.optionOne, q.optionTwo, q.optionThree]) //add shuffled options
                }))
                SetQuestions(QuestionWithShuffleOptions) 
                //update state with shuffled questions, options 
            })
            .catch( (error) => {
                console.error(error) //log errors
            })
    },[]) //run once on component mount

    useEffect( () => {
        if (TimeLeft > 0){
            const timer = setTimeout( () => {
                SetTimeLeft(TimeLeft-1) //decrease time by 1 every second
            },1000)

            return ()=> clearTimeout(timer) //clear timer on unmounts/TimeLeft changes

            }else{
                HandleUserAnswer(null) //run effect when TimeLeft changes
            } 
        },
        [TimeLeft])

    useEffect( () => {
        if (CurrentQuestionIndex == 10){
            SubmitScore(Score) //send user score to the backend
            path('../result', {state: {Score}}) //pass Score as an object and use useLocation on the result page to use this data
        }
    },[CurrentQuestionIndex]
    )

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

         //track incorrect answers
        let newIncorrectAnswers = [...IncorrectAnswers];

        if (selectedAnswer !== currentQuestion.answer) {
            //save incorrect answer details
            newIncorrectAnswers.push({
                question: currentQuestion.question,
                correctAnswer: currentQuestion.answer,
                userAnswer: selectedAnswer,
            });
            //update state with the new incorrect answers
            SetIncorrectAnswers(newIncorrectAnswers);
            //store the incorrect answers in localStorage for review purposes
            localStorage.setItem('incorrectAnswers', JSON.stringify(newIncorrectAnswers)); 
        }

        setTimeout( () => {
        SetCurrentQuestionIndex(CurrentQuestionIndex+1) //increament current question index
        SetTimeLeft(30)//reset timer to 30 seconds for next question

        SetHasAnswered(false)
        
        SetMessageColor("") //set color to empty string
        SetAnswerMessage("") //empty the message for next question

    },2000) //two second before next question

    if (selectedAnswer === currentQuestion.answer){
            
        SetScore(Score+1)

        SetMessageColor('green')
        SetAnswerMessage("CORRECT!")

    }else{
        SetMessageColor('red')
        SetAnswerMessage("Oops..")
    }

    SetHasAnswered(true) //has answered the question, so can't press the buttons again
    }


    const SubmitScore = (score) => {

        //retrieve user token from localStorage
        const token = localStorage.getItem('token')

        return axios.post(`${API_URL}/score/`, 
        {score: score}, //send the score as payload to the backend
            {
                headers: { 'Authorization': `Token ${token}`} //include authorization header
            }
        ) 
        .then( (response) =>{
            console.log("success sending score", response.data) //log success response
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
            <title className="game-title">Game</title>
    
            <h4 className="time-left">Player: {name}</h4>
            <h4 className="time-left">Time Left: {TimeLeft}</h4>
            <h4 className="time-left">Question {CurrentQuestionIndex+1}/10</h4>
            <h1 className="question-index">Question {CurrentQuestionIndex+1}</h1>
            <br/>

            <h2>{currentQuestion.question}</h2>

            <div className="game-button-container">

            {currentQuestion.options.map((option, index) => (
                <button key={index} className="game-button"
                        onClick={() => HandleUserAnswer(option)}>
                    {option}
                </button>
            ))}
            </div>
            <strong><p style={{color: MessageColor}}>{AnswerMessage}</p></strong>
            <h5 className="quit-game"><Link to = '../home'>Quit Game:(</Link></h5>
        </div>
    </div>
        </>
    );
}

export default Game