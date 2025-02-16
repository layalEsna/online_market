

import React, { useState } from 'react'
import { useFormik } from 'formik'
import { useNavigate } from 'react-router-dom'
import * as Yup from 'yup'

// Login failed.
function Login() {

    const [errorMessage, setErrorMessage] = useState('')

    const navigate = useNavigate()

    const passwordPattern = /^(?=.*[A-Z])(?=.*[a-z])(?=.*[!@#$%^&*]).{8,}$/

    const formik = useFormik({
        initialValues: {
            username: '',
            password: ''

        },
        validationSchema: Yup.object({
            username: Yup.string()
                .required('Username is required.')
                .min(5, 'Username must be at least 5 characters.')
                .max(50, 'Username must be less than 50 characters.'),
            password: Yup.string()
                .required('Password is required.')
                .min(8, 'Password must be at least 8 characters.')
                .matches(passwordPattern, 'Password must be at least 8 characters long and include at least 1 lowercase letter, 1 uppercase letter, and 1 special character (!@#$%^&*).'),

        }),
        onSubmit: (values => {
            console.log("Submitting login request with values:", values);

            // fetch('http://127.0.0.1:5555/login', {
            fetch('http://localhost:5555/login', {
                credentials: 'include',
                method: 'POST',
                // credentials: 'include',
                headers: {
                    'Content-Type': 'application/json'
                },
                // credentials: 'include', 
                body: JSON.stringify(values)

            })
                .then(res => res.json())


                .then((data) => {
                    if (!data.message || data.message !== 'Successful login!') {
                        // throw new Error(data.error || "Login failed.")
                        throw new Error('User not found')
                    }
                    sessionStorage.setItem('username', values.username)
                    localStorage.setItem('username', values.username)
                    navigate('/sellers')
                })
                .catch(e => {
                    setErrorMessage(e.message)
                    // console.error(`Internal error: ${e.message}`)
                })

        })
    })

    return (
        <div>
            <h1>Login</h1>

            <form onSubmit={formik.handleSubmit}>
                <div>
                    <label htmlFor='username'>user name:</label>
                    <input
                        id='username'
                        type='text'
                        name='username'
                        value={formik.values.username}
                        onChange={formik.handleChange}
                        onBlur={formik.handleBlur}
                    />
                    {formik.errors.username && formik.touched.username && (
                        <div>{formik.errors.username}</div>
                    )}
                </div>
                <div>
                    <label htmlFor='password'>password:</label>
                    <input
                        id='password'
                        type='password'
                        name='password'
                        value={formik.values.password}
                        onChange={formik.handleChange}
                        onBlur={formik.handleBlur}
                    />
                    {formik.errors.password && formik.touched.password && (
                        <div>{formik.errors.password}</div>
                    )}
                </div>

                <div>
                    <button className='btn' type='submit'>login</button>
                </div>

            </form>
            {errorMessage && <div>{errorMessage}</div>}

        </div>
    )
}

export default Login
