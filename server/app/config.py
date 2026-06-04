import os
from pathlib import Path


class Settings:
    DATABASE_PATH: Path = Path(__file__).parent.parent / "worldcup.db"
    CLIENT_DIST_PATH: Path = Path(__file__).parent.parent.parent / "client" / "dist"
    CORS_ORIGINS: list[str] = [
        "http://localhost:5173",
        "http://localhost:3001",
    ]
    DEBUG: bool = False

    def __init__(self):
        extra = os.getenv("CORS_ORIGINS", "")
        if extra:
            self.CORS_ORIGINS.extend([o.strip() for o in extra.split(",") if o.strip()])


settings = Settings()
