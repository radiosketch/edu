import axios from "axios"

const getAPI = axios.create({
	// Where the django rest api resides
	baseURL: "http://localhost:8000/api",
	timeout: 1000,
})

export {
	getAPI,
	axios
}