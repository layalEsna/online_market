import React from "react";

import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Signup from "./Signup";
import Login from "./Login";

function App() {
  return (
    <Router>
      <div>
        <h1>Project Client</h1>
        <main>
          <Routes>
            <Route path="/signup" element={<Signup />} />
            <Route path="/login" element={<Login />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;
