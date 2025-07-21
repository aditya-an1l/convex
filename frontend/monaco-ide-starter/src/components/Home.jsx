import React from 'react';
import { useNavigate } from 'react-router-dom';

const Home = () => {
  const navigate = useNavigate();

  return (
    <div style={{ padding: "1rem" }}>
      <h1>Welcome to My Online IDE App</h1>
      <p>Click below to start coding.</p>
      <button onClick={() => navigate("/ide")}>Go to IDE</button>
    </div>
  );
};

export default Home;