from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload

from ..database import get_db
from ..models import Team, Match, Tournament
from ..schemas import TeamOut, TeamDetailOut, MatchOut

router = APIRouter(prefix="/api/teams", tags=["teams"])


def _match_to_out(m: Match) -> MatchOut:
    return MatchOut(
        id=m.id,
        tournament_id=m.tournament_id,
        stage=m.stage,
        date=m.date,
        team1_id=m.team1_id,
        team2_id=m.team2_id,
        score_team1=m.score_team1,
        score_team2=m.score_team2,
        winner_id=m.winner_id,
        venue=m.venue,
        city=m.city,
        attendance=m.attendance,
        team1_name=m.team1.name if m.team1 else None,
        team2_name=m.team2.name if m.team2 else None,
        winner_name=m.winner.name if m.winner else None,
        tournament_year=m.tournament.year if m.tournament else None,
        tournament_host=m.tournament.host if m.tournament else None,
    )


@router.get("", response_model=list[TeamOut])
def list_teams(db: Session = Depends(get_db)):
    return db.query(Team).order_by(Team.name.asc()).all()


@router.get("/{team_id}", response_model=TeamDetailOut)
def get_team(team_id: int, db: Session = Depends(get_db)):
    team = db.query(Team).filter(Team.id == team_id).first()
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")

    matches = (
        db.query(Match)
        .options(joinedload(Match.team1), joinedload(Match.team2), joinedload(Match.winner), joinedload(Match.tournament))
        .filter((Match.team1.has(Team.id == team_id)) | (Match.team2.has(Team.id == team_id)))
        .order_by(Match.tournament_id.desc(), Match.date.asc())
        .all()
    )

    titles = (
        db.query(Tournament)
        .filter(Tournament.winner == team.name)
        .count()
    )
    runner_up = (
        db.query(Tournament)
        .filter(Tournament.runner_up == team.name)
        .count()
    )

    return TeamDetailOut(
        id=team.id,
        name=team.name,
        country_code=team.country_code,
        matches=[_match_to_out(m) for m in matches],
        titles=titles,
        runner_up=runner_up,
    )
