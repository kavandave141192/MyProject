import Form from "../components/Form"


function Login(){

    
         return <Form route="/api/token/" method="login"/>

// You're passing props to Form.
// So inside Form.jsx, you probably have something like:
// function Form({ route, method }) {
// Therefore:

// route = "/api/token/"
// method = "login"

// The Form component can then decide what it should do.
}

export default Login