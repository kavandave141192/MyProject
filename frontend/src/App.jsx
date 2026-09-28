import react from "react"
import {BrowserRouter,Routes,Route,Navigate} from "react-router-dom"
import Login from "./pages/Login"
import Register from "./pages/Register"
import Notfound from "./pages/Notfound"
import Home from "./pages/Home"
import ProtectedRoute from "./components/ProtectedRoute"
// import { REFRESH_TOKEN } from "./constants"

function Logout(){
  localStorage.clear()
    return <Navigate to="/login"/>  
}
function RegisterAndLogout(){
  localStorage.clear()
  return <Register/>
}

function App() {
  return (      
    <BrowserRouter>
        <Routes>
          <Route path="/" element={<ProtectedRoute><Home/></ProtectedRoute>}></Route>
          <Route path="/login" element={<Login/>}></Route>
          <Route path="/logout" element={<Logout/>}></Route>
          <Route path="/register" element={<Register/>}></Route>
          <Route path="*" element={<Notfound/>}></Route>
          
        </Routes>
    </BrowserRouter>
  )
}

export default App
