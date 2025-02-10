
import React, { useEffect, useState } from "react"
import { useNavigate } from "react-router-dom"


function Seller() {

    const [sellers, setSellers] = useState([])
    const navigate = useNavigate()
    const [error, setError] = useState(null)
    const [username, setUsername] = useState(null)
    
    useEffect(() => {
        const loggedInUser = sessionStorage.getItem('username') || localStorage.getItem('username');
        
        if (loggedInUser) {
            setUsername(loggedInUser)
        }
        fetch('http://localhost:5555/sellers')
            .then(res => {
                if (!res.ok) {
                    throw new Error(`Failed to fetch data: ${res.status} ${res.statusText}`)
                }
                return res.json()
            })
            .then(data => {
                console.log(data)
                setSellers(data.sellers)
            })
            .catch(e => {console.error(e)
            setError(e.message)}
        )
    }, [])

    return (
        <div>
            
            
            <h1>Market View</h1>
            {username && <p>Welcome, {username}!</p>}
            
            {sellers.map(seller => (
                <div key={seller.id}>
                    <h3>{seller.username}</h3>  
                    {seller.products.length > 0 ? (
                        seller.products.map(product => (
                            <div key={product.id}>
                                <p>{product.name}</p>
                    <img
                                    src={product.image}
                                    alt={product.name}
                                    style={{ width: '150px', height: '150px', objectFit: 'cover' }}
                    />
                    <p>{product.description}</p>
                                <p>price: ${product.price}</p> 
                                <button className='btn' onClick={()=> navigate(`/products/${product.id}`)}>buy</button>
                                {/* <button onClick={()=> navigate(`/sellers/${seller.id}`)}>buy</button> */}

                            </div>
                        ))
                    ):( <p>No product available</p>)}
                    
                    {/* <button onClick={()=> navigate(`/products/${product.id}`)}>buy</button> */}
                </div>
            ))}
            
        </div>
    )
}

export default Seller