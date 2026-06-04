import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';

export default function Tournaments() {
  const [tournaments, setTournaments] = useState([]);

  useEffect(() => {
    fetch('/api/tournaments')
      .then(r => r.json())
      .then(setTournaments);
  }, []);

  return (
    <div className="page">
      <h1>World Cup Tournaments</h1>
      <p className="subtitle">All 22 editions from 1930 to 2022</p>
      <div className="tournament-grid">
        {tournaments.map(t => (
          <Link to={`/tournaments/${t.id}`} key={t.id} className="tournament-card">
            <div className="tournament-year">{t.year}</div>
            <div className="tournament-host">{t.host}</div>
            <div className="tournament-winner">
              <span className="trophy">🏆</span> {t.winner}
            </div>
            <div className="tournament-stats">
              <span>{t.total_matches} matches</span>
              <span>{t.total_goals} goals</span>
            </div>
          </Link>
        ))}
      </div>
    </div>
  );
}
