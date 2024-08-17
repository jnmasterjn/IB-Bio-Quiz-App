import { login } from "../../api.services/api"

import {Link} from "react-router-dom"

function Signin() {

    return (
    <>
        <h1>Login Page</h1>
        <div>
            <form>
                <label> Username: </label>
                <input type="text" placeholder="Insert your username" name="username"></input>
                <br/>
                <label> Password: </label>
                <input type="password" placeholder="Insert your password" name="password"></input>

                <br/>
                <button onClick={login}>Login</button>
                <br/>
            </form>

            <Link to='../Signup'>Not a member yet?</Link>
            
        </div>
    </>
    )
}

export default Signin
