import { useState, useEffect } from 'react';

function Review() {

    const [incorrectAnswers, setIncorrectAnswers] = useState([]);

    //load incorrect answers from localStorage when component mounts
    useEffect(() => {
        const storedAnswers = JSON.parse(localStorage.getItem('incorrectAnswers')); //retrieve and parse stored data
        if (storedAnswers) {
            setIncorrectAnswers(storedAnswers); //update state with retrieved answers
        }
    }, []); //run once on component mount

    function clearIncorrectAnswers(){
        localStorage.removeItem('incorrectAnswers'); //remove incorrect answers from localStorage
        setIncorrectAnswers([]) //reset state to an empty array
    }
    
    return (
        <>
            <div className='empty'></div>
            <div className='box'>
                <h2>Review Your Incorrect Answers Here</h2>
                <ul>

            {/* ternary statement to check if there are wrong answers stored*/}
            {incorrectAnswers.length > 0 ? 
                <>
                    {incorrectAnswers.map((item, index) => (
                        <li key={index}>
                            <br/>
                            <p><strong>Question:</strong> {item.question}</p>
                            <p style={{backgroundColor: '#FF7F7F',borderRadius: '5px',padding:'10px'}} className='r-p'>
                                <strong>Your Answer:</strong> {item.userAnswer}</p>
                            <p style={{backgroundColor: '#66CDAA', borderRadius: '5px', padding:'10px'}} className='r-p'>
                                <strong>Correct Answer:</strong> {item.correctAnswer}</p>
                            <br></br>
                        </li>
                    ))}
                </>:    
                // render nothing if there are no incorrect answers
            <></>
            }
                </ul>
        {/* show button if there are incorrect answers that haven't been reviewed */}
        {incorrectAnswers.length > 0 && (
        <button
            onClick={() => {
                clearIncorrectAnswers(); // Clear answers
            }}>
        I have reviewed all my wrong answers.
        </button>
)}
            </div>

        <br/>

        </>
    )
}

export default Review;


