# /heroes/lycanthrope/tooltip
page = "https://dotabuff.com/matches/"
import sys
import traceback
import time


import urllib2
from dateutil import parser as dt_parser
from models import Game, Score
from heroes import heroes
import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from lxml import etree
import pdb
import mechanize
import string
import re
import pprint
pp = pprint.PrettyPrinter(indent = 4)
import argparse

dt = datetime.datetime

engine = create_engine('sqlite:///master.db', echo=False)
 
# create a Session
Session = sessionmaker(bind=engine)
session = Session()


# override mechanize's history behavior
class NoHistory(object):
  def add(self, *a, **k): pass
  def clear(self): pass


# return a list of match ids, given a player id and a page
def grab_match_ids(id, pnum):
  page = "https://dotabuff.com/players/"
  page_post = "/matches?page="
  br = mechanize.Browser(factory=mechanize.RobustFactory(), history=NoHistory())
  
  roles = {}
  url = page+id+page_post+str(pnum)
  print url
  response = br.open(url)
  
  data = response.read()
  data = data.replace('&#x27;', "'")

  regex = 'matchid">(\d*)<'

  match = re.findall(regex, data)

  ids = []
  for a in match:
    ids += [a]
     
  if pnum == 1:
    regex_2 = 'page=(\d*)">Last '
    match = re.findall(regex_2, data)
    if match is None:
      return [ids, -1]
    return [ids, match[0]]
  else:
    return [ids, -1]

def grab_match(id):
  # check if the id already exists
  if session.query(Game).filter(Game.id == id).first() is not None:
    # already parsed
    return -1 # already parsed
  
  url = page+id
#  print "Parsing", id, url
  print ".",

  br = mechanize.Browser(factory=mechanize.RobustFactory(), history=NoHistory())
  
  roles = {}

  response = br.open(url)
  
  data = response.read()
  data = data.replace('&#x27;', "'")


  regex = '<h1>Match (\d*)<\/h1><\/div><\/div><div id="content-header-secondary"><dl><dt>Type<\/dt><dd>(\w*)<\/dd><\/dl>(<dl><dt>Game Mode<\/dt><dd>([\w\s]*)<\/dd><\/dl>)*<dl><dt>Duration<\/dt><dd>(.*)<\/dd><\/dl><dl><dt>Region<\/dt><dd>(.*)<\/dd><\/dl><dl><dt>Played<\/dt><dd><time class="timeago" datetime="(\d*)-(\d*)-(\d*)T(\d*):(\d*):(\d*)Z" title="(.*)">(.*)<\/time>'
  match = re.findall(regex, data)

  game = {}
  game["id"] = match[0][0]
  game["type"] = match[0][1]
  game["mode"] = match[0][3]
  game["duration"] = match[0][4]
  game["region"] = match[0][5]
  game["played"] = match[0][12]
  game["winner"] = "" # radiant or dire

  regex_radiant_win = '<span class="team radiant">Radiant Victory<\/span>'
  regex_dire_win = '<span class="team dire">Dire Victory<\/span>'
  
  match = re.findall(regex_radiant_win, data)
  if match:
    game["winner"] = "Radiant"

  match = re.findall(regex_dire_win, data)
  if match:
    game["winner"] = "Dire"

  if game["winner"] == "":
    print id, "unknown winner"
    print "*********"
    

  
  # create the game
  new_game = Game(game["id"], game["type"], game["mode"],
                  game["duration"], game["region"],
                  dt_parser.parse(game["played"]),
                  game["winner"])

  new_game.scores = []
  
    
  # we'll parse players using etree
  root = etree.HTML(data)
 
  players = root.findall('.//table/tbody/tr')
  count = 0
  for p in players:
    proot = etree.HTML(etree.tostring(p))

    # players = [won, side, player, hero, level, k, d, a, lh, dn, xpm, gpm, [items]]
    pl = {}
    pl["won"] = 0

    # first five are on radiant, next five are on dire
    if count < 5:
      pl["side"] = "Radiant"
      if game["winner"] == "Radiant":
        pl["won"] = 1
    else:
      pl["side"] = "Dire"
      if game["winner"] == "Dire":
        pl["won"] = 1


        
    # player id
      
    regex_p = "/players/(\d*)"
    match = re.findall(regex_p,  etree.tostring(proot.findall('.//td/a')[0]))
    try:
      pl["player"] = match[0]
    except IndexError, e:
      print id, "is a bot game"
      return -2 # this is a bot game

    # player hero
    regex_p = 'class="hero-link">(.*)</a>'
    match = re.findall(regex_p,  etree.tostring(proot.findall('.//td/a')[1]))
    pl["hero"] = match[0]
    
    # hero level
    regex_p = '">(\d*)'
    match = re.findall(regex_p, etree.tostring(proot.findall('.//td[@class="cell-centered"]')[0]))
    pl["level"] = int(match[0])
    
    # kills
    regex_p = '">(\d*)'
    match = re.findall(regex_p, etree.tostring(proot.findall('.//td[@class="cell-centered"]')[1]))
    pl["kills"] = int(match[0])

    # deaths
    regex_p = '">(\d*)'
    match = re.findall(regex_p, etree.tostring(proot.findall('.//td[@class="cell-centered"]')[2]))
    pl["deaths"] = int(match[0])
    
    # assists
    regex_p = '">(\d*)'
    match = re.findall(regex_p, etree.tostring(proot.findall('.//td[@class="cell-centered"]')[3]))
    pl["assists"] = int(match[0])

    # gold
    regex_p = '">(.*)<'
    match = re.findall(regex_p, etree.tostring(proot.findall('.//td[@class="cell-centered"]')[4]))
    pl["gold"] = int(string.replace(match[0], ",", ""))

    # last hits
    regex_p = '">(\d*)'
    match = re.findall(regex_p, etree.tostring(proot.findall('.//td[@class="cell-centered"]')[5]))
    pl["lh"] = int(match[0])

    # denies
    regex_p = '">(\d*)'
    match = re.findall(regex_p, etree.tostring(proot.findall('.//td[@class="cell-centered"]')[6]))
    pl["dn"] = int(match[0])
    
    # xpm
    regex_p = '">(\d*)'
    match = re.findall(regex_p, etree.tostring(proot.findall('.//td[@class="cell-centered"]')[7]))
    pl["xpm"] = int(match[0])

    # gpm
    regex_p = '">(\d*)'
    match = re.findall(regex_p, etree.tostring(proot.findall('.//td[@class="cell-centered"]')[8]))
    pl["gpm"] = int(match[0])
    
    # items
    items = proot.findall('.//td/div[@class="image-container image-container-icon image-container-item"]')
    player_items = []
    for ite in items:
      regex_i = '<img alt="(.*)" class="image-icon'
      match = re.findall(regex_i, etree.tostring(ite))
      player_items += [match[0]]

    pl["items"] = player_items

    plitems = ["", "", "", "", "", ""]

    for i, k in enumerate(pl["items"]):
      plitems[i] = k
    

