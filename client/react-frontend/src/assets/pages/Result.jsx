import { useLocation } from "react-router-dom"



function Result(){

    const location = useLocation() //get current location objext, include the state
    const { Score = 0 } = location.state || {} // Provide a default value of 0 if `state` is null or undefined


    return(
    <>
        <h1>Result: </h1>
        <div><h2>Your Score is {Score}/10</h2></div>
    </>
    )
}

export default Result