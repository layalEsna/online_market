import React from "react";

import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Signup from "./Signup";
import Login from "./Login";
import Seller from "./Seller";

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
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;
