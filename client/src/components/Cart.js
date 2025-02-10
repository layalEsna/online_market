
import React, { useState, useEffect } from "react"
import { useNavigate } from "react-router-dom"

function Cart() {

    const [info, setInfo] = useState({ cart: [] })
    // { cart: [] }
    const navigate = useNavigate()

    useEffect(() => {
        fetch('http://localhost:5555/products/purchases')
            .then(res => {
                if (!res.ok) {
                    throw new Error('Failed to fetch data.')
                }
                return res.json()
            })
            .then(data => {
                setInfo(data)
            })
            .catch(e => console.error(e))
    }, [])

    function handleCheckout() {
        navigate('/purchase-confirmation')
    }

    return (
        <div>
            <h3>Your Cart</h3>

            {info.cart.length > 0 ? (
                info.cart.map(purchase => (
                    <div key={purchase.id}>

                        <p>{purchase.product.name}</p>
                        <img src={purchase.product.image} alt={purchase.product.name}
                            style={{ width: '150px', height: '150px', objectFit: 'cover' }}
                        />
                        <p>{purchase.product.description}</p>
                        <p>{purchase.product.price}</p>

                        <p>Qty: {purchase.quantity}</p>
                        <p>total price: ${purchase.product.price * purchase.quantity}</p>
                        <p>Delivery Address: {purchase.delivery_address}</p>
                        <p>Payment Method: {purchase.payment_method}</p>

                    </div>
                ))
            ): (<p>Your cart is empty.</p>)}
            <button className='btn' type="button" onClick={handleCheckout}>Checkout</button>
        </div>
    )



}

export default Cart