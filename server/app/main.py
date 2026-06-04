import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from .config import settings
from .database import engine, Base
from .routers import tournaments, matches, teams, moments, stats

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("worldcup")

app = FastAPI(title="World Cup Archive API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tournaments.router)
app.include_router(matches.router)
app.include_router(teams.router)
app.include_router(moments.router)
app.include_router(stats.router)

dist = settings.CLIENT_DIST_PATH
if dist.exists():
    app.mount("/assets", StaticFiles(directory=str(dist / "assets")), name="assets")

    @app.get("/{full_path:path}")
    async def serve_spa(full_path: str):
        index = dist / "index.html"
        if index.exists():
            return FileResponse(str(index))
        return {"error": "not found"}
else:
    @app.get("/")
    async def root():
        return {"message": "World Cup Archive API. Client build not found. Run 'npm run build' in client directory or use Vite dev server on :5173."}


@app.on_event("startup")
async def startup():
    Base.metadata.create_all(bind=engine)
    logger.info("Database tables verified")
