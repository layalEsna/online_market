
import React, { useState } from 'react'
import { useFormik } from 'formik'
import { useNavigate } from 'react-router-dom'
import * as Yup from 'yup'


function Signup() {

    const navigate = useNavigate()

    const passwordPattern = /^(?=.*[A-Z])(?=.*[a-z])(?=.*[!@#$%^&*]).{8,}$/

    const formik = useFormik({
        initialValues: {
            username: '',
            password: '',
            confirm_password: ''
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
            confirm_password: Yup.string()
                .required('Confirm_password is required.')
                .oneOf([Yup.ref('password'), null], 'Password must match.')

        }),
        onSubmit: (values => {
        
        })
    })

    return (
        <div>

        </div>
    )
}

export default Signup
