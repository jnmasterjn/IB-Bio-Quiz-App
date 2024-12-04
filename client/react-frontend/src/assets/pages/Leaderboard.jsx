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
        <div className='box'>
            <title>Leaderboard</title>
            <h1>Leaderboard</h1>
            <p>🔔 Note: The leaderboard ranks players based on their total score, <br></br>
                which is calculated by adding up scores from all the games they’ve played.</p>
            <div style={{ display: 'flex', justifyContent: 'center' }}>
            <table>
                <tr>
                    <th>Rank</th>
                    <th>User</th>
                    <th>Score</th>
                </tr>

                {rankings.map((player, index) => (
                    <tr style = {{'textAlign':'left'}} key = {index}>
                            <td>{index+1}</td>
                            <td>{player.username}</td>
                            <td>{player.score}</td>
                    </tr>
                ))}
            </table>
            </div>
        <br/>
        <Link to='../Home'><button>Back to home</button></Link>
        </div>
        </>
    );
}

export default Leaderboard;




