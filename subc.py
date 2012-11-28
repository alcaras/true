from trueskill import trueskill as trueskill

print "subc in house league"

class Player(object):
    def __init__(self):
        self.skill = (25.0, 25.0/3.0) 
        self.rank = 0


# regulars
players = {"alcaras" : Player(),
           "Wyv" : Player(),
           "Boozie" : Player(),
           "Krygore" : Player(),
           "Vorsh" : Player(),
           "Rip" : Player(),
           "Speed" : Player(),
           "m1gemini" : Player(),
           "Skolops" : Player(),
           # guests
           "lostsights" : Player(), # Vorsh's friends
           "Brewskis" : Player(),
           "dgeis7121" : Player(), 
           "Sekans_Aval" : Player(),
           # more guests
           "Anias" : Player(),
           # Boozie's friends
           "Janker" : Player(), # aka Poo Flinger
           
           }

# matches -- teams are a list of strings of player's names
# winning team first
def do_match(win, loss):
    master_list = []
    for p in win:
        players[p].rank = 1
        master_list += [players[p]]
    for p in loss:
        players[p].rank = 2
        master_list += [players[p]]
    trueskill.AdjustPlayers(master_list)

def show_rankings():
    pl = {}
    for k, v in players.iteritems():
        pl[k] = v.skill[0] - v.skill[1] # floor on skill
    sorted_pl = sorted(pl.iteritems(),
                            key = lambda(k, v): (v, k),
                            reverse=True)
    for p in sorted_pl:
        print(p[0].rjust(20) + ": " + format(p[1], ".1f"))
    print

# game 1: november 15, 2012
# http://steamcommunity.com/sharedfiles/filedetails/?id=108536439
do_match(["alcaras", "Wyv", "Boozie", "Krygore", "Skolops"],
         ["Vorsh", "lostsights", "Rip", "Speed", "m1gemini"])

# game 2: 

do_match(["Vorsh", "Rip", "Wyv", "Skolops", "Krygore"],
         ["Boozie", "Speed", "Brewskis", "m1gemini", "alcaras"])

# interlude
# capital one v. subc

#do_match(["Vorsh", "lostsights", "Brewskis", "dgeis7121", "Sekans_Aval"],
#         ["Krygore", "Speed", "Vorsh", "Rip", "alcaras"])

# game 3 -- nov 27
# anias guests
do_match(["dgeis7121", "Anias", "Boozie", "Speed", "m1gemini"],
         ["Brewskis", "Vorsh", "alcaras", "Rip", "Janker"])

# game 4
do_match(["Brewskis", "Boozie", "Wyv", "Speed", "m1gemini"],
         ["dgeis7121", "Vorsh", "alcaras", "Rip", "Janker"])

show_rankings()




