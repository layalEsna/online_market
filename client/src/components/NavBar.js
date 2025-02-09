
import { Link } from "react-router-dom"

function NavBar() {
    
    return (
        <nav>
            {/* <Link to='/signup'></Link>
            <Link to='/login'></Link> */}
            <Link to='/sellers'>Market View</Link>
            
            <Link to='/cart'>Cart</Link>
       </nav>
)

}

export default NavBar