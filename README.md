# World Cup Archive

A full-stack web app for exploring FIFA World Cup history — tournaments, matches, teams, and iconic moments with embedded YouTube highlights.

## Tech Stack

- **Frontend:** React 18, React Router, Vite
- **Backend:** FastAPI, SQLAlchemy, SQLite
- **Data:** 22 tournaments, 83 teams, 44 matches, 30 historical moments

## Routes

| Path | Description |
|------|-------------|
| `/` | Home |
| `/tournaments` | All World Cups |
| `/tournaments/:id` | Single tournament detail |
| `/matches` | All matches |
| `/matches/:id` | Match detail with moments |
| `/teams` | All national teams |
| `/teams/:id` | Team detail + appearances |
| `/moments` | All historical moments |

## Setup & Run

```bash
# Install dependencies
npm run install:all

# Seed the database
npm run seed

# Start both servers (backend :3001 + frontend :5173)
npm run dev
```

Or run each separately:

```bash
cd server && uvicorn app.main:app --reload --port 3001
cd client && npm run dev
```

### Production build

```bash
npm run build
```

The FastAPI server will serve the built client from `client/dist/` on `:3001`.
