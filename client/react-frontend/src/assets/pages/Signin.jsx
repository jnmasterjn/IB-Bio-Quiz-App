import { login } from "../../api.services/api";
import { Link } from "react-router-dom";

function Signin() {

    const handleLogin = (e) => {
        e.preventDefault();  // Prevent the form from submitting the traditional way
        const username = e.target.elements.username.value;
        const password = e.target.elements.password.value;

        login(username, password)
            .then(response => {
                console.log('Login successful:', response.data);  // Handle successful login
                // You can redirect the user or set some state here
            })
            .catch(error => {
                console.error('Login failed:', error.response ? error.response.data : error.message);
            });
    };

    return (
        <>
            <h1>Login Page</h1>
            <div>
                <form onSubmit={handleLogin}>
                    <label> Username: </label>
                    <input type="text" placeholder="Insert your username" name="username"></input>
                    <br/>
                    <label> Password: </label>
                    <input type="password" placeholder="Insert your password" name="password"></input>
                    <br/>
                    <button type="submit">Login</button>
                    <br/>
                </form>

                <Link to='../Signup'>Not a member yet?</Link>
                
            </div>
        </>
    )
}

export default Signin;
