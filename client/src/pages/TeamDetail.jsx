import { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';

export default function TeamDetail() {
  const { id } = useParams();
  const [team, setTeam] = useState(null);

  useEffect(() => {
    fetch(`/api/teams/${id}`)
      .then(r => r.json())
      .then(setTeam);
  }, [id]);

  if (!team) return <div className="page"><p>Loading...</p></div>;

  const wins = team.matches?.filter(m => m.winner_name === team.name).length || 0;
  const losses = team.matches?.filter(m => m.winner_name && m.winner_name !== team.name).length || 0;

  return (
    <div className="page">
      <Link to="/teams" className="back-link">← Back to Teams</Link>

      <div className="team-header">
        <h1>{team.name}</h1>
        <span className="team-code">{team.country_code}</span>
      </div>

      <div className="stats-grid">
        <div className="stat-card">
          <span className="stat-number">{team.titles}</span>
          <span className="stat-label">World Titles</span>
        </div>
        <div className="stat-card">
          <span className="stat-number">{team.runner_up}</span>
          <span className="stat-label">Runner-up</span>
        </div>
        <div className="stat-card">
          <span className="stat-number">{wins}</span>
          <span className="stat-label">Match Wins</span>
        </div>
        <div className="stat-card">
          <span className="stat-number">{team.matches?.length || 0}</span>
          <span className="stat-label">Total Matches</span>
        </div>
      </div>

      <h2>Matches</h2>
      <div className="matches-list">
        {team.matches?.map(m => (
          <Link to={`/matches/${m.id}`} key={m.id} className="match-card">
            <div className="match-info">
              <span className="match-stage">{m.stage}</span>
              <span className="match-year">{m.tournament_year}</span>
            </div>
            <div className="match-teams">
              <span className={m.team1_name === m.winner_name ? 'winner' : ''}>{m.team1_name}</span>
              <span className="match-score">{m.score_team1} - {m.score_team2}</span>
              <span className={m.team2_name === m.winner_name ? 'winner' : ''}>{m.team2_name}</span>
            </div>
          </Link>
        ))}
      </div>
    </div>
  );
}
