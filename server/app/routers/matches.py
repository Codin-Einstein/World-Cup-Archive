from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session, joinedload

from ..database import get_db
from ..models import Match, Team, Tournament, Moment
from ..schemas import MatchOut, MatchDetailOut, MomentOut

router = APIRouter(prefix="/api/matches", tags=["matches"])


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


@router.get("", response_model=list[MatchOut])
def list_matches(
    stage: Optional[str] = Query(None),
    team: Optional[str] = Query(None),
    year: Optional[int] = Query(None),
    db: Session = Depends(get_db),
):
    q = (
        db.query(Match)
        .options(joinedload(Match.team1), joinedload(Match.team2), joinedload(Match.winner), joinedload(Match.tournament))
    )

    if stage:
        q = q.filter(Match.stage == stage)
    if team:
        q = q.filter((Match.team1.has(Team.name == team)) | (Match.team2.has(Team.name == team)))
    if year:
        q = q.filter(Match.tournament.has(Tournament.year == year))

    matches = q.order_by(Match.date.desc()).all()
    return [_match_to_out(m) for m in matches]


@router.get("/{match_id}", response_model=MatchDetailOut)
def get_match(match_id: int, db: Session = Depends(get_db)):
    match = (
        db.query(Match)
        .options(
            joinedload(Match.team1),
            joinedload(Match.team2),
            joinedload(Match.winner),
            joinedload(Match.tournament),
            joinedload(Match.moments),
        )
        .filter(Match.id == match_id)
        .first()
    )
    if not match:
        raise HTTPException(status_code=404, detail="Match not found")

    base = _match_to_out(match)
    return MatchDetailOut(
        **base.model_dump(),
        moments=[
            MomentOut(
                id=mom.id,
                match_id=mom.match_id,
                title=mom.title,
                description=mom.description,
                video_url=mom.video_url,
                source=mom.source,
                category=mom.category,
            )
            for mom in match.moments
        ],
    )
