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
        localStorage.clear()
        console.log('deleted local storage')
    }
    
    return (
        <>
        <div>
            <h2>Review Your Incorrect Answers</h2>
            <ul>
        {incorrectAnswers.map((item, index) => (
            <li key={index}>
                <p><strong>Question:</strong> {item.question}</p>
                <p><strong>Your Answer:</strong> {item.userAnswer}</p>
                <p><strong>Correct Answer:</strong> {item.correctAnswer}</p>
                <br></br>
            </li>
        ))}
            </ul>
        </div>
        
        {/* show button when there are incorrect answer that haven't been reviewed */}
        {incorrectAnswers.length>0  && 
        (<button onClick={clearIncorrectAnswers}>I have reviewed all my wrong answers.</button>)
        }

        

        </>
    )
}

export default Review;


