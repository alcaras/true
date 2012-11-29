print "subc in house league (hero average points)"

players = {"alcaras" : {},
           "Wyv" : {},
           "Boozie" : {},
           "Krygore" : {},
           "Vorsh" : {},
           "Rip" : {},
           "Speed" : {},
           "m1gemini" : {},
           "Skolops" : {},
           # guests
           "lostsights" : {}, # Vorsh's friends
           "Brewskis" : {},
           "dgeis7121" : {}, 
           "Sekans_Aval" : {},
           "Redbox" : {},            
           # more guests
           "Anias" : {},
           # Boozie's friends
           "Janker" : {}, # aka Poo Flinger      

           }


import pdb
import pprint
import numpy
pp = pprint.PrettyPrinter(indent = 4)

from hap import *

def hap_score(hero, kills, deaths, assists, gpm, player="", verbose=True):
    global players
    if gpm == -1:
        return 0

    hap_ = hap(hero, kills, deaths, assists, gpm)
    if hap_ == -100:
        return
    if hero not in players[player]:
        players[player][hero] = [hap_]
    else:
        players[player][hero] += [hap_]
    if verbose==True:
        print str(player).ljust(15),
        print str(hero).ljust(20),
        print str(hap_).rjust(4)
    return

def show_rankings():
    pav = {}
    for pk, pv in players.iteritems():
        toss = []
        for hk, hv in pv.iteritems():
                toss += hv
        if toss != []:
            pav[pk] = numpy.mean(toss)
    sorted_pav = sorted(pav, key=lambda(k): pav[k], reverse=True)
    for p in sorted_pav:
        print str(p).ljust(15), str(round(pav[p],2)).rjust(10)
    return pav



    


# game 1: november 15, 2012
# http://steamcommunity.com/sharedfiles/filedetails/?id=108536439
#do_match(["alcaras", "Wyv", "Boozie", "Krygore", "Skolops"],
#         ["Vorsh", "lostsights", "Rip", "Speed", "m1gemini"])

print "game 1"
# need gpm
# dire, victorious
hap_score("Dark Seer", 7, 3, 19, 338, "alcaras")
hap_score("Viper", 13, 6, 13, 414, "Wyv")
hap_score("Necrolyte", 7, 5, 25, 325, "Krygore")
hap_score("Lich", 3, 3, 16, 199, "Skolops")
hap_score("Slardar", 6, 3, 18, 399, "Boozie")

# radiant
hap_score("Tidehunter", 2, 7, 11, 189, "Vorsh")
hap_score("Templar Assassin", 4, 6, 7, 270, "lostsights")
hap_score("Death Prophet", 8, 9, 6, 262, "Speed")
hap_score("Sand King", 4, 5, 12, 192, "Rip")
hap_score("Sven", 1, 10, 12, 168, "m1gemini")
                     
print

print "game 2"
                                            
# game 2: 
#do_match(["Vorsh", "Rip", "Wyv", "Skolops", "Krygore"],
#         ["Boozie", "Speed", "Brewskis", "m1gemini", "alcaras"])
# dire, victorious
hap_score("Undying", 12, 6, 16, 387, "Vorsh")
hap_score("Magnus", 7, 3, 12, 492, "Rip")
hap_score("Lion", 3, 5, 15, 231, "Wyv")
hap_score("Lich", 3, 11, 13, 165, "Skolops")
hap_score("Huskar", 7, 8, 4, 358, "Krygore")

# radiant
hap_score("Bounty Hunter", 15, 5, 10, 434, "Boozie")
hap_score("Jakiro", 3, 9, 18, 215, "Speed")
hap_score("Batrider", 4, 7, 12, 270, "Brewskis")
hap_score("Sven", 0, 10, 6, 229, "m1gemini")
hap_score("Dark Seer", 8, 3, 12, 404, "alcaras")

print 

# clanwar 1
# capital one v. subc

#do_match(["Vorsh", "lostsights", "Brewskis", "dgeis7121", "Sekans_Aval"],
#         ["Krygore", "Speed", "Vorsh", "Rip", "alcaras"])

