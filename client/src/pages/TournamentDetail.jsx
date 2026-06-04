import { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';

export default function TournamentDetail() {
  const { id } = useParams();
  const [tournament, setTournament] = useState(null);

  useEffect(() => {
    fetch(`/api/tournaments/${id}`)
      .then(r => r.json())
      .then(setTournament);
  }, [id]);

  if (!tournament) return <div className="page"><p>Loading...</p></div>;

  return (
    <div className="page">
      <Link to="/tournaments" className="back-link">← Back to Tournaments</Link>
      <div className="tournament-header">
        <h1>{tournament.year} World Cup</h1>
        <p className="host">Hosted by: <strong>{tournament.host}</strong></p>
      </div>

      <div className="podium">
        <div className="podium-item gold">
          <span className="podium-medal">🥇</span>
          <span className="podium-label">Winner</span>
          <span className="podium-team">{tournament.winner}</span>
        </div>
        <div className="podium-item silver">
          <span className="podium-medal">🥈</span>
          <span className="podium-label">Runner-up</span>
          <span className="podium-team">{tournament.runner_up}</span>
        </div>
        <div className="podium-item bronze">
          <span className="podium-medal">🥉</span>
          <span className="podium-label">Third Place</span>
          <span className="podium-team">{tournament.third_place}</span>
        </div>
      </div>

      <div className="tournament-stats-bar">
        <div><strong>{tournament.total_matches}</strong> Matches</div>
        <div><strong>{tournament.total_goals}</strong> Goals</div>
        <div><strong>{(tournament.attendance || 0).toLocaleString()}</strong> Attendance</div>
      </div>

      <h2>Matches</h2>
      <div className="matches-list">
        {tournament.matches?.map(m => (
          <Link to={`/matches/${m.id}`} key={m.id} className="match-card">
            <div className="match-info">
              <span className="match-stage">{m.stage}</span>
              <span className="match-date">{m.date}</span>
            </div>
            <div className="match-teams">
              <span className={m.team1_name === m.winner_name ? 'winner' : ''}>{m.team1_name}</span>
              <span className="match-score">{m.score_team1} - {m.score_team2}</span>
              <span className={m.team2_name === m.winner_name ? 'winner' : ''}>{m.team2_name}</span>
            </div>
            {m.venue && <div className="match-venue">{m.venue}, {m.city}</div>}
          </Link>
        ))}
      </div>
    </div>
  );
}
