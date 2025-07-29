import React from "react";
import Editor from "@monaco-editor/react";

const CodeEditor = ({ code, setCode, language = "javascript" }) => {
  return (
    <div style={{ height: "400px", border: "1px solid #ccc", marginTop: "1rem" }}>
      <Editor
        height="100%"
        language={language}
        theme="vs-dark"
        value={code}
        onChange={(value) => setCode(value)}
      />
    </div>
  );
};

export default CodeEditor;
