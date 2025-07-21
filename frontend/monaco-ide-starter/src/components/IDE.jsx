import React from "react";
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { useState } from "react";
import CodeEditor from "./CodeEditor";
import OutputBox from "./OutputBox";
import LanguageSelector from "./LanguageSelector";
import RunButton from "./RunButton";

const IDE = () =>{
  const [code, setCode] = useState("// Start coding...");
  const [output, setOutput] = useState("");
  const [language, setLanguage] = useState("javascript");

  const handleRun = () => {
    setOutput("Running... (connect backend here)");
  };

  return (
    <div style={{ padding: "1rem" }}>
      <h1>Online IDE</h1>
      <LanguageSelector language={language} setLanguage={setLanguage} />
      <CodeEditor code={code} setCode={setCode} language={language} />
      <RunButton onClick={handleRun} />
      <OutputBox output={output} />
    </div>
  );
}

export default IDE;