# radiant, victorious
# hap_score("Bounty Hunter", 2, 0, 2, 297, "Vorsh")
# hap_score("Jakiro", 2, 3, 9, 243, "dgeis7121")
# hap_score("Faceless Void", 3, 1, 2, 335, "Brewskis")
# hap_score("Lina", 0, 1, 2, 187, "Sekans_Aval")
# hap_score("Pudge", 7, 2, 4, 342, "lostsights") # aka sly

# # dire
# hap_score("Windrunner", 0, 2, 3, 104, "alcaras")
# hap_score("Earthshaker", 1, 2, 3, 120, "Rip")
# hap_score("Dragon Knight", 1, 2, 0, 224, "Wyv")
# hap_score("Huskar", 2, 7, 1, 187, "Krygore")
# hap_score("Queen of Pain", 1, 2, 2, 164, "Speed")

print "game 3"
# game 3 -- nov 27
# anias guests
#do_match(["dgeis7121", "Anias", "Boozie", "Speed", "m1gemini"],
#         ["Brewskis", "Vorsh", "alcaras", "Rip", "Janker"])

# dire, victorious
hap_score("Luna", 3, 1, 10, 538, "dgeis7121")
hap_score("Night Stalker", 12, 1, 10, 472, "Anias")
hap_score("Undying", 11, 0, 10, 467, "Boozie")
hap_score("Dazzle", 0, 0, 5, 248, "Speed")
hap_score("Lion", 1, 8, 10, 229, "m1gemini")

# radiant
hap_score("Nature's Prophet", 2, 6, 1, 336, "Brewskis")
hap_score("Razor", 3, 6, 1, 218, "Vorsh")
hap_score("Dark Seer", 1, 5, 3, 210, "alcaras")
hap_score("Jakiro", 3, 3, 3, 148, "Rip")
hap_score("Pugna", 1, 9, 4, 143, "Janker")

print

# game 4
#do_match(["Brewskis", "Boozie", "Wyv", "Speed", "m1gemini"],
#         ["dgeis7121", "Vorsh", "alcaras", "Rip", "Janker"])

print "game 4"

# dire, victorious
hap_score("Queen of Pain", 13, 4, 21, 446, "Brewskis")
hap_score("Magnus", 11, 5, 20, 439, "Boozie")
hap_score("Lifestealer", 6, 3, 14, 543, "Wyv")
hap_score("Windrunner", 8, 4, 6, 368, "Speed")
hap_score("Lich", 4, 7, 23, 286, "m1gemini")

# radiant
hap_score("Viper", 8, 10, 8, 346, "dgeis7121")
hap_score("Dragon Knight", 1, 6, 9, 270, "Vorsh")
hap_score("Tidehunter", 7, 9, 10, 225, "alcaras")
hap_score("Disruptor", 2, 6, 11, 176, "Rip")
hap_score("Venomancer", 4, 13, 11, 174, "Janker")

print

print "game 5"

# radiant victorious
hap_score("Leshrac", 8, 7, 20, 396, "alcaras")
hap_score("Templar Assassin", 7, 6, 26, 354, "Boozie")
hap_score("Bounty Hunter", 17, 5, 17, 472, "Vorsh")
hap_score("Lina", 12, 11, 13, 327, "Speed")
hap_score("Disruptor", 3, 6, 22, 202, "Rip")

# dire
hap_score("Weaver", 13, 6, 15, 391, "Brewskis")
hap_score("Slardar", 6, 10, 19, 315, "dgeis7121")
hap_score("Jakiro", 1, 13, 18, 172, "Redbox")
hap_score("Viper", 11, 10, 13, 312, "Wyv")
hap_score("Lich", 3, 8, 15, 173, "m1gemini")


pp.pprint(players)

sp = show_rankings()

balance_teams(sp, ["dgeis7121", "Anias", "Boozie", "Speed", "m1gemini",
                   "Brewskis", "Vorsh", "alcaras", "Rip", "Janker"])

