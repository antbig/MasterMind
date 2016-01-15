"""
    Creer par Antoine Leonard
        antoine@antbig.fr
"""
import Interface
import Resolver
import Line
import LineCreator
import PlayerInput


class Game:

    def start(self, useplayer = True):
        line = LineCreator.generatenewline(12)
        if useplayer:
            input = PlayerInput.PlayerInput(line.getnbcolor())
        else:
            input = Resolver.IA(line.getnbcolor(), line)

        print line
        correct = False

        tentative = 0

        while not correct:
            tentative += 1
            while not input.askforanswer():
                pass
            answer = input.getline()
            result = answer.compareto(line)
            stringresult = ""
            for r in result.getresult():
                stringresult += r+" "
            print answer, "(", stringresult, ")"
            correct = result.iscorrect()
            input.setResult(result)
        print "Termine en ", Line.counttry, " tentatives"

