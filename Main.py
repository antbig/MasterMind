"""
    MasterMind
    par Antoine Leonard et Hakim Kebli

"""

"""
 Version avec joueur en mode console

import Game


game = Game.Game()
game.start()
"""

"""
 Version avec joueur en mode graphique


import Interface


interface = Interface.Interface()
interface.run()
"""

"""
 Version avec IA utilisant un algorithme genetique
"""
import Game
import time
import Line


amounttry = 0
start = time.clock()
for test in range(10):
    game = Game.Game()
    game.start(False)
    amounttry += Line.counttry
    Line.counttry = 0
    print "Tours ", test, "temps moyen ", (time.clock()-start)/(test+1), " Tentative moyenne ", amounttry/(test+1)

print "temps moyen ", (time.clock()-start)/(test+1), "Tentative moyenne ", amounttry/(test+1)

