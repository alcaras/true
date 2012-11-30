from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from hap import *

Base = declarative_base()
 
class Game(Base):
    __tablename__ = 'games'
    id = Column(Integer, primary_key=True)
    type = Column(String)
    mode = Column(String)
    duration = Column(String)
    region = Column(String)
    played = Column(Date)
    winner = Column(String)

    def __init__(self, id, type, mode, duration, region, played, winner):
        self.id = id
        self.type = type
        self.mode = mode
        self.duration = duration
        self.region = region
        self.played = played
        self.winner = winner
        
    def __repr__(self):
        return "<Game('%s')>" % (self.id)

class Score(Base):
    __tablename__ = 'scores'
    id = Column(Integer, primary_key=True)
    player_id = Column(Integer)
    game_id = Column(Integer, ForeignKey("games.id"))
    game = relationship("Game", backref=backref('scores', order_by=id))
    # players = [won, side, player, hero, level, k, d, a, lh, dn, xpm, gpm, [items]]
    won = Column(Integer)
    side = Column(String)
    hero = Column(String)
    level = Column(Integer)
    kills = Column(Integer)
    deaths = Column(Integer)
    assists = Column(Integer)
    last_hits = Column(Integer)
    denies = Column(Integer)
    xpm = Column(Integer)
    gpm = Column(Integer)
    item1 = Column(String)
    item2 = Column(String)
    item3 = Column(String)
    item4 = Column(String)
    item5 = Column(String)
    item6 = Column(String)
    points = Column(Integer)
    def __init__(self, player_id, hero, level, kills, deaths,
                 assists, last_hits, denies, xpm, gpm,
                 item1, item2, item3, item4, item5, item6,
                 side, won):
        self.player_id = player_id
        self.hero = hero
        self.level = level
        self.kills = kills
        self.deaths = deaths
        self.assists = assists
        self.last_hits = last_hits
        self.denies = denies
        self.xpm = xpm
        self.gpm = gpm
        self.item1 = item1
        self.item2 = item2
        self.item3 = item3
        self.item4 = item4
        self.item5 = item5
        self.item6 = item6
        self.side = side
        self.won = won
        self.points = hap(hero, kills, deaths, assists, gpm)

    def __repr__(self):
        return "<Score('%s', '%s', '%s')>" % (self.game_id, self.player_id, self.hero)


