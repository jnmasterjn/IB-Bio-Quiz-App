import React from 'react'
import {Link} from "react-router-dom"

function About() {

    return (
        <div className='box'>
            <h1>Overwhelmed with IB Biology's disastrous amount of units?</h1>
            <h3>"Don't worry, I got you. Welcome to IB BioMaster!"</h3>
            <br></br>
            <p>This web app is designed to aid IB Biology students (SL/HL) in studying for their exams.</p>
            <p>All questions are IB-tailored, extracted from public IB databases, IB study guides, and my biology notes (I promise they're good).</p>
            <p>What are you still waiting for? Practice now before it's too late!</p>
            <Link to='../rule'><button>Begin Your 7-Point Journey</button></Link>
        </div>
    );
}

export default About;
