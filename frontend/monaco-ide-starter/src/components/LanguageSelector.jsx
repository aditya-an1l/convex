import React from "react";
const LanguageSelector = ({ language, setLanguage }) => {
  return (
    <div style={{ marginBottom: "1rem" }}>
      <label>Select Language: </label>
      <select value={language} onChange={(e) => setLanguage(e.target.value)}>
        <option value="javascript">JavaScript</option>
        <option value="python">Python</option>
        <option value="cpp">C++</option>
      </select>
    </div>
  );
};

export default LanguageSelector;
