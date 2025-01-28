import {Link} from "react-router-dom"

function Nothing() {

    return (
        <>
            <h1>Welcome!</h1>
            <Link to='../signin'><button>Signin here</button></Link>
        
        </>
    );
}

export default Nothing;
