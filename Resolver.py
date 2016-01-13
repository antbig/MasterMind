"""
    Creer par Antoine Leonard
        antoine@antbig.fr
"""
import PlayerInput
import LineCreator
import Line
import Colors


class IA(PlayerInput.PlayerInput):

    def __init__(self, nbcolor, doublon=False):
        super(IA, self).__init__(nbcolor)
        self.__doublon = doublon
        self.__firstTry = True

    def askforanswer(self):
        if self.__firstTry:
            self.line = LineCreator.generatenewline(self.nbcolor)
            self.__firstTry = False
        return True

    def setResult(self, result):
        non = result.getNON()
        ok = result.getCorrect()
        color = result.getRigthColor()
        oldLine = self.line;
        newline = Line.Line()
        #DEBUT du traitement
        newline.addcolor(Colors.BLUE)

        #Fin du traitement
        self.line = newline