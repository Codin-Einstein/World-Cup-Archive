import { Link, useLocation } from 'react-router-dom';

export default function Navbar() {
  const { pathname } = useLocation();

  const links = [
    { to: '/', label: 'Home' },
    { to: '/tournaments', label: 'Tournaments' },
    { to: '/matches', label: 'Matches' },
    { to: '/moments', label: 'Moments' },
    { to: '/teams', label: 'Teams' },
  ];

  return (
    <nav className="navbar">
      <Link to="/" className="nav-brand">
        <span className="nav-logo">🏆</span>
        <span className="nav-title">World Cup Archive</span>
      </Link>
      <div className="nav-links">
        {links.map(l => (
          <Link
            key={l.to}
            to={l.to}
            className={`nav-link ${pathname === l.to ? 'active' : ''}`}
          >
            {l.label}
          </Link>
        ))}
      </div>
    </nav>
  );
}
