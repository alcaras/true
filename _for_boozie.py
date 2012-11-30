from hero_averages import *

for k, v in hero_averages.iteritems():
    i = 0
    print k + ",",
    for y in [v["kills"], v["deaths"], v["assists"], v["gpm"]]:
        for z in y:
            print z + ",",

    print

    

