import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';

export default function Teams() {
  const [teams, setTeams] = useState([]);
  const [search, setSearch] = useState('');

  useEffect(() => {
    fetch('/api/teams')
      .then(r => r.json())
      .then(setTeams);
  }, []);

  const filtered = teams.filter(t =>
    t.name.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <div className="page">
      <h1>World Cup Teams</h1>
      <input
        type="text"
        placeholder="Search teams..."
        value={search}
        onChange={e => setSearch(e.target.value)}
        className="search-input"
      />
      <div className="teams-grid">
        {filtered.map(t => (
          <Link to={`/teams/${t.id}`} key={t.id} className="team-card">
            <span className="team-card-name">{t.name}</span>
            <span className="team-card-code">{t.country_code}</span>
          </Link>
        ))}
      </div>
    </div>
  );
}
