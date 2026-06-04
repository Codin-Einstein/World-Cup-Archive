from pydantic import BaseModel
from typing import Optional


class TournamentOut(BaseModel):
    id: int
    year: int
    host: str
    winner: str
    runner_up: str
    third_place: Optional[str] = None
    fourth_place: Optional[str] = None
    total_goals: Optional[int] = None
    total_matches: Optional[int] = None
    attendance: Optional[int] = None


class MatchOut(BaseModel):
    id: int
    tournament_id: int
    stage: str
    date: str
    team1_id: int
    team2_id: int
    score_team1: Optional[int] = None
    score_team2: Optional[int] = None
    winner_id: Optional[int] = None
    venue: Optional[str] = None
    city: Optional[str] = None
    attendance: Optional[int] = None
    team1_name: Optional[str] = None
    team2_name: Optional[str] = None
    winner_name: Optional[str] = None
    tournament_year: Optional[int] = None
    tournament_host: Optional[str] = None


class TournamentDetailOut(TournamentOut):
    matches: list[MatchOut] = []


class MomentOut(BaseModel):
    id: int
    match_id: Optional[int] = None
    title: str
    description: Optional[str] = None
    video_url: str
    source: str = "YouTube"
    category: str = "highlight"


class MomentWithMatchOut(MomentOut):
    match_date: Optional[str] = None
    team1_name: Optional[str] = None
    team2_name: Optional[str] = None
    tournament_year: Optional[int] = None


class MatchDetailOut(MatchOut):
    moments: list[MomentOut] = []


class TeamOut(BaseModel):
    id: int
    name: str
    country_code: str


class TeamDetailOut(TeamOut):
    matches: list[MatchOut] = []
    titles: int = 0
    runner_up: int = 0


class TitleCount(BaseModel):
    winner: str
    titles: int


class StatsOut(BaseModel):
    count: int
    total: int
    total_goals: int
    teams: int
    mostTitles: list[TitleCount] = []
