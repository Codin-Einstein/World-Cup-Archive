from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from ..database import get_db
from ..models import Tournament, Match, Team
from ..schemas import StatsOut, TitleCount

router = APIRouter(prefix="/api/stats", tags=["stats"])


@router.get("", response_model=StatsOut)
def get_stats(db: Session = Depends(get_db)):
    tournament_count = db.query(func.count(Tournament.id)).scalar() or 0
    match_count = db.query(func.count(Match.id)).scalar() or 0
    team_count = db.query(func.count(Team.id)).scalar() or 0
    total_goals = db.query(func.coalesce(func.sum(Tournament.total_goals), 0)).scalar() or 0

    title_rows = (
        db.query(Tournament.winner, func.count(Tournament.id).label("titles"))
        .group_by(Tournament.winner)
        .order_by(func.count(Tournament.id).desc())
        .limit(5)
        .all()
    )

    return StatsOut(
        count=tournament_count,
        total=match_count,
        total_goals=int(total_goals),
        teams=team_count,
        mostTitles=[TitleCount(winner=row.winner, titles=row.titles) for row in title_rows],
    )
