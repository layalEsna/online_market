import React from "react";

import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Signup from "./Signup";
import Login from "./Login";
import Seller from "./Seller";
import ProductDetails from "./ProductDetails";
import Cart from "./Cart";
import NavBar from "./NavBar"
import Logout from "./Logout";

function App() {
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
            <Route path="/logout" element={<Logout />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;