#                 (player_id, hero, level, kills, deaths,
#                  assists, last_hits, denies, xpm, gpm,
#                  item1, item2, item3, item4, item5, item6,
#                  side, won):

    # players = [player, hero, level, k, d, a, lh, dn, xpm, gpm, [items]]
    new_score = Score(pl["player"], pl["hero"], pl["level"],
                      pl["kills"], pl["deaths"], pl["assists"],
                      pl["lh"], pl["dn"], pl["xpm"], pl["gpm"],
                      plitems[0], plitems[1], plitems[2], 
                      plitems[3], plitems[4], plitems[5],
                      pl["side"], pl["won"])


    new_game.scores.extend([new_score])
    

    count += 1

  session.add(new_game)
  session.commit()
  return 1 # all good



name_id = {
  "alcaras": "32775483",
  "rip" : "8899909",
  "speed": "9541377",
  "krygore" : "9929964",
  "vorsh" : "703282",
  "m1gemini" : "8807692",
  "Skolops" : "115058462",
# all done with these
#           "wyv": "64684222",
#           "boozie" : "537293",
#           "anias" : "32457950",
#           "Brewskis" : "33402007",


# holding off on these
#            "lostsights" : "431886",
#            "dgeis7121" : "100516439", 
#            "Sekans_Aval" : "30473417",
#            "Janker" : "55376440", 
#            "Redbox" : "40453657",
           }
bte
up_through = '' # the latest id we've parsed through (pull from the db)

for k, v in name_id.iteritems():
  print dt.now(), "starting ", k
  # figure out how many pages there are
  ids, max_page = grab_match_ids(v, 1)
  print dt.now(), k, "page 1 of ", max_page
  for id in ids:
    try:
      grab_match(id)     
      time.sleep(0.4)
    except urllib2.HTTPError, e:
        print dt.now(), e.code
        time.sleep(10)
        continue
    except Exception, e:
        print  dt.now(), "Exception:", e, sys.exc_info()[0]
        print '-'*60
        traceback.print_exc(file=sys.stdout)
        print '-'*60
        time.sleep(3)
        continue
  print
  for i in range(2, int(max_page)+1):
    print dt.now(), k, "page ", i, " of ", max_page
    ids, _ = grab_match_ids(v, i)
    for id in ids:
      try:
        grab_match(id)
        time.sleep(0.4)
      except urllib2.HTTPError, e:
        print dt.now(), e.code
        time.sleep(10)
        continue
      except Exception, e:
        print  dt.now(), "Exception:", e, sys.exc_info()[0]
        print '-'*60
        traceback.print_exc(file=sys.stdout)
        print '-'*60
        time.sleep(3)
        continue
    print




      
