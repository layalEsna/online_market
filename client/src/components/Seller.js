
import React, { useEffect, useState } from "react"
import { useNavigate } from "react-router-dom"

function Seller() {

    const [sellers, setSellers] = useState([])
    const navigate = useNavigate()
    const [error, setError] = useState(null)
    
    useEffect(() => {
        fetch('http://127.0.0.1:5555/sellers')
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
            <h1>Market Viwe</h1>
            console.log("Seller component rendered")
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
                    />
                    <p>{product.description}</p>
                    <p>price: ${product.price}</p> 
                            </div>
                        ))
                    ):( <p>No product available</p>)}
                    
                    <button onClick={()=> navigate(`/sellers/${seller.id}`)}>buy</button>
                </div>
            ))}
            
        </div>
    )
}

export default Seller