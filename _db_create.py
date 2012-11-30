from sqlalchemy import create_engine
engine = create_engine('sqlite:///master.db', echo=False)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref

class Game(Base):
    __tablename__ = 'games'
    id = Column(Integer, primary_key=True)
    type = Column(String)
    mode = Column(String)
    duration = Column(String)
    region = Column(String)
    played = Column(String)
    winner = Column(String)

    def __init__(self, id, type, mode, duration, region, played, winner):
        self.id = id
        self.type = type
        self.mode = mode
        self.duration = duration
        self.region = region
        self.played = played
        self.winner = winner
        
    def __repr__self(self):
        return "<Game('%s')>" % (self.id)

class Score(Base):
    __tablename__ = 'scores'
    id = Column(Integer, primary_key=True)
    player_id = Column(Integer)
    game_id = relationship("Game", backref=backref('scores', order_by=id))
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

    
Base.metadata.create_all()
