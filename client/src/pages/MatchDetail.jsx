import { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import YouTubeEmbed from '../components/YouTubeEmbed';

export default function MatchDetail() {
  const { id } = useParams();
  const [match, setMatch] = useState(null);
  const [playingId, setPlayingId] = useState(null);

  useEffect(() => {
    fetch(`/api/matches/${id}`)
      .then(r => r.json())
      .then(setMatch);
  }, [id]);

  if (!match) return <div className="page"><p>Loading...</p></div>;

  return (
    <div className="page">
      <Link to="/matches" className="back-link">← Back to Matches</Link>

      <div className="match-header">
        <span className="match-badge">{match.tournament_year} World Cup · {match.stage}</span>
        <span className="match-date-large">{match.date}</span>
      </div>

      <div className="match-hero">
        <div className={`match-team-box ${match.team1_name === match.winner_name ? 'is-winner' : ''}`}>
          <span className="team-flag">{getFlag(match.team1_name)}</span>
          <span className="team-name-large">{match.team1_name}</span>
          {match.team1_name === match.winner_name && <span className="winner-badge">Winner</span>}
        </div>
        <div className="match-score-display">
          <span className="score-big">{match.score_team1}</span>
          <span className="score-sep">:</span>
          <span className="score-big">{match.score_team2}</span>
          {match.score_team1 === match.score_team2 && (
            <span className="penalty-note">(went to penalties)</span>
          )}
        </div>
        <div className={`match-team-box ${match.team2_name === match.winner_name ? 'is-winner' : ''}`}>
          <span className="team-flag">{getFlag(match.team2_name)}</span>
          <span className="team-name-large">{match.team2_name}</span>
          {match.team2_name === match.winner_name && <span className="winner-badge">Winner</span>}
        </div>
      </div>

      {match.venue && (
        <div className="match-venue-box">
          <span>📍 {match.venue}, {match.city}</span>
          {match.attendance && <span>👥 {match.attendance.toLocaleString()} attendance</span>}
        </div>
      )}

      {match.moments && match.moments.length > 0 && (
        <section>
          <h2>Watch Moments</h2>
          <div className="moments-grid">
            {match.moments.map(mom => (
              <div key={mom.id} className="moment-card-wrapper">
                <div
                  className="moment-card"
                  onClick={() => setPlayingId(playingId === mom.id ? null : mom.id)}
                >
                  <div className="moment-play">▶</div>
                  <div className="moment-info">
                    <h3>{mom.title}</h3>
                    <p>{mom.description}</p>
                    <span className="moment-category">{mom.category}</span>
                  </div>
                </div>
                {playingId === mom.id && (
                  <YouTubeEmbed url={mom.video_url} title={mom.title} onClose={() => setPlayingId(null)} />
                )}
              </div>
            ))}
          </div>
        </section>
      )}
    </div>
  );
}

const flags = {
  Brazil: '🇧🇷', Argentina: '🇦🇷', Uruguay: '🇺🇾', Italy: '🇮🇹', Germany: '🇩🇪',
  France: '🇫🇷', England: '🏴󠁧󠁢󠁥󠁮󠁧󠁿', Spain: '🇪🇸', Netherlands: '🇳🇱', 'West Germany': '🇩🇪',
  Portugal: '🇵🇹', Croatia: '🇭🇷', Sweden: '🇸🇪', Hungary: '🇭🇺', Czechoslovakia: '🇨🇿',
  Austria: '🇦🇹', Switzerland: '🇨🇭', 'Soviet Union': '🇷🇺', Poland: '🇵🇱', Turkey: '🇹🇷',
  Yugoslavia: '🇷🇸', Chile: '🇨🇱', Belgium: '🇧🇪', 'United States': '🇺🇸', 'South Korea': '🇰🇷',
  Japan: '🇯🇵', Morocco: '🇲🇦', Senegal: '🇸🇳', Colombia: '🇨🇴', Denmark: '🇩🇰',
  Mexico: '🇲🇽', Paraguay: '🇵🇾', Cameroon: '🇨🇲', Nigeria: '🇳🇬', Ghana: '🇬🇭',
  'Costa Rica': '🇨🇷', 'Saudi Arabia': '🇸🇦', Iran: '🇮🇷', Australia: '🇦🇺',
  Romania: '🇷🇴', Bulgaria: '🇧🇬', Scotland: '🏴󠁧󠁢󠁳󠁣󠁴󠁿', 'Northern Ireland': '🇬🇧',
  Wales: '🏴󠁧󠁢󠁷󠁬󠁳󠁿', Algeria: '🇩🇿', 'Ivory Coast': '🇨🇮', Tunisia: '🇹🇳',
  Egypt: '🇪🇬', Ecuador: '🇪🇨', Peru: '🇵🇪', Honduras: '🇭🇳', 'New Zealand': '🇳🇿',
  Iraq: '🇮🇶', Kuwait: '🇰🇼', Canada: '🇨🇦', Cuba: '🇨🇺', 'Dutch East Indies': '🇮🇩',
  Norway: '🇳🇴', Ireland: '🇮🇪', Slovakia: '🇸🇰', Slovenia: '🇸🇮', Bosnia: '🇧🇦',
  Ukraine: '🇺🇦', Serbia: '🇷🇸', 'Czech Republic': '🇨🇿', Russia: '🇷🇺', Panama: '🇵🇦',
  Iceland: '🇮🇸', Qatar: '🇶🇦', 'Serbia and Montenegro': '🇷🇸', Zaire: '🇨🇩',
  Haiti: '🇭🇹', 'East Germany': '🇩🇪', 'El Salvador': '🇸🇻', Zambia: '🇿🇲',
  Indonesia: '🇮🇩', 'United Arab Emirates': '🇦🇪', Jamaica: '🇯🇲', 'South Africa': '🇿🇦',
  China: '🇨🇳', Togo: '🇹🇬', 'Trinidad and Tobago': '🇹🇹', Angola: '🇦🇴',
};

function getFlag(teamName) {
  return flags[teamName] || '🏳️';
}
