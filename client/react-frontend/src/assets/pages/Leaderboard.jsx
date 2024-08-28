import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';

function Leaderboard() {

    const API_URL = 'http://127.0.0.1:8000'

    const [rankings, setRankings] = useState([]);

    useEffect(() => {
        axios.get(`${API_URL}/leaderboard/`) //send an api request to the backend
            .then(response => {
                setRankings(response.data);
            })
            .catch(error => {
                console.error('error:', error);
            });
    }, []);

    return (
        <>
        <div>
            <h1>Leaderboard</h1>
            <ul>
                {rankings.map((player, index) => (
                    <ol key={index}>{player.username}: {player.score}</ol>
                ))}
            </ul>
        </div>
        <Link to='../Home'><button>Back to home</button></Link>
        </>
    );
}

export default Leaderboard;
