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
        self.__partie = []

    def askforanswer(self):
        if self.__firstTry:
            self.line = Line.Line()
            self.line.addcolor(Colors.COLORS[0])
            self.line.addcolor(Colors.COLORS[0])
            self.line.addcolor(Colors.COLORS[0])
            self.line.addcolor(Colors.COLORS[0])
            self.__firstTry = False
        return True

    def setResult(self, result):
        non = result.getNON()
        ok = result.getCorrect()
        color = result.getRigthColor()
        oldLine = self.line;
        newline = Line.Line()
        #DEBUT du traitement


        #Fin du traitement
        self.line = newline

    def getNextMove(self, oldmove):
        move = list(oldmove)
        move[-1] += 1
        for i in range(self.nbcolor, 0, -1):
            if move[i] == len(Colors.COLORS):
                move[i] = 0
                move[i-1] += 1
        return move

    def getcorrection(self, ):
        pass


class essai:

    def __init__(self,bien_place=0,mal_place=0,score=0,combinaison=[]):

        self.combinaison = combinaison
        self.bien_place = bien_place
        self.mal_place = mal_place
        self.score = score