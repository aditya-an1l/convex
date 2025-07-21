import React from "react";
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from "./components/Home";
import IDE from "./components/IDE";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/ide" element={<IDE />} />
      </Routes>
    </Router>
  );
}

export default App;
