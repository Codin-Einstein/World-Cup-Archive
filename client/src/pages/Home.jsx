import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';

export default function Home() {
  const [stats, setStats] = useState(null);
  const [recentMatches, setRecentMatches] = useState([]);

  useEffect(() => {
    fetch('/api/stats')
      .then(r => r.json())
      .then(setStats);

    fetch('/api/matches')
      .then(r => r.json())
      .then(data => setRecentMatches(data.slice(0, 5)));
  }, []);

  return (
    <div className="page">
      <section className="hero">
        <h1>The World Cup Archive</h1>
        <p>Every match. Every moment. Every trophy. Explore the complete history of the FIFA World Cup.</p>
        <div className="hero-actions">
          <Link to="/tournaments" className="btn btn-primary">Browse Tournaments</Link>
          <Link to="/moments" className="btn btn-secondary">Watch Moments</Link>
        </div>
      </section>

      {stats && (
        <section className="stats-grid">
          <div className="stat-card">
            <span className="stat-number">{stats.count}</span>
            <span className="stat-label">Tournaments</span>
          </div>
          <div className="stat-card">
            <span className="stat-number">{stats.total || 0}</span>
            <span className="stat-label">Total Matches</span>
          </div>
          <div className="stat-card">
            <span className="stat-number">{stats.total_goals || 0}</span>
            <span className="stat-label">Total Goals</span>
          </div>
          <div className="stat-card">
            <span className="stat-number">{stats.teams || 0}</span>
            <span className="stat-label">Teams</span>
          </div>
        </section>
      )}

      {stats && stats.mostTitles && (
        <section>
          <h2>Most Successful Nations</h2>
          <div className="titles-list">
            {stats.mostTitles.map((t, i) => (
              <div key={t.winner} className="title-row">
                <span className="title-rank">{i + 1}</span>
                <span className="title-nation">{t.winner}</span>
                <span className="title-count">{t.titles} {t.titles === 1 ? 'title' : 'titles'}</span>
              </div>
            ))}
          </div>
        </section>
      )}

      {recentMatches.length > 0 && (
        <section>
          <h2>Recent Matches</h2>
          <div className="matches-list">
            {recentMatches.map(m => (
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
        </section>
      )}
    </div>
  );
}
