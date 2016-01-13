"""
    Creer par Antoine Leonard
        antoine@antbig.fr
"""
import Colors
import Line


class PlayerInput(object):

    def __init__(self, nbcolor):
        self.nbcolor = nbcolor
        self.line = Line.Line()

    def askforanswer(self):
        stringvalue = ""
        for color in Colors.COLORS:
            stringvalue += color.getdisplayname() + " "
        print "couleurs disponible : ", stringvalue
        print "Reponce (", self.nbcolor, ") :"
        return self.__processinput(raw_input())

    def setResult(self, result):
        pass

    def __processinput(self, inputvalue):
        line = Line.Line()
        choices = inputvalue.split(" ")
        if len(choices) != self.nbcolor:
            print "Il faut ", self.nbcolor , " couleurs"
            return False
        for colorname in choices:
            color = Colors.getcolorfromname(colorname)
            if color == 0:
                print "la couleur ", colorname, " n'existe pas"
                return False
            line.addcolor(color)
        self.line = line
        return True

    def getline(self):
        return self.line
