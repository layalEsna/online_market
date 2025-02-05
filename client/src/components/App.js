import React from "react";

import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Signup from "./Signup";
import Login from "./Login";
import Seller from "./Seller";
import ProductDetails from "./ProductDetails";

function App() {
  return (
    <Router>
      <div>
        <h1>Project Client</h1>
        <main>
          <Routes>
            <Route path="/signup" element={<Signup />} />
            <Route path="/login" element={<Login />} />
            <Route path="/sellers" element={<Seller />} />
            <Route path="/products/:product_id" element={<ProductDetails />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;
