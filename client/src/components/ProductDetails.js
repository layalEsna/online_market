
import React, { useEffect, useState } from "react"
import { useFormik } from "formik"
import { useNavigate } from "react-router-dom"
import { useParams } from "react-router-dom"
import * as Yup from 'yup'
// import Cart from "./Cart"

function ProductDetails() {

    const [products, setProducts] = useState({
        name: '',
        description: '',
        image: '',
        price: ''
    })
    const [errorMessage, setErrorMessage] = useState('')
    const { product_id } = useParams()
    const navigate = useNavigate()


    // const loggedInUser = sessionStorage.getItem('username') || localStorage.getItem('username')
    // if (!loggedInUser) {
    //     console.log('User is not logged in')
    //     return
    // }

    useEffect(() => {
        console.log("Fetching product with ID:", product_id)
        fetch(`http://127.0.0.1:5555/products/${product_id}`)
        // fetch(`http://localhost:5555/products/${product_id}`)
            .then(res => {
                if (!res.ok) {
                    throw new Error(`Failed to fetch product with ID: ${product_id}`)
                }
                return res.json()
            })

            // .then(data => setProducts(data))
            .then(data => {
                console.log("Fetched product data:", data);
                setProducts(data);
            })

            .catch(e => console.error(`Internal error: ${e}`))
    }, [product_id])

    const formik = useFormik({
        initialValues: {
            quantity: 1,
            delivery_address: '',
            payment_method: ''
        },
        validationSchema: Yup.object({
            quantity: Yup.number()
                .required('Quantity is required.')
                .min(1, 'Quantity must be greater than 0.'),
            delivery_address: Yup.string()
                .required('Delivery address is required.')
                .max(255, 'Delivery address must be less than 255 characters.'),
            payment_method: Yup.string()
                .required('Payment method is required.')
                .max(50, 'Payment method must be less than 50 characters.')
        }),
        onSubmit: (values => {
            const loggedInUser = sessionStorage.getItem('username') || localStorage.getItem('username')
            if (!loggedInUser) {
                console.log('User is not logged in')
                setErrorMessage('You must be logged in to make a purchase.')
                return
            }
            fetch(`http://127.0.0.1:5555/products/${product_id}/purchase`, {
            // fetch("http://127.0.0.1:5555/products/4/purchase", {
                method: 'POST',
                credentials: 'include',
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                },

                body: JSON.stringify({})
                // body: JSON.stringify({ ...values, username: loggedInUser })
                // body: JSON.stringify({
                //     quantity: 1,
                //     delivery_address: "123 Main St",
                //     payment_method: "visa"
                // }),




            })
                .then(res => {
                    if (!res.ok) {
                        throw new Error('Failed to submit form')
                    }
                    return res.json()
                })
                .then(data => {
                    console.log(data)
                    navigate('/cart')
                }

                )

                .catch(e => console.log(`Internal error: ${e}`))
        })


    })



    return (
        <div>

            <h1>Product Details</h1>
            <form onSubmit={formik.handleSubmit}>
                <div>
                    <label htmlFor="quantity">Qty</label>
                    <select
                        id="quantity"
                        name="quantity"
                        value={formik.values.quantity}
                        onChange={formik.handleChange}
                        onBlur={formik.handleBlur}
                    >
                        <option value="1">1</option>
                        <option value="2">2</option>
                        <option value="3">3</option>
                        <option value="4">4</option>
                        <option value="5">5</option>
                        <option value="6">6</option>
                        <option value="7">7</option>
                        <option value="8">8</option>
                        <option value="9">9</option>
                        <option value="10">10</option>

                    </select>
                    {formik.errors.quantity && formik.touched.quantity && (
                        <div>{formik.errors.quantity}</div>
                    )}
                </div>
                <div>
                    <label htmlFor="delivery_address">delivery address</label>
                    <input
                        id="delivery_address"
                        name="delivery_address"
                        type="text"
                        value={formik.values.delivery_address}
                        onChange={formik.handleChange}
                        onBlur={formik.handleBlur}
                    />
                    {formik.errors.delivery_address && formik.touched.delivery_address && (
                        <div>{formik.errors.delivery_address}</div>
                    )}
                </div>
                <div>
                    <label htmlFor="payment_method">payment_method</label>
                    <select
                        id="payment_method"
                        name="payment_method"
                        value={formik.values.payment_method}
                        onChange={formik.handleChange}
                        onBlur={formik.handleBlur}
                    >
                        <option value="">select one</option>
                        <option value="visa">visa</option>
                        <option value="afterpay">afterpay</option>
                        <option value="pay_pal">pay_pal</option>

                    </select>
                    {formik.errors.payment_method && formik.touched.payment_method && (
                        <div>{formik.errors.payment_method}</div>
                    )}
                </div>
                <button type="submit">add to the list</button>

            </form>


        </div>
    )

}


export default ProductDetails