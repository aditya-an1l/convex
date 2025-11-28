import React, { useEffect, useMemo, useRef, useState } from "react";
import { useNavigate } from "react-router-dom";

/**
 * Neo-Holographic Aurora Home Page
 * - Unique holographic/aurora background
 * - Enhanced floating Indic & code characters with depth/parallax
 * - Glassy cards, subtle micro-interactions
 * - Accessibility minded (semantic tags, aria-labels)
 *
 * Drop-in replacement for existing Home.jsx
 */

const INDIC_CHARS = [
  "अ", "आ", "इ", "क", "ख", // Hindi
  "அ", "ஆ", "இ", "க", // Tamil
  "అ", "ఆ", "క", "ఖ", // Telugu
  "ಅ", "ಆ", "ಕ", "ಖ", // Kannada
  "if", "else", "for", "print", // Code tokens
];

const rand = (min, max) => Math.random() * (max - min) + min;

// --- LOGO COMPONENT ---
// 💡 PASTE YOUR SVG CODE INSIDE THIS COMPONENT
const ConvexLogo = () => (
  <svg
    width="100%"
    height="100%"
    viewBox="0 0 600 500"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
    aria-hidden="true"
  >
    {/* --- REPLACE CONTENT BELOW WITH YOUR SVG --- */}
    <g transform="translate(200, 0)">
      <path
        d="M100,0 
         A100,250 0 1,1 100,500 
         A100,250 0 1,1 100,0 
         Z 
         M135,25 
         A60,225 0 1,1 135,475 
         A60,225 0 1,1 135,25 
         Z"
        fill="url(#logo-g)"
        fillRule="evenodd"
      />
    </g>
    <text x="180" y="160" className="char-style" textAnchor="end">अ</text>
    <text x="180" y="240" className="char-style" textAnchor="end">𑐲</text>
    <text x="180" y="320" className="char-style" textAnchor="end">α</text>
    <text x="180" y="400" className="char-style" textAnchor="end">Γ</text>

    <text x="420" y="145" className="binary-style" textAnchor="start">1 1 0</text>
    <text x="420" y="215" className="binary-style" textAnchor="start">1 0 1</text>
    <text x="420" y="285" className="binary-style" textAnchor="start">0 1 0</text>
    <text x="420" y="355" className="binary-style" textAnchor="start">0 0 1</text>
    <text x="420" y="425" className="binary-style" textAnchor="start">1 0 1</text>
    {/* Gradient Definition */}
    <defs>
      <linearGradient id="logo-g" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stopColor="#ffd36b" />
        <stop offset="50%" stopColor="#ff7aa2" />
        <stop offset="100%" stopColor="#9b8cff" />
      </linearGradient>
      <style
        dangerouslySetInnerHTML={{
          __html: `
      .char-style {
        font-family: serif; 
        font-size: 65px; 
        fill: #fdfdfdff; 
        font-weight: bold;
      }
      .binary-style {
        font-family: "Courier New", monospace; 
        font-size: 55px; 
        fill: #fcfcfcff; 
        font-weight: bold;
        letter-spacing: 5px;
      }
    `,
        }}
      />
    </defs>
    {/* --- END REPLACEMENT --- */}
  </svg>
);

const FloatingChar = ({ char, idx, seed }) => {
  // Randomized params but stable per component via seed+idx
  const left = `${(seed * 100 * (idx + 1)) % 100}%`;
  const size = `${Math.round((seed * 20 * (idx + 1)) % 30 + 18)}px`;
  const duration = `${(seed * 18 + idx) % 22 + 18}s`;
  const delay = `${(seed * 7 + idx) % 10}s`;
  const hue = Math.round((seed * 360 + idx * 37) % 360);

  // INCREASED VISIBILITY: Bumped base opacity from 0.08 to 0.4 range
  const opacity = 0.4 + ((seed * 7 + idx) % 4) * 0.1;

  const style = {
    position: "absolute",
    left,
    top: "110%",
    fontSize: size,
    color: `hsl(${hue}deg 85% 70% / ${opacity})`,
    transform: `translateY(0) rotate(${(idx % 2 === 0) ? -8 : 8}deg)`,
    animation: `floatUp ${duration} linear infinite`,
    animationDelay: delay,
    textShadow: `0 4px 20px hsla(${hue}deg, 85%, 60%, 0.4)`,
    pointerEvents: "none",
    willChange: "transform, opacity",
    filter: "drop-shadow(0 6px 30px rgba(0,0,0,0.25))",
  };

  return <div aria-hidden style={style}>{char}</div>;
};

