export default function YouTubeEmbed({ url, title, onClose }) {
  const videoId = extractVideoId(url);
  if (!videoId) {
    return <div className="embed-error">Invalid video URL</div>;
  }

  return (
    <div className="youtube-embed">
      <div className="embed-header">
        <span className="embed-title">{title}</span>
        <button className="embed-close" onClick={onClose}>✕</button>
      </div>
      <div className="embed-player">
        <iframe
          src={`https://www.youtube.com/embed/${videoId}?autoplay=1&rel=0`}
          title={title}
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
          referrerPolicy="strict-origin-when-cross-origin"
          allowFullScreen
        />
      </div>
    </div>
  );
}

function extractVideoId(url) {
  if (!url) return null;
  const patterns = [
    /(?:youtube\.com\/watch\?v=|youtu\.be\/|youtube\.com\/embed\/)([a-zA-Z0-9_-]{11})/,
    /^([a-zA-Z0-9_-]{11})$/,
  ];
  for (const pattern of patterns) {
    const match = url.match(pattern);
    if (match) return match[1];
  }
  return null;
}
