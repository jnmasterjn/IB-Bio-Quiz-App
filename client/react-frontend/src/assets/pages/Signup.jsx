import { useState } from "react"
import { Link, useNavigate } from "react-router-dom"
import { signup } from "../../api.services/api"



function Signup() {

    const path = useNavigate()
    const [Error, setError] = useState(false)
    const handleSignup = (e) => {
        e.preventDefault()
        const username = e.target.elements.username.value
        const password = e.target.elements.password.value

        signup(username, password)
            .then(()=>{
                path('../Signin') // if signup successfully can go to login page
            })

            .catch(()=>{
                setError(true)
            })
    }


    return (
        <>
            <h1>Signup</h1>
            <div>
                <form onSubmit={handleSignup}>
                    <label> Username: </label>
                    <input type="text" placeholder="Insert your username" name="username"></input>
                    <br/>
                    <label> Password: </label>
                    <input type="password" placeholder="Insert your password" name="password"></input>
                    <br/>
                    <br/>
                    <button type="submit">Create my account</button>
                    <br/>
                </form>

                {/* check the value of Error, if it's true generate the <p> */}
                {Error && <p style={{color:'red'}}> Error. Account already exsist. </p>} 

                <Link to='../Signin'>Already have an account? Sign in here!</Link>
                
            </div>
        </>
    )
}

export default Signup
