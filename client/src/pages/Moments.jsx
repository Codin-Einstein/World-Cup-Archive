import { useState, useEffect } from 'react';
import YouTubeEmbed from '../components/YouTubeEmbed';

export default function Moments() {
  const [moments, setMoments] = useState([]);
  const [category, setCategory] = useState('');
  const [playing, setPlaying] = useState(null);

  const categories = ['iconic', 'legend', 'classic', 'drama', 'historic'];

  useEffect(() => {
    const params = category ? `?category=${category}` : '';
    fetch(`/api/moments${params}`)
      .then(r => r.json())
      .then(setMoments);
  }, [category]);

  return (
    <div className="page">
      <h1>World Cup Moments</h1>
      <p className="subtitle">Relive the most iconic moments in World Cup history</p>

      <div className="filters">
        <button
          className={`btn btn-sm ${category === '' ? 'btn-primary' : 'btn-outline'}`}
          onClick={() => setCategory('')}
        >
          All
        </button>
        {categories.map(c => (
          <button
            key={c}
            className={`btn btn-sm ${category === c ? 'btn-primary' : 'btn-outline'}`}
            onClick={() => setCategory(c)}
          >
            {c.charAt(0).toUpperCase() + c.slice(1)}
          </button>
        ))}
      </div>

      <div className="moments-grid">
        {moments.map(mom => (
          <div key={mom.id} className="moment-card-wrapper">
            <div
              className="moment-card"
              onClick={() => setPlaying(playing === mom.id ? null : mom.id)}
            >
              <div className="moment-play">▶</div>
              <div className="moment-info">
                <div className="moment-meta">
                  <span className="moment-year">{mom.tournament_year}</span>
                  <span className="moment-category">{mom.category}</span>
                </div>
                <h3>{mom.title}</h3>
                <p>{mom.description}</p>
                <span className="moment-match">{mom.team1_name} vs {mom.team2_name}</span>
              </div>
            </div>
            {playing === mom.id && (
              <YouTubeEmbed url={mom.video_url} title={mom.title} onClose={() => setPlaying(null)} />
            )}
          </div>
        ))}
      </div>
    </div>
  );
}
