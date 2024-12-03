//Trivia/client/react-frontend/src/api.services/api.jsx

import axios from 'axios' //import axios for HTTP requests

const API_URL = 'http://127.0.0.1:8000' //backend API (local)

//fetch quiz data from the server
export const quiz = () => {
    //send GET request to /quiz endpoint
    return axios.get(`${API_URL}/quiz/`)
}

export const signup = (username, password) => {
    return axios.post(`${API_URL}/signup/`, {username:username, password:password})
}

export const login = (username, password) => {
    return axios.post(`${API_URL}/login/`, {username:username, password:password}) //username and password is data payload
}
