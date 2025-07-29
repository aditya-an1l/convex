import React from "react";
const OutputBox = ({ output }) => {
  return (
    <div style={{ marginTop: "1rem", background: "#f0f0f0", padding: "1rem" }}>
      <h3>Output:</h3>
      <pre>{output}</pre>
    </div>
  );
};

export default OutputBox;
