import React from 'react';
import { useNavigate } from 'react-router-dom';

const Home = () => {
  const navigate = useNavigate();

  const cardStyle = {
    background: '#fff',
    padding: '1.5rem',
    borderRadius: '12px',
    boxShadow: '0 4px 6px rgba(0,0,0,0.1)',
    transition: 'transform 0.2s ease',
    cursor: 'pointer',
  };

  return (
    <div style={{ fontFamily: 'Inter, system-ui, sans-serif', background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)', minHeight: '100vh' }}>
      <header style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '1rem 2rem', background: 'rgba(17, 24, 39, 0.95)', backdropFilter: 'blur(10px)', color: '#fff' }}>
        <div style={{ display: 'flex', alignItems: 'center', cursor: 'pointer' }} onClick={() => navigate('/')}>
          <div style={{ width: '40px', height: '40px', background: 'linear-gradient(45deg, #2563eb, #7c3aed)', borderRadius: '8px', display: 'flex', alignItems: 'center', justifyContent: 'center', marginRight: '0.5rem', fontSize: '20px' }}>
            🗺️
          </div>
          <h2 style={{ margin: 0, fontWeight: '700' }}>Convex IDE</h2>
        </div>
        <nav style={{ display: 'flex', gap: '1rem' }}>
          <button style={{ padding: '0.5rem 1rem', color: '#e5e7eb', background: 'none', border: '1px solid transparent', borderRadius: '6px', fontWeight: '500', cursor: 'pointer', transition: 'all 0.2s' }} 
                  onMouseEnter={(e) => { e.target.style.background = 'rgba(255,255,255,0.1)'; e.target.style.borderColor = 'rgba(255,255,255,0.2)'; }}
                  onMouseLeave={(e) => { e.target.style.background = 'none'; e.target.style.borderColor = 'transparent'; }}>
            Features
          </button>
          <button style={{ padding: '0.5rem 1rem', color: '#e5e7eb', background: 'none', border: '1px solid transparent', borderRadius: '6px', fontWeight: '500', cursor: 'pointer', transition: 'all 0.2s' }}
                  onMouseEnter={(e) => { e.target.style.background = 'rgba(255,255,255,0.1)'; e.target.style.borderColor = 'rgba(255,255,255,0.2)'; }}
                  onMouseLeave={(e) => { e.target.style.background = 'none'; e.target.style.borderColor = 'transparent'; }}>
            Architecture
          </button>
          <button style={{ padding: '0.5rem 1.5rem', background: 'linear-gradient(45deg, #2563eb, #7c3aed)', color: '#fff', borderRadius: '6px', fontWeight: '600', border: 'none', cursor: 'pointer', transition: 'transform 0.2s' }}
                  onMouseEnter={(e) => e.target.style.transform = 'translateY(-1px)'}
                  onMouseLeave={(e) => e.target.style.transform = 'translateY(0)'}
                  onClick={() => navigate('/ide')}>
            Go to IDE
          </button>
        </nav>
      </header>

      <section style={{ position: 'relative', textAlign: 'center', padding: '6rem 2rem', background: 'rgba(0,0,0,0.3)', backdropFilter: 'blur(5px)' }}>
        <div style={{ position: 'relative', zIndex: 1, color: '#fff', maxWidth: '900px', margin: '0 auto' }}>
          <h1 style={{ fontSize: '3.5rem', marginBottom: '1.5rem', fontWeight: '800', background: 'linear-gradient(45deg, #fff, #e0e7ff)', WebkitBackgroundClip: 'text', WebkitTextFillColor: 'transparent', backgroundClip: 'text' }}>
            🗺️ Write Code in Your Own Language
          </h1>
          <p style={{ fontSize: '1.3rem', marginBottom: '3rem', opacity: '0.9', lineHeight: '1.6' }}>
            Convex allows you to write programming logic using your native language, then seamlessly translates it into executable code like Python or Java.
          </p>
          <button style={{ padding: '1rem 2rem', background: 'linear-gradient(45deg, #2563eb, #7c3aed)', color: '#fff', borderRadius: '12px', fontWeight: '600', border: 'none', cursor: 'pointer', fontSize: '1.1rem', boxShadow: '0 8px 25px rgba(37, 99, 235, 0.3)', transition: 'all 0.3s' }}
                  onMouseEnter={(e) => { e.target.style.transform = 'translateY(-2px)'; e.target.style.boxShadow = '0 12px 35px rgba(37, 99, 235, 0.4)'; }}
                  onMouseLeave={(e) => { e.target.style.transform = 'translateY(0)'; e.target.style.boxShadow = '0 8px 25px rgba(37, 99, 235, 0.3)'; }}
                  onClick={() => navigate('/ide')}>
            Start Coding Now
          </button>
        </div>
      </section>

      <section style={{ padding: '4rem 2rem', maxWidth: '1200px', margin: '0 auto' }}>
        <h2 style={{ fontSize: '2.5rem', marginBottom: '1rem', color: '#fff', textAlign: 'center', fontWeight: '700' }}>✅ Core Features</h2>
        <p style={{ marginBottom: '3rem', textAlign: 'center', color: '#e0e7ff', fontSize: '1.1rem' }}>
          Let users write <strong>code in their native language</strong>, and translate it into real code (Python, Java, etc.) that can be executed.
        </p>
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', gap: '2rem' }}>
          <div style={{...cardStyle, background: 'rgba(255,255,255,0.95)', backdropFilter: 'blur(10px)'}}
               onMouseEnter={(e) => e.target.style.transform = 'translateY(-5px)'}
               onMouseLeave={(e) => e.target.style.transform = 'translateY(0)'}>
            <div style={{ fontSize: '2rem', marginBottom: '1rem' }}>🧠</div>
            <h3 style={{ color: '#1f2937', marginBottom: '1rem' }}>Native Syntax</h3>
            <p style={{ color: '#4b5563', lineHeight: '1.6' }}>
              Define keywords in languages like Hindi, Tamil, Kannada, etc. Mapping words like <code style={{ background: '#f3f4f6', padding: '2px 6px', borderRadius: '4px' }}>यदि</code> → <code style={{ background: '#f3f4f6', padding: '2px 6px', borderRadius: '4px' }}>if</code>
            </p>
          </div>
          <div style={{...cardStyle, background: 'rgba(255,255,255,0.95)', backdropFilter: 'blur(10px)'}}
               onMouseEnter={(e) => e.target.style.transform = 'translateY(-5px)'}
               onMouseLeave={(e) => e.target.style.transform = 'translateY(0)'}>
            <div style={{ fontSize: '2rem', marginBottom: '1rem' }}>🔧</div>
            <h3 style={{ color: '#1f2937', marginBottom: '1rem' }}>Smart Translator</h3>
            <p style={{ color: '#4b5563', lineHeight: '1.6' }}>
              Advanced rule-based translator using dictionaries and NLP to convert native-language code into valid Python or Java.
            </p>
          </div>
          <div style={{...cardStyle, background: 'rgba(255,255,255,0.95)', backdropFilter: 'blur(10px)'}}
               onMouseEnter={(e) => e.target.style.transform = 'translateY(-5px)'}
               onMouseLeave={(e) => e.target.style.transform = 'translateY(0)'}>
            <div style={{ fontSize: '2rem', marginBottom: '1rem' }}>⚙️</div>
            <h3 style={{ color: '#1f2937', marginBottom: '1rem' }}>Safe Executor</h3>
            <p style={{ color: '#4b5563', lineHeight: '1.6' }}>
              Safely run the translated code with built-in security measures and error handling for Python and Java execution.
            </p>
          </div>
          <div style={{...cardStyle, background: 'rgba(255,255,255,0.95)', backdropFilter: 'blur(10px)'}}
               onMouseEnter={(e) => e.target.style.transform = 'translateY(-5px)'}
               onMouseLeave={(e) => e.target.style.transform = 'translateY(0)'}>
            <div style={{ fontSize: '2rem', marginBottom: '1rem' }}>🖥️</div>
            <h3 style={{ color: '#1f2937', marginBottom: '1rem' }}>Web Interface</h3>
            <p style={{ color: '#4b5563', lineHeight: '1.6' }}>
              Modern online editor with syntax highlighting, translation preview, and real-time execution results.
            </p>
          </div>
        </div>
      </section>

      <footer style={{ textAlign: 'center', padding: '2rem', background: 'rgba(17, 24, 39, 0.95)', backdropFilter: 'blur(10px)', color: '#9ca3af', marginTop: '4rem' }}>
        <p>&copy; 2025 Convex IDE • <a href="#" style={{ color: '#60a5fa', textDecoration: 'none' }}>Apache License 2.0</a></p>
      </footer>
    </div>
  );
};

export default Home;
