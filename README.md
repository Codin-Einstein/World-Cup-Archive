# World Cup Archive

A full-stack web app for exploring FIFA World Cup history: Tournaments, matches, teams, and iconic moments with embedded YouTube highlights.

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

## Prerequisites

- **Node.js** 18+
- **Python** 3.10+
- **npm** (comes with Node.js)

---

## Setup & Run

### 1. Create a Python virtual environment

Isolates Python dependencies to avoid conflicts with system packages.

#### Linux / macOS
```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows (PowerShell)
```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

#### Windows (CMD)
```cmd
python -m venv venv
venv\Scripts\activate.bat
```

> Your shell prompt will show `(venv)` when the environment is active.
> Run `deactivate` to exit the virtual environment.

### 2. Install dependencies

```bash
npm run install:all
```

> This runs `npm install` in `client/` and `pip install -r requirements.txt` (inside the venv) in `server/`.

### 3. Seed the database

```bash
npm run seed
```

### 4. Start the app

#### Run both servers together (requires `npm run install:all` first)
```bash
# Make sure your venv is active first!
npm run dev
```

#### Run each server separately

**Backend (FastAPI on `:3001`)**

| Platform | Command |
|----------|---------|
| Linux / macOS | `cd server && source ../venv/bin/activate && uvicorn app.main:app --reload --port 3001` |
| Windows (PowerShell) | `cd server; ..\venv\Scripts\Activate.ps1; uvicorn app.main:app --reload --port 3001` |
| Windows (CMD) | `cd server && ..\venv\Scripts\activate.bat && uvicorn app.main:app --reload --port 3001` |

**Frontend (Vite on `:5173`)**

```bash
cd client && npm run dev
```

> You can also open a second terminal: run the backend in one and the frontend in the other.

### Production build

```bash
npm run build
```

The FastAPI server will serve the built client from `client/dist/` on `:3001`.

---

<small>Node modules (`node_modules/`) and the virtual environment (`venv/`) are gitignored, clone and repeat these steps on each machine.</small>
