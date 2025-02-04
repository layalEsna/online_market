import React, { useEffect, useState } from "react";
// import { Switch, Route } from "react-router-dom";
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Signup from "./Signup";

import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Signup from "./Signup";

function App() {
  return (
    <Router>
      <div>
        <h1>Project Client</h1>
        <main>
          <Routes>
            <Route path="/signup" element={<Signup />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;
