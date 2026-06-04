import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';

export default function Matches() {
  const [matches, setMatches] = useState([]);
  const [teams, setTeams] = useState([]);
  const [filterTeam, setFilterTeam] = useState('');
  const [filterYear, setFilterYear] = useState('');
  const [filterStage, setFilterStage] = useState('');

  useEffect(() => {
    fetch('/api/teams').then(r => r.json()).then(setTeams);

    const params = new URLSearchParams();
    if (filterTeam) params.set('team', filterTeam);
    if (filterYear) params.set('year', filterYear);
    if (filterStage) params.set('stage', filterStage);

    fetch(`/api/matches?${params}`)
      .then(r => r.json())
      .then(setMatches);
  }, [filterTeam, filterYear, filterStage]);

  const stages = ['Group Stage', 'Round of 16', 'Quarter-final', 'Semi-final', 'Final', 'Final Round', 'Second Round'];

  return (
    <div className="page">
      <h1>All Matches</h1>

      <div className="filters">
        <select value={filterTeam} onChange={e => setFilterTeam(e.target.value)}>
          <option value="">All Teams</option>
          {teams.map(t => <option key={t.id} value={t.name}>{t.name}</option>)}
        </select>
        <select value={filterYear} onChange={e => setFilterYear(e.target.value)}>
          <option value="">All Years</option>
          {[2022, 2018, 2014, 2010, 2006, 2002, 1998, 1994, 1990, 1986, 1982, 1978, 1974, 1970, 1966, 1962, 1958, 1954, 1950, 1938, 1934, 1930].map(y => (
            <option key={y} value={y}>{y}</option>
          ))}
        </select>
        <select value={filterStage} onChange={e => setFilterStage(e.target.value)}>
          <option value="">All Stages</option>
          {stages.map(s => <option key={s} value={s}>{s}</option>)}
        </select>
      </div>

      <div className="matches-list">
        {matches.map(m => (
          <Link to={`/matches/${m.id}`} key={m.id} className="match-card">
            <div className="match-info">
              <span className="match-stage">{m.stage}</span>
              <span className="match-year">{m.tournament_year}</span>
              <span className="match-date">{m.date}</span>
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
