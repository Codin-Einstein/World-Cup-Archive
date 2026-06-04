from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import Tournament, Match, Team
from ..schemas import TournamentOut, TournamentDetailOut, MatchOut

router = APIRouter(prefix="/api/tournaments", tags=["tournaments"])


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


@router.get("", response_model=list[TournamentOut])
def list_tournaments(db: Session = Depends(get_db)):
    return db.query(Tournament).order_by(Tournament.year.desc()).all()


@router.get("/{tournament_id}", response_model=TournamentDetailOut)
def get_tournament(tournament_id: int, db: Session = Depends(get_db)):
    tournament = db.query(Tournament).filter(Tournament.id == tournament_id).first()
    if not tournament:
        raise HTTPException(status_code=404, detail="Tournament not found")

    matches = (
        db.query(Match)
        .filter(Match.tournament_id == tournament_id)
        .order_by(Match.date.asc())
        .all()
    )

    return TournamentDetailOut(
        id=tournament.id,
        year=tournament.year,
        host=tournament.host,
        winner=tournament.winner,
        runner_up=tournament.runner_up,
        third_place=tournament.third_place,
        fourth_place=tournament.fourth_place,
        total_goals=tournament.total_goals,
        total_matches=tournament.total_matches,
        attendance=tournament.attendance,
        matches=[_match_to_out(m) for m in matches],
    )
