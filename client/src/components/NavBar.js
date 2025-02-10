
import { Link, useNavigate } from "react-router-dom"


function NavBar() {
    
    const navigate = useNavigate()
    function handleLogout() {
        fetch('http://127.0.0.1:5555/logout', {
            method: 'DELETE',
            credentials: 'include'
        })
            .then(res => {
                if (!res.ok) {
                throw new Error('Logout failed.')
                }
                return res.json()
            })
            .then(data => {
                console.log(data.message)
                navigate('/login')
            })
            .catch(e => {
            console.error(`Error during logout: ${e}`)
        })
    }
    

    return (
      
            <nav>
                
            
            <Link className='nav' to='/sellers'>Market View</Link>
            
            <Link className='nav' to='/cart'>Cart</Link>
            <button className='btn' onClick={handleLogout}>logout</button>
       

            </nav>
           
            
)

}

export default NavBar