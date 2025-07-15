import React from "react";

import { useState } from "react";
import CodeEditor from "./components/CodeEditor";
import OutputBox from "./components/OutputBox";
import LanguageSelector from "./components/LanguageSelector";
import RunButton from "./components/RunButton";

function App() {
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

export default App;
