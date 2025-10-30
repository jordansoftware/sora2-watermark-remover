import React, { useState } from "react";

export default function App() {
  const [video, setVideo] = useState(null);
  const [resultUrl, setResultUrl] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleUpload = (e) => setVideo(e.target.files[0]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!video) return alert("Choisis une vidéo d'abord !");
    setLoading(true);
    const formData = new FormData();
    formData.append("file", video);

    const res = await fetch("http://localhost:8000/process_video", {
      method: "POST",
      body: formData
    });

    const blob = await res.blob();
    setResultUrl(URL.createObjectURL(blob));
    setLoading(false);
  };

  return (
    <div className="p-10 text-center">
      <h1 className="text-3xl font-bold mb-6">🎬 Watermark Remover (Python + React)</h1>

      <form onSubmit={handleSubmit}>
        <input type="file" accept="video/*" onChange={handleUpload} className="mb-4" />
        <br />
        <button
          type="submit"
          className="bg-blue-600 text-white px-6 py-2 rounded"
          disabled={loading}
        >
          {loading ? "Traitement..." : "Envoyer la vidéo"}
        </button>
      </form>

      {resultUrl && (
        <div className="mt-6">
          <h2 className="text-xl mb-2">Résultat :</h2>
          <video controls src={resultUrl} className="mx-auto w-2/3 rounded" />
        </div>
      )}
    </div>
  );
}
