import { useState } from "react";
import { login } from "../../api.services/api";
import { Link, useNavigate} from "react-router-dom";
import { useAuth } from "../authentication/Auth";


function Signin() {

    const path = useNavigate() //used to redirect user to other pages once signed in

    const {login: authLogin} = useAuth() //rename login from auth.jsx to use authLogin

    const [Error, setError ] = useState(false)

    const handleLogin = (e) => {
        e.preventDefault(); //prevent reloading the page
        const username = e.target.elements.username.value; //get user insert username from input field 
        const password = e.target.elements.password.value; //get user insert password from input field 

        login(username, password) //call login function with the received username and password

            .then((response) => {

                const token = response.data.token // Retrieve the token from the response data
                
                localStorage.setItem('name', username) //store the user's login name to display on home page, name is the variable
                localStorage.setItem('token', token) //store token 

                authLogin() //updates the isLoggedIn state in your authentication context, mark user as logged in
                
                path('../home') //if they login they can go to the game page.
            })

            .catch(() => {
                setError(true) //change Error from useState to true since the loginf failed there's an error.
            });
    };

    return (
        <>
        <div>
            <title>Signin</title>
            <h1>Welcome back, Please Login</h1>
            <div>
                <form onSubmit={handleLogin}>
                    <label> Username: </label>
                    <input type="text" placeholder="Insert your username" name="username"></input>
                    <br/>
                    <label> Password: </label>
                    <input type="password" placeholder="Insert your password" name="password"></input>
                    <br/>
                    <br/>
                    <button type="submit">Login</button>
                    <br/>
                </form>

                {/* check the value of Error, if it's true generate the <p> */}
                {Error && <p style={{color:'red'}}> Login failed. Please try again. </p>} 

                {/* if the user want to make a new acc redirect them to the signup page */}
                <br/>
                <Link to='../Signup'>Not a member yet? Join now for free!</Link>
                
            </div>
        </div>
        </>
    )
}

export default Signin
