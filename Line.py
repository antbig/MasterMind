"""
    Creer par Antoine Leonard
        antoine@antbig.fr

    Class qui contient une ligne de couleur
"""


class Line:

    def __init__(self):
        self.__colors = []

    def addcolor(self,color):
        self.__colors.append(color)


    def getnbcolors(self):
        return len(self.__colors)

    def hascolor(self, color):
        return color in self.__colors

    def iscoloratposition(self, color, position):
        if position >= len(self.__colors):
            return False
        return self.__colors[position] == color

    def __str__(self):
        stringvalue = ""
        for color in self.__colors:
            stringvalue += (color.getname()+" ")
        return stringvalue
