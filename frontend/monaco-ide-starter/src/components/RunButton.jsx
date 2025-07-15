import React from "react";
const RunButton = ({ onClick }) => {
  return (
    <button onClick={onClick} style={{ marginTop: "1rem" }}>
      Run Code
    </button>
  );
};

export default RunButton;
