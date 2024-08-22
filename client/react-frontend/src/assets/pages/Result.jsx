import { useLocation, Link } from "react-router-dom"



function Result(){

    const location = useLocation() //get current location objext, include the state
    const { Score = 0 } = location.state || {} // Provide a default value of 0 if `state` is null or undefined


    return(
    <>
        <h1>Result: </h1>
        <div><h2>Congrats! Your Score is</h2></div>
        <h1>{Score}/10</h1>
        <Link to='../rule'><button>Play Another Round</button></Link>
        <Link to='../home'><button>Home Page</button></Link>
    </>
    )
}

export default Result