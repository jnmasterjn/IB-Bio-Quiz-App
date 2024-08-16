//Trivia/client/react-frontend/src/api.services/api.jsx

import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000/'
 
export const signup = (username, password) => {
    return axios.post(`${API_URL}/signup`, {username, password})
}

export const login = (username, password) => {
    return axios.post(`${API_URL}/login`, {username, password})
}

