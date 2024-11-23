import { Link } from "react-router-dom";

function Home() {
    const name = localStorage.getItem('name');

    return (
        <>
        <div className="box">
            <title>Home</title>
            <div>
                <h1>Welcome Back, {name}!</h1>
                <p style={{ fontStyle: "italic", fontSize: "18px" }}>
                    "Ready to conquer IB Biology today?"
                </p>

                <div style={{ margin: "20px 0", display: "flex", gap: "20px", justifyContent: "center" }}>
                    <Link to='../rule'>
                        <button className="h-button">🎮 Game</button>
                    </Link>

                    <Link to='../leaderboard'>
                        <button className="h-button">🏆 Leaderboard</button>
                    </Link>

                    <Link to='../review'>
                        <button className="h-button">🔍 Review</button>
                    </Link>
                </div>

                <div>
                    <p>💡 Tip of the Day: Practice makes perfect! Take on a quiz and climb the leaderboard. 💡</p>
                </div>
            </div>
        </div>
        </>
    );
}

export default Home;
