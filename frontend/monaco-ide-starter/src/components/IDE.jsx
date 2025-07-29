import React, { useState } from "react";
import { useNavigate } from 'react-router-dom';
import CodeEditor from "./CodeEditor";
import OutputBox from "./OutputBox";
import LanguageSelector from "./LanguageSelector";
import RunButton from "./RunButton";

const IDE = () => {
  const navigate = useNavigate();
  
  const [code, setCode] = useState("// Start coding...");
  const [output, setOutput] = useState("");
  const [language, setLanguage] = useState("javascript");

  const handleRun = () => {
    setOutput("Running... (connect backend here)\n\nCode executed successfully!\nLanguage: " + language);
  };

  return (
    <div style={{ 
      fontFamily: 'Inter, system-ui, sans-serif', 
      background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)', 
      minHeight: '100vh',
      color: '#e2e8f0'
    }}>
      {/* Header - matching Home page style */}
      <header style={{ 
        display: 'flex', 
        justifyContent: 'space-between', 
        alignItems: 'center', 
        padding: '1rem 2rem', 
        background: 'rgba(17, 24, 39, 0.95)', 
        backdropFilter: 'blur(10px)',
        color: '#fff'
      }}>
        <div style={{ display: 'flex', alignItems: 'center', cursor: 'pointer' }} onClick={() => navigate('/')}>
          <div style={{ 
            width: '40px', 
            height: '40px', 
            background: 'linear-gradient(45deg, #2563eb, #7c3aed)', 
            borderRadius: '8px', 
            display: 'flex', 
            alignItems: 'center', 
            justifyContent: 'center', 
            marginRight: '0.5rem',
            fontSize: '20px'
          }}>
            🗺️
          </div>
          <h2 style={{ margin: 0, fontWeight: '700' }}>Convex IDE</h2>
        </div>
        
        <div style={{ display: 'flex', alignItems: 'center', gap: '1rem' }}>
          <button 
            onClick={() => navigate('/')}
            style={{
              padding: '0.5rem 1rem',
              color: '#e5e7eb',
              background: 'none',
              border: '1px solid transparent',
              borderRadius: '6px',
              fontWeight: '500',
              cursor: 'pointer',
              transition: 'all 0.2s'
            }}
            onMouseEnter={(e) => { 
              e.target.style.background = 'rgba(255,255,255,0.1)'; 
              e.target.style.borderColor = 'rgba(255,255,255,0.2)'; 
            }}
            onMouseLeave={(e) => { 
              e.target.style.background = 'none'; 
              e.target.style.borderColor = 'transparent'; 
            }}
          >
            🏠 Back to Home
          </button>
        </div>
      </header>

      {/* Main IDE Content */}
      <div style={{ 
        padding: '2rem', 
        maxWidth: '1200px', 
        margin: '0 auto'
      }}>
        <div style={{ 
          background: 'rgba(255, 255, 255, 0.95)', 
          borderRadius: '12px', 
          padding: '2rem',
          backdropFilter: 'blur(10px)',
          boxShadow: '0 8px 32px rgba(0,0,0,0.1)',
          color: '#1f2937'
        }}>
          <h1 style={{ 
            fontSize: '2.5rem', 
            marginBottom: '2rem', 
            color: '#1f2937',
            textAlign: 'center',
            fontWeight: '700'
          }}>
            🖥️ Online IDE
          </h1>
          
          <LanguageSelector language={language} setLanguage={setLanguage} />
          <CodeEditor code={code} setCode={setCode} language={language} />
          <RunButton onClick={handleRun} />
          <OutputBox output={output} />
        </div>
      </div>

      {/* Footer - matching Home page style */}
      <footer style={{ 
        textAlign: 'center', 
        padding: '2rem', 
        background: 'rgba(17, 24, 39, 0.95)', 
        backdropFilter: 'blur(10px)', 
        color: '#9ca3af', 
        marginTop: '2rem' 
      }}>
        <p>&copy; 2025 Convex IDE • <a href="#" style={{ color: '#60a5fa', textDecoration: 'none' }}>Apache License 2.0</a></p>
      </footer>
    </div>
  );
};

export default IDE;
