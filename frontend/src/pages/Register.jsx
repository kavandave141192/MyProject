import Form from "../components/Form"



function Register(){

    return <Form route="/api/user/register" method="register"/>

// Register.jsx
//       ↓
// Form.jsx
//       ↓
// POST /api/user/register
//       ↓
// Django
//       ↓
// CreateUserView
//       ↓
// UserSerializer
//       ↓
// User database
}
export default Register