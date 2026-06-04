from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

from .database import Base


class Tournament(Base):
    __tablename__ = "tournaments"

    id = Column(Integer, primary_key=True, autoincrement=True)
    year = Column(Integer, nullable=False, unique=True)
    host = Column(String, nullable=False)
    winner = Column(String, nullable=False)
    runner_up = Column(String, nullable=False)
    third_place = Column(String, nullable=True)
    fourth_place = Column(String, nullable=True)
    total_goals = Column(Integer, nullable=True)
    total_matches = Column(Integer, nullable=True)
    attendance = Column(Integer, nullable=True)

    matches = relationship("Match", back_populates="tournament")


class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)
    country_code = Column(String, nullable=False)

    matches_as_team1 = relationship(
        "Match", foreign_keys="Match.team1_id", back_populates="team1"
    )
    matches_as_team2 = relationship(
        "Match", foreign_keys="Match.team2_id", back_populates="team2"
    )
    matches_won = relationship(
        "Match", foreign_keys="Match.winner_id", back_populates="winner"
    )


class Match(Base):
    __tablename__ = "matches"

    id = Column(Integer, primary_key=True, autoincrement=True)
    tournament_id = Column(Integer, ForeignKey("tournaments.id"), nullable=False)
    stage = Column(String, nullable=False)
    date = Column(String, nullable=False)
    team1_id = Column(Integer, ForeignKey("teams.id"), nullable=False)
    team2_id = Column(Integer, ForeignKey("teams.id"), nullable=False)
    score_team1 = Column(Integer, nullable=True)
    score_team2 = Column(Integer, nullable=True)
    winner_id = Column(Integer, ForeignKey("teams.id"), nullable=True)
    venue = Column(String, nullable=True)
    city = Column(String, nullable=True)
    attendance = Column(Integer, nullable=True)

    tournament = relationship("Tournament", back_populates="matches")
    team1 = relationship("Team", foreign_keys=[team1_id], back_populates="matches_as_team1")
    team2 = relationship("Team", foreign_keys=[team2_id], back_populates="matches_as_team2")
    winner = relationship("Team", foreign_keys=[winner_id], back_populates="matches_won")
    moments = relationship("Moment", back_populates="match", order_by="Moment.id")


class Moment(Base):
    __tablename__ = "moments"

    id = Column(Integer, primary_key=True, autoincrement=True)
    match_id = Column(Integer, ForeignKey("matches.id"), nullable=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    video_url = Column(String, nullable=False)
    source = Column(String, default="YouTube")
    category = Column(String, default="highlight")

    match = relationship("Match", back_populates="moments")
