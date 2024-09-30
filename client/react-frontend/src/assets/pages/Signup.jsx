import { useState } from "react"
import { Link, useNavigate } from "react-router-dom"
import { signup } from "../../api.services/api"
import "../css/home.css";



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
        <div className="box">
    
        <title>Signup</title>
            <h1>Create a new account</h1>
            <div>
                <form onSubmit={handleSignup}>
                    <input type="text" placeholder="Username" name="username" className="input-username"></input>
                    <br/>
                    <input type="password" placeholder="Password" name="password" className="input-password"></input>
                    <br/>
                    <br/>
                    <button type="submit">Create my account</button>
                    <br/>
                </form>

                {/* check the value of Error, if it's true generate the <p> */}
                {Error && <p style={{color:'red'}}> Error: Account already exsist. </p>} 
                
                <br/>
                <Link to='../Signin'>Already have an account? Sign in here</Link>
                
            </div>
        </div>
        </>
    )
}

export default Signup
