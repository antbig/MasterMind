"""
    Creer par Antoine Leonard
        antoine@antbig.fr
"""
import PlayerInput
import LineCreator


class IA(PlayerInput.PlayerInput):

    def __init__(self, nbcolor, doublon=False):
        super(IA, self).__init__(nbcolor)
        self.__doublon = doublon

    def askforanswer(self):
        self.line = LineCreator.generatenewline(self.nbcolor)
        return True

    def setResult(self, result):
        pass