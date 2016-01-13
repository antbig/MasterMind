"""
    Creer par Antoine Leonard
        antoine@antbig.fr
"""
import Colors
import Line


class PlayerInput:

    def __init__(self, nbcouleur):
        self.__nbcouleur = nbcouleur
        self.__line = Line.Line()

    def askforanswer(self):
        stringvalue = ""
        for color in Colors.COLORS:
            stringvalue += color.getdisplayname() + " "
        print "couleurs disponible : ", stringvalue
        print "Reponce :"
        return self.__processinput(raw_input())

    def __processinput(self, inputvalue):
        line = Line.Line()
        choices = inputvalue.split(" ")
        if len(choices) != self.__nbcouleur:
            print "Il faut ", self.__nbcouleur , " couleurs"
            return False
        for colorname in choices:
            color = Colors.getcolorfromname(colorname)
            if color == 0:
                print "la couleur ", colorname, " n'existe pas"
                return False
            line.addcolor(color)
        self.__line = line
        return True

    def getline(self):
        return self.__line
