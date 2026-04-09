import { useState } from "react";

const API_BASE = import.meta.env.VITE_API_URL ?? "http://localhost:8000";

/** Edit this list to add or change preset prompts shown in the UI. */
const PROMPT_TEMPLATES = [
  { label: "Box", text: "Create a box 40mm wide, 30mm deep, 20mm tall." },
  { label: "Cylinder", text: "Create a cylinder with radius 15mm and height 40mm." },
  { label: "Hole pattern", text: "Create a plate 80mm by 50mm by 5mm with four M4 holes in the corners, 10mm from each edge." },
  { label: "Sphere", text: "Create a sphere with radius 25mm." },
];

export default function App() {
  const [prompt, setPrompt] = useState(PROMPT_TEMPLATES[0].text);
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState(null);
  const [error, setError] = useState(null);

  const handleGenerate = async () => {
    setLoading(true);
    setMessage(null);
    setError(null);

    try {
      const response = await fetch(`${API_BASE}/cad`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ prompt }),
      });

      const contentType = response.headers.get("content-type") ?? "";

      if (contentType.includes("application/json")) {
        const data = await response.json();
        if (data.error) {
          setError(data.error);
          if (data.generated_code) {
            console.warn("Generated code:", data.generated_code);
          }
          return;
        }
      }

      if (!response.ok) {
        throw new Error(`Request failed (${response.status})`);
      }

      const blob = await response.blob();
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = "model.zip";
      document.body.appendChild(a);
      a.click();
      a.remove();
      window.URL.revokeObjectURL(url);
      setMessage("Model generated — download started.");
    } catch (err) {
      console.error(err);
      setError(err instanceof Error ? err.message : "Failed to generate model");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div
      style={{
        maxWidth: 560,
        margin: "0 auto",
        padding: "48px 24px",
      }}
    >
      <h1
      style={{
        fontWeight: 700,
        fontSize: "2rem",
        marginBottom: 6,
        background: "linear-gradient(90deg,#58a6ff,#3fb950)",
        WebkitBackgroundClip: "text",
        color: "transparent",
        
      }}
      >
      CAD Generator
      </h1>
      <p style={{ color: "#8b949e", marginTop: 0, marginBottom: 24 }}>
        Describe a shape; the server builds CadQuery code and returns a STEP
        archive as <code>model.zip</code>.
      </p>

      <label
        htmlFor="prompt"
        style={{ display: "block", fontSize: "0.875rem", marginBottom: 8 }}
      >
        Prompt
      </label>

      <div style={{ marginBottom: 12 }}>
        <span
          style={{
            display: "block",
            fontSize: "0.75rem",
            color: "#8b949e",
            marginBottom: 8,
            textTransform: "uppercase",
            letterSpacing: "0.04em",
          }}
        >
          Templates
        </span>
        <div
          style={{
            display: "flex",
            flexWrap: "wrap",
            gap: 8,
          }}
        >
          {PROMPT_TEMPLATES.map((t) => (
            <button
              key={t.label}
              type="button"
              disabled={loading}
              onClick={() => setPrompt(t.text)}
              style={{
                padding: "6px 12px",
                borderRadius: 999,
                border: "1px solid #30363d",
                background: "#21262d",
                color: "#f3ebe6",
                fontSize: "0.8125rem",
                cursor: loading ? "not-allowed" : "pointer",
              }}
            >
              {t.label}
            </button>
          ))}
        </div>
      </div>

      <textarea
        id="prompt"
        rows={4}
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
        disabled={loading}
        placeholder="Describe the part you want…"
        style={{
          width: "100%",
          padding: "12px 14px",
          borderRadius: 8,
          border: "1px solid #30363d",
          background: "#161b22",
          color: "#e6edf3",
          fontSize: "1rem",
          marginBottom: 16,
          resize: "vertical",
          fontFamily: "inherit",
          lineHeight: 1.45,
        }}
      />

      <button
        type="button"
        onClick={handleGenerate}
        disabled={loading}
        style={{
          padding: "12px 20px",
          borderRadius: 8,
          border: "none",
          background: loading ? "#238636aa" : "#238636",
          color: "#fff",
          fontWeight: 600,
          cursor: loading ? "not-allowed" : "pointer",
          fontSize: "1rem",
        }}
      >
        {loading ? "Generating…" : "Generate"}
      </button>

      {message && (
        <p style={{ color: "#3fb950", marginTop: 20, marginBottom: 0 }}>{message}</p>
      )}
      {error && (
        <p style={{ color: "#f85149", marginTop: 20, marginBottom: 0 }} role="alert">
          {error}
        </p>
      )}
    </div>
  );
}