const Home = () => {
  const navigate = useNavigate();
  const [scrolled, setScrolled] = useState(false);
  const [mouse, setMouse] = useState({ x: 0, y: 0 });
  const floatingCount = 18;
  const heroRef = useRef(null);

  // Stabilize characters using useMemo
  const floatingChars = useMemo(() => {
    const baseSeed = Math.random();
    return Array.from({ length: floatingCount }).map((_, i) => ({
      char: INDIC_CHARS[Math.floor(rand(0, INDIC_CHARS.length))],
      idx: i,
      seed: baseSeed * (i + 1),
    }));
  }, []);

  // Navbar scroll effect
  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 48);
    window.addEventListener("scroll", onScroll, { passive: true });
    return () => window.removeEventListener("scroll", onScroll);
  }, []);

  // Mouse parallax
  useEffect(() => {
    const onMouse = (e) => {
      const x = (e.clientX / window.innerWidth - 0.5) * 2; // -1..1
      const y = (e.clientY / window.innerHeight - 0.5) * 2;
      setMouse({ x, y });
    };
    window.addEventListener("mousemove", onMouse);
    return () => window.removeEventListener("mousemove", onMouse);
  }, []);

  // keyboard accessibility
  useEffect(() => {
    const handler = (e) => {
      if (e.key === "Enter" && document.activeElement === heroRef.current) {
        navigate("/ide");
      }
    };
    window.addEventListener("keydown", handler);
    return () => window.removeEventListener("keydown", handler);
  }, [navigate]);

  const base = {
    fontFamily: '"Inter", ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial',
    minHeight: "100vh",
    color: "#e6eef8",
    position: "relative",
    overflowX: "hidden",
    backgroundColor: "#030317",
    WebkitFontSmoothing: "antialiased",
    MozOsxFontSmoothing: "grayscale",
  };

  return (
    <div style={base} role="document">
      <style>
        {`
        /* ---------- Keyframes ---------- */
        @keyframes floatUp {
          0% { transform: translateY(0) rotate(0deg); opacity: 0; }
          10% { opacity: 0.7; }
          60% { opacity: 0.5; }
          100% { transform: translateY(-120vh) rotate(22deg); opacity: 0; }
        }
        @keyframes auroraShift {
          0% { filter: hue-rotate(0deg) saturate(100%); opacity: 0.95; }
          50% { filter: hue-rotate(25deg) saturate(120%); opacity: 1; }
          100% { filter: hue-rotate(0deg) saturate(100%); opacity: 0.95; }
        }

        /* ---------- Utility classes ---------- */
        .container {
          max-width: 1240px; /* Slightly wider for modern feel */
          margin: 0 auto;
          padding: 0 2rem;
        }

        /* ---------- Backgrounds ---------- */
        .bg-layer {
          position: fixed;
          inset: 0;
          z-index: 0;
          pointer-events: none;
        }
        .bg-noise {
          position: absolute;
          inset: 0;
          background-image: radial-gradient(rgba(255,255,255,0.02) 1px, transparent 1px);
          background-size: 32px 32px;
          opacity: 0.06;
          mix-blend-mode: overlay;
        }
        .bg-aurora {
          position: absolute;
          left: 50%;
          top: 20%;
          width: 1300px;
          height: 500px;
          transform: translateX(-50%) rotate(-6deg);
          background: linear-gradient(120deg, rgba(34,211,238,0.12), rgba(168,85,247,0.12), rgba(255,127,80,0.1));
          filter: blur(80px) contrast(120%);
          opacity: 0.9;
          animation: auroraShift 14s ease-in-out infinite;
          border-radius: 30%;
        }
        .bg-aurora-2 {
          position: absolute;
          left: 12%;
          top: 50%;
          width: 900px;
          height: 420px;
          transform: translateY(-20%) rotate(10deg);
          background: linear-gradient(90deg, rgba(255,100,150,0.06), rgba(20,184,166,0.06));
          filter: blur(90px);
          opacity: 0.85;
          animation: auroraShift 22s ease-in-out infinite;
          border-radius: 40%;
        }
        .bg-grid {
          position: absolute;
          inset: 0;
          background-image: linear-gradient(90deg, rgba(255,255,255,0.02) 1px, transparent 1px),
                            linear-gradient(180deg, rgba(255,255,255,0.02) 1px, transparent 1px);
          background-size: 200px 200px;
          mix-blend-mode: overlay;
          opacity: 0.03;
        }

        /* ---------- Glass Card ---------- */
        .glass-card {
          background: linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01));
          border: 1px solid rgba(255,255,255,0.06);
          backdrop-filter: blur(10px) saturate(120%);
          box-shadow: 0 8px 30px rgba(2,6,23,0.6);
          transition: transform 300ms cubic-bezier(.2,.9,.2,1), box-shadow 300ms;
        }
        .glass-card:hover { transform: translateY(-8px); box-shadow: 0 28px 60px rgba(2,6,23,0.75); }

        /* ---------- Enhanced Navbar ---------- */
        header.site-header {
          position: fixed;
          inset-inline: 0;
          top: 0;
          z-index: 60;
          display: flex;
          justify-content: center;
          align-items: center;
          height: 80px; /* Taller navbar */
          transition: all 300ms cubic-bezier(0.4, 0, 0.2, 1);
          border-bottom: 1px solid transparent;
        }
        .site-header-inner {
          width: 100%;
          display: flex;
          align-items: center;
          justify-content: space-between;
        }
        
        /* Logo Section */
        .nav-left { 
          display: flex; 
          align-items: center; 
          gap: 1.2rem; 
          cursor: pointer;
          user-select: none;
        }
        .logo-mark {
          width: 44px; 
          height: 44px; 
          display: flex; 
          align-items: center; 
          justify-content: center;
          /* Removed simple border/bg to allow custom SVG logo to shine */
          filter: drop-shadow(0 0 8px rgba(155, 140, 255, 0.3));
        }

        /* Navigation Links */
        .nav-links { display: flex; gap: 2rem; align-items: center; color: #c6d2e6; }
        .nav-link-item { 
          position: relative;
          text-decoration: none; 
          color: inherit; 
          font-weight: 500; 
          font-size: 0.95rem; 
          opacity: 0.85; 
          transition: opacity 200ms; 
          padding: 0.5rem 0;
        }
        .nav-link-item:hover { opacity: 1; color: #fff; }
        .nav-link-item::after {
          content: '';
          position: absolute;
          bottom: 0;
          left: 0;
          width: 0%;
          height: 2px;
          background: linear-gradient(90deg, #ffd36b, #ff7aa2);
          transition: width 250ms ease;
        }
        .nav-link-item:hover::after { width: 100%; }

        /* CTA Button */
        .nav-cta {
          padding: 12px 24px;
          border-radius: 12px;
          border: 1px solid rgba(255,255,255,0.1);
          background: rgba(255,255,255,0.03);
          color: #fff;
          cursor: pointer;
          font-weight: 600;
          font-size: 0.9rem;
          transition: all 200ms ease;
          backdrop-filter: blur(4px);
        }
        .nav-cta:hover { 
          transform: translateY(-2px); 
          background: rgba(255,255,255,0.08);
          box-shadow: 0 0 20px rgba(155, 140, 255, 0.2);
          border-color: rgba(155, 140, 255, 0.3);
        }

        /* Scrolled State */
        header.site-header.scrolled {
          background: rgba(3, 3, 23, 0.75);
          backdrop-filter: blur(16px) saturate(180%);
          border-bottom: 1px solid rgba(255,255,255,0.05);
          height: 72px; /* Shrinks slightly on scroll */
        }
        header.site-header.scrolled .logo-mark {
          transform: scale(0.9); /* Subtle logo shrink */
          transition: transform 300ms;
        }

        /* ---------- Hero ---------- */
        .hero { padding: 12rem 0 6rem; text-align: center; position: relative; z-index: 10; }
        .badge {
          display: inline-flex; gap: 0.6rem; align-items: center;
          padding: 0.45rem 0.9rem; border-radius: 999px;
          font-weight: 700; font-size: 0.9rem; letter-spacing: 0.2px;
          background: linear-gradient(90deg, rgba(249,115,22,0.07), rgba(168,85,247,0.04));
          border: 1px solid rgba(249,115,22,0.06);
          color: #ffd8b8;
        }
        h1.hero-title {
          margin: 1.4rem 0 1rem;
          font-size: clamp(2.6rem, 6.2vw, 4.8rem);
          line-height: 1.02;
          font-weight: 800;
          color: #f8fbff;
          letter-spacing: -1px;
        }
        .title-accent {
          background: linear-gradient(90deg, #ffd36b, #ff7aa2, #9b8cff);
          -webkit-background-clip: text;
          -webkit-text-fill-color: transparent;
        }
        .hero-sub {
          color: #a7b6d3; font-size: 1.08rem; max-width: 720px; margin: 0 auto 2.4rem; line-height: 1.7;
        }
        .hero-cta-group { display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap; margin-top: 1.2rem; }
        
        /* ---------- Grid & Footer ---------- */
        .grid { display: grid; gap: 1.6rem; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); }
        .feature-idx {
          position: absolute; font-size: 6.5rem; font-weight: 900;
          color: rgba(255,255,255,0.03); right: 16px; top: -12px; pointer-events: none;
        }
        footer.site-footer { margin-top: 6rem; padding: 3.6rem 0; color: #6f7f95; border-top: 1px solid rgba(255,255,255,0.03); }

        @media (max-width: 720px) {
          .nav-links { display: none; }
          .hero { padding-top: 9.5rem; }
        }
      `}
      </style>

      {/* ---------- Background visual layers ---------- */}
      <div className="bg-layer" aria-hidden>
        <div className="bg-aurora" style={{ transform: `translateX(${mouse.x * -10}px) translateY(${mouse.y * -8}px) rotate(-6deg)` }} />
        <div className="bg-aurora-2" style={{ transform: `translateX(${mouse.x * 14}px) translateY(${mouse.y * 10}px) rotate(10deg)` }} />
        <div className="bg-grid" />
        <div className="bg-noise" />
      </div>

      {/* ---------- Floating characters ---------- */}
      <div style={{ position: "fixed", inset: 0, zIndex: 5, pointerEvents: "none" }} aria-hidden>
        {floatingChars.map((item) => (
          <FloatingChar key={item.idx} char={item.char} idx={item.idx} seed={item.seed} />
        ))}
      </div>

      {/* ---------------- Header / Nav ---------------- */}
      <header className={`site-header ${scrolled ? "scrolled" : ""}`} role="banner">
        <div className="site-header-inner container">
          <div className="nav-left" onClick={() => navigate("/")} role="button" tabIndex={0}>
            {/* Logo Section */}
            <div className="logo-mark">
               <ConvexLogo />
            </div>
            
            {/* Logo Text */}
            <div style={{ display: "flex", flexDirection: "column", lineHeight: 1 }}>
              <span style={{
                fontWeight: 800,
                fontSize: "1.25rem",
                letterSpacing: "-0.5px",
                color: "#fff"
              }}>Convex</span>
              <small style={{ color: "#90a0bd", fontSize: "0.75rem", fontWeight: 500 }}>Native language IDE</small>
            </div>
          </div>

          <nav style={{ display: "flex", alignItems: "center", gap: "2.5rem" }} aria-label="Primary">
            <div className="nav-links" role="list">
              <a className="nav-link-item" href="#features" onClick={(e) => { e.preventDefault(); document.querySelector("#features")?.scrollIntoView({ behavior: "smooth" }); }}>Features</a>
              <a className="nav-link-item" href="#how" onClick={(e) => { e.preventDefault(); document.querySelector("#how")?.scrollIntoView({ behavior: "smooth" }); }}>How it works</a>
            </div>
            <button className="nav-cta" onClick={() => navigate("/ide")}>
              Launch IDE
            </button>
          </nav>
        </div>
      </header>

      {/* ---------------- Hero ---------------- */}
      <main>
        <section className="hero" aria-labelledby="hero-heading" ref={heroRef}>
          <div className="container">
            <div style={{ display: "inline-flex", justifyContent: "center", width: "100%" }}>
              {/* <div className="badge" aria-hidden>
                <span style={{ width: 8, height: 8, borderRadius: 999, background: "linear-gradient(90deg,#ffd36b,#ff7aa2)" }} />
                Now supporting Hindi, Tamil, Telugu & Kannada
              </div> */}
            </div>

            <h1 id="hero-heading" className="hero-title">
              Code in the language <br />
              <span className="title-accent">you already think with.</span>
            </h1>

            <p className="hero-sub">
              Write logic in your native words and let Convex parse, compile and run it instantly.
              A holographic, browser-first IDE that speaks your language — fast, safe and delightful.
            </p>

            <div className="hero-cta-group">
              <button
                onClick={() => navigate("/ide")}
                style={{
                  padding: "14px 32px",
                  borderRadius: 14,
                  border: "none",
                  background: "linear-gradient(90deg,#ffd36b,#ff7aa2,#9b8cff)",
                  fontWeight: 800,
                  cursor: "pointer",
                  boxShadow: "0 18px 50px rgba(155,140,255,0.14)",
                  color: "#071423",
                  fontSize: "1.04rem",
                  transition: "transform 0.2s"
                }}
                onMouseEnter={(e) => e.target.style.transform = "translateY(-2px)"}
                onMouseLeave={(e) => e.target.style.transform = "translateY(0)"}
              >
                Start Coding Now
              </button>

              <button
                onClick={() => document.querySelector("#how")?.scrollIntoView({ behavior: "smooth" })}
                style={{
                  padding: "12px 26px",
                  borderRadius: 12,
                  border: "1px solid rgba(255,255,255,0.06)",
                  background: "transparent",
                  color: "#c9dbf3",
                  fontWeight: 700,
                  cursor: "pointer",
                  fontSize: "1.03rem"
                }}
              >
                View Documentation
              </button>
            </div>
          </div>
        </section>

        {/* ---------- How it works ---------- */}
        <section id="how" style={{ padding: "4.5rem 0" }}>
          <div className="container">
            <h2 style={{ textAlign: "center", fontSize: "2.2rem", color: "#f8fbff", marginBottom: "2.2rem", fontWeight: 800 }}>
              How Convex Works
            </h2>
            <div className="grid">
              {[
                { step: "01", title: "Write Native Keywords", desc: "Type logic using your natural language keywords — no awkward translation step." },
                { step: "02", title: "Smart Parse & Map", desc: "Language packs convert native tokens to safe Python/JS AST using deterministic rules." },
                { step: "03", title: "Secure Execution", desc: "We run code in sandboxed containers and return outputs with logs & visuals." }
              ].map((card, i) => (
                <article key={i} className="glass-card" style={{ padding: 28, borderRadius: 18, position: "relative" }}>
                  <div className="feature-idx">{card.step}</div>
                  <h3 style={{ margin: "0 0 0.6rem 0", color: "#ffd6a8", fontSize: "1.15rem" }}>{card.title}</h3>
                  <p style={{ margin: 0, color: "#a9bbd8", lineHeight: 1.6 }}>{card.desc}</p>
                </article>
              ))}
            </div>
          </div>
        </section>

        {/* ---------- Features ---------- */}
        <section id="features" style={{ padding: "3.5rem 0 6rem" }}>
          <div className="container">
            <h2 style={{ fontSize: "2.1rem", fontWeight: 800, color: "#f8fbff", marginBottom: "1.6rem" }}>Features</h2>
            <div className="grid">
              {[
                { icon: "🌏", title: "Universal Syntax", desc: "Same logic, native keywords. Faster learning curve for new programmers." },
                { icon: "⚡", title: "Zero Setup", desc: "Browser-first execution—no local Python installs or environments needed." },
                { icon: "🔒", title: "Secure Sandbox", desc: "Isolated execution with resource constraints and audit logs." },
                { icon: "🧩", title: "Extensible Packs", desc: "Add new languages by authoring small JSON/AST mapping packs." },
              ].map((f, i) => (
                <div key={i} className="glass-card" style={{ padding: 24, borderRadius: 16 }}>
                  <div style={{ fontSize: 28, marginBottom: 12 }}>{f.icon}</div>
                  <h4 style={{ margin: "0 0 8px 0", color: "#f1f7ff" }}>{f.title}</h4>
                  <p style={{ margin: 0, color: "#9fb0d1" }}>{f.desc}</p>
                </div>
              ))}
            </div>
          </div>
        </section>

        {/* ---------- Footer ---------- */}
        <footer className="site-footer" role="contentinfo">
          <div className="container" style={{ textAlign: "center" }}>
            <p style={{ margin: 0, fontSize: "0.98rem" }}>
              &copy; {new Date().getFullYear()} Convex Project • <span style={{ color: "#9fb0d1" }}>Built for India 🇮🇳</span>
            </p>
            <p style={{ marginTop: 10, color: "#7f94b0", fontSize: "0.92rem" }}>
              Made with care — Neo-Holographic Aurora theme.
            </p>
          </div>
        </footer>
      </main>
    </div>
  );
};

export default Home;