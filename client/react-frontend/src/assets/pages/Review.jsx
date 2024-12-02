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
            <div className='empty'></div>
            <div className='box'>
                <h2>Review Your Incorrect Answers Here</h2>
                <ul>

            {/* ternary statement to check if there are wrong answers */}
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
                
            <></>
            }
                </ul>
        {/* show button when there are incorrect answer that haven't been reviewed */}
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


