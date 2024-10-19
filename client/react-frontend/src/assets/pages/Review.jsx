import { useState, useEffect } from 'react';

function Review() {
    const [incorrectAnswers, setIncorrectAnswers] = useState([]);

    // Load incorrect answers from localStorage when the component mounts
    useEffect(() => {
        const storedAnswers = JSON.parse(localStorage.getItem('incorrectAnswers'));
        if (storedAnswers) {
            setIncorrectAnswers(storedAnswers);
        }
    }, []);

    function clearIncorrectAnswers(){
        localStorage.removeItem('incorrectAnswers');
        setIncorrectAnswers([])
    }
    
    return (
        <>
        <div className='box'>
            <h2>Review Your Incorrect Answers Here</h2>
            <ul>

        {/* ternary statement to check if there are wrong answers */}
        {incorrectAnswers.length > 0 ? 
            <>
                {incorrectAnswers.map((item, index) => (
                    <li key={index}>
                        <p><strong>Question:</strong> {item.question}</p>
                        <p><strong>Your Answer:</strong> {item.userAnswer}</p>
                        <p><strong>Correct Answer:</strong> {item.correctAnswer}</p>
                        <br></br>
                    </li>
                ))}
            </>:
        <></>
        }
            </ul>
        </div>
        
        {/* show button when there are incorrect answer that haven't been reviewed */}
        {incorrectAnswers.length > 0 && (
        <button
            onClick={(e) => {
                clearIncorrectAnswers(); // Clear answers
                e.target.innerText = "Please refresh the page";
            }}
        >
        I have reviewed all my wrong answers.
    </button>
)}

        <br/>

        </>
    )
}

export default Review;


