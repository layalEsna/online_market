import React from "react";

import { BrowserRouter as Router, Route, Routes, useBeforeUnload } from 'react-router-dom';
import Signup from "./Signup";
import Login from "./Login";
import Seller from "./Seller";
import ProductDetails from "./ProductDetails";
import Cart from "./Cart";
import NavBar from "./NavBar"
import React, { useState, useEffect } from "react";
// import Logout from "./Logout";

function App() {
  const [user, setUser] = useState(null)

  useEffect(() => {
    fetch('/check_session')
      .then(res => {
        if (!res.ok) {
        throw new Error('Failed to fetch user ID.')
        }
        return res.json()
      })
      .then(user => setUser(user))
    .catch(e => console.error(e))
  }, [])

  return (
    <Router>
      <div>
        <NavBar/>
        <main>
          <Routes>
            <Route path="/signup" element={<Signup />} />
            <Route path="/login" element={<Login />} />
            <Route path="/sellers" element={<Seller />} />
            <Route path="/products/:product_id" element={<ProductDetails />} />
            <Route path="/cart" element={<Cart />} />
            {/* <Route path="/logout" element={<Logout />} /> */}
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;
