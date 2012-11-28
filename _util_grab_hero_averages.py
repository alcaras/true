# http://fantasy.dota-academy.com/HeroAverages


page = "http://fantasy.dota-academy.com/HeroAverages"


from heroes import heroes

import mechanize
import string
import re
import pprint
pp = pprint.PrettyPrinter(indent = 4)

# override mechanize's history behavior
class NoHistory(object):
  def add(self, *a, **k): pass
  def clear(self): pass

br = mechanize.Browser(factory=mechanize.RobustFactory(), history=NoHistory())

#response = br.open(page)
#data = response.read()
f = open('hero-averages.html', 'r')
data = f.read()

data = data.replace('&#x27;', "'")

# we want to rip out winrates
# rubular.com is useful for setting up strings

# dear god
regex = '<span style="color:white">(.*)<\/span>\s<\/td>\s<td style="vertical-align:middle;padding-right:60px; padding-top:35px;">\s<span class="avtitle">\s<img height=24 src="\/assets\/icons\/kills.png" title="Kills"\/>\s<\/span>\s<span class="bleft">&nbsp;<\/span>\s<span class="worst">([\d]*\.[\d]*)<\/span>\s<span class="worse">([\d]*\.[\d]*) - ([\d]*\.[\d]*)<\/span>\s<span class="bad">([\d]*\.[\d]*) - ([\d]*\.[\d]*) <\/span>\s<span class="good">([\d]*\.[\d]*) - ([\d]*\.[\d]*)<\/span>\s<span class="better">([\d]*\.[\d]*) - ([\d]*\.[\d]*)<\/span>\s<span class="best">([\d]*\.[\d]*)\+<\/span>\s<span class="bright">&nbsp;<\/span>\s<\/td>\s<\/tr>\s<tr>\s<td style="vertical-align:middle;"><span class="avtitle">\s<img height=24 title="Deaths" src="\/assets\/icons\/Skull-icon.gif"\/><\/span>\s<span class="bleft">&nbsp;<\/span>\s<span class="worst">([\d]*\.[\d]*)\+<\/span>\s<span class="worse">([\d]*\.[\d]*) - ([\d]*\.[\d]*)<\/span>\s<span class="bad">([\d]*\.[\d]*) - ([\d]*\.[\d]*)<\/span>\s<span class="good">([\d]*\.[\d]*) - ([\d]*\.[\d]*)<\/span>\s<span class="better">([\d]*\.[\d]*) - ([\d]*\.[\d]*)<\/span>\s<span class="best">([\d]*\.[\d]*)<\/span>\s<span class="bright">&nbsp;<\/span>\s<\/td>\s<\/tr><tr>\s<td style="vertical-align:middle;"><span class="avtitle"> <img height=24 title="Assists" src="\/assets\/icons\/hand.png"\/><\/span> <span class="bleft">&nbsp;<\/span><span class="worst">([\d]*\.[\d]*)<\/span><span class="worse">([\d]*\.[\d]*) - ([\d]*\.[\d]*)<\/span><span class="bad">([\d]*\.[\d]*) - ([\d]*\.[\d]*) <\/span> <span class="good">([\d]*\.[\d]*) - ([\d]*\.[\d]*)<\/span><span class="better">([\d]*\.[\d]*) - ([\d]*\.[\d]*)<\/span><span class="best">([\d]*\.[\d]*)\+<\/span><span class="bright">&nbsp;<\/span><\/td><\/tr><tr>\s<td style="vertical-align:middle; padding-bottom:10px;"><span class="avtitle"> <img height=24 title="GPM" src="\/assets\/icons\/farm.png"\/><\/span> <span class="bleft">&nbsp;<\/span><span class="worst"> ([\d]*) - ([\d]*)<\/span><span class="worse">([\d]*) - ([\d]*)<\/span><span class="bad">([\d]*) - ([\d]*) <\/span> <span class="good">([\d]*) - ([\d]*)<\/span><span class="better">([\d]*) - ([\d]*)<\/span><span class="best">([\d]*)\+<\/span><span class="bright">&nbsp;<\/span><\/td><\/tr><tr>\s<\/tr>'

match = re.findall(regex, data)

hero_averages = {}
for a in match:
    hero_averages[a[0]] = {}
    hero_averages[a[0]]["kills"] = [a[2], a[4], a[6], a[8], a[10]]
    hero_averages[a[0]]["deaths"] = [a[12], a[14], a[16], a[18], a[20]]
    hero_averages[a[0]]["assists"] = [a[22], a[24], a[26], a[28], a[30]]
    hero_averages[a[0]]["gpm"] = [a[32], a[34], a[36], a[38], a[40]]

print "hero_averages = ",
pp.pprint(hero_averages)




