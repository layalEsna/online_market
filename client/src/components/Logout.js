
// import { useNavigate } from "react-router-dom"

// function Logout() {
//     const navigate = useNavigate()

//     function handleLogout() {
//         fetch('http://127.0.0.1:5555/logout', {
//             method: 'DELETE',
//         })
//             .then(res => {
//                 if (res.ok) {
//                 navigate('/login')
//                 } else {
//                     console.error('Logout failed.')
//             }
//             })
//             .catch(e => {
//             console.error(`Error during logout: ${e}`)
//         })
//     }
    
//     return (
//         <div>
//             <button onClick={handleLogout}>logout</button>
//         </div>
//     )
// }

// export default Logout