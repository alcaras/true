import numpy
from hero_averages import *


# sp is a dictionary of all players + scores
# p is the list of players in this particular game
def balance_teams(sp, p):
    total=indexA=indexB=i=j=sideA=sideB=0

    OFFSET = 13
    arr = []
    count = 0
    for k in p:
        count += 1
        # lowest possible score is -12
        # to avoid negative numbers, add 13
        arr += [sp[k] + OFFSET]
        
    if count != 10:
        print "don't have data for 10 players"
        return

    total = numpy.sum(arr)
    n = 10
    split = n/2

    a = b = [0]*n
    arr.sort()
     
    indexA = 0
    while indexA< split :
        indexA = indexA+1
        a[indexA] = arr[i]

        if(indexA< split):
            indexA=indexA+1
            a[indexA] = arr[n-i-1]
            sideA = sideA+arr[n-i-1]
            sideA = sideA+arr[i]

        i=i+1
        j=i

    while indexB < n-split :
        indexB=indexB+1
        b[indexB] = arr[j]
        sideB = sideB+arr[j]
        j=j+1

    t1 = split - 1
    t2 = split


    sideA = sideA + (b[t2]-a[t1])
    sideB = sideB + (a[t1]-b[t2])

    # split is always odd, since n = 10
    sideA = min(sideA, sideB)
    sideB= max(sideA, sideB)

    print 
    

    team_one = []

    for v in a:
        if v > 0:
            find = v - OFFSET
            for k, w in sp.iteritems():
                if round(w,2) == round(find,2):
                    team_one += [k]
    
    team_two = []
    
    for y in p:
        if y not in team_one:
            team_two += [y]
        
    
    print team_one
    z = 0
    for y in team_one:
        z += sp[y]
        print str(y).ljust(15), str(round(sp[y],2)).rjust(10)
    print z
    print
    print team_two
    z = 0
    for y in team_two:
        z += sp[y]
        print str(y).ljust(15), str(round(sp[y],2)).rjust(10)
    print z

    

    # print the possible teams

    

    return


def hap(hero, k, d, a, gpm):
    if hero not in hero_averages: # no data for that hero
        return -100
    score = 0

    if  k >= float(hero_averages[hero]["kills"][4]):
        score += 5
    elif k >= float(hero_averages[hero]["kills"][3]):
        score += 3
    elif k >= float(hero_averages[hero]["kills"][2]):
        score += 1
    elif k >= float(hero_averages[hero]["kills"][1]):
        score += 0
    elif k >= float(hero_averages[hero]["kills"][0]):
        score += -1
    else:
        score += -3

    if  d <= float(hero_averages[hero]["deaths"][4]):
        score += 5
    elif d <= float(hero_averages[hero]["deaths"][3]):
        score += 3
    elif d <= float(hero_averages[hero]["deaths"][2]):
        score += 1
    elif d <= float(hero_averages[hero]["deaths"][1]):
        score += 0
    elif d <= float(hero_averages[hero]["deaths"][0]):
        score += -1
    else:
        score += -3


    if  a >= float(hero_averages[hero]["assists"][4]):
        score += 5
    elif a >= float(hero_averages[hero]["assists"][3]):
        score += 3
    elif a >= float(hero_averages[hero]["assists"][2]):
        score += 1
    elif a >= float(hero_averages[hero]["assists"][1]):
        score += 0
    elif a >= float(hero_averages[hero]["assists"][0]):
        score += -1
    else:
        score += -3

    if  gpm >= int(hero_averages[hero]["gpm"][4]):
        score += 5
    elif gpm >= int(hero_averages[hero]["gpm"][3]):
        score += 3
    elif gpm >= int(hero_averages[hero]["gpm"][2]):
        score += 1
    elif gpm >= int(hero_averages[hero]["gpm"][1]):
        score += 0
    elif gpm >= int(hero_averages[hero]["gpm"][0]):
        score += -1
    else:
        score += -3

    return score
