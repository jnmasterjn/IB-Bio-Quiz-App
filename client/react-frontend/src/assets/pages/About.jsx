import React from 'react';

function About() {
    return (
        <div className='box'>
        <div style={{ padding: '20px', fontFamily: 'Arial, sans-serif', textAlign: 'center' }}>
            <h1>Welcome to My Trivia App</h1>
            <p>Hello there! 👋</p>
            <p>
                You're currently on the About page of my awesome trivia app, built with <strong>React</strong> on the front-end and <strong>Django</strong> as the back-end.
            </p>
            <p>
                Oh, and guess what? The database I’m using is none other than the simple but mighty <strong>SQLite</strong>. 💾
            </p>
            <p>
                Is this all too fancy? Nah, I'm just goofing around and trying to make it look like I’m doing something complicated... but really, it’s all good fun! 😄
            </p>
            <p>
                Anyway, enjoy the trivia, and remember — the real challenge is not the app, but how well you know IB biology! 🧬🦠
            </p>
        </div>
        </div>
    );
}

export default About;
