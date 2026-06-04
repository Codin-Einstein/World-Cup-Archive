from typing import Optional

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session, joinedload

from ..database import get_db
from ..models import Moment, Match, Tournament
from ..schemas import MomentWithMatchOut

router = APIRouter(prefix="/api/moments", tags=["moments"])


@router.get("", response_model=list[MomentWithMatchOut])
def list_moments(
    category: Optional[str] = Query(None),
    db: Session = Depends(get_db),
):
    q = (
        db.query(Moment)
        .options(
            joinedload(Moment.match).joinedload(Match.team1),
            joinedload(Moment.match).joinedload(Match.team2),
            joinedload(Moment.match).joinedload(Match.tournament),
        )
    )

    if category:
        q = q.filter(Moment.category == category)

    moments = q.order_by(Moment.id.asc()).all()

    result = []
    for mom in moments:
        m = mom.match
        result.append(MomentWithMatchOut(
            id=mom.id,
            match_id=mom.match_id,
            title=mom.title,
            description=mom.description,
            video_url=mom.video_url,
            source=mom.source,
            category=mom.category,
            match_date=m.date if m else None,
            team1_name=m.team1.name if m and m.team1 else None,
            team2_name=m.team2.name if m and m.team2 else None,
            tournament_year=m.tournament.year if m and m.tournament else None,
        ))

    return result
