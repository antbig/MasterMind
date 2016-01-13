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


    def getnbcolor(self):
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

    def getcolor(self, position):
        return self.__colors[position]

    def compareto(self, line):
        return LineResult(self, line)

    def getallcolors(self):
        return self.__colors

class LineResult:

    def __init__(self, line, compareto):
        self.__line = line
        self.__compareto = compareto
        self.__result = []
        self.__process()

    def __process(self):
        copyofcompareto = list(self.__compareto.getallcolors())
        for position in range(0, self.__line.getnbcolor()):
            if self.__line.getcolor(position) == self.__compareto.getcolor(position):
                self.__result.append("OK")
                copyofcompareto.remove(self.__line.getcolor(position))
            else:
                self.__result.append("NON")
        for position in range(0, self.__line.getnbcolor()):
            if self.__line.getcolor(position) in copyofcompareto and self.__result[position] != "OK":
                copyofcompareto.remove(self.__line.getcolor(position))
                self.__result.pop(position)
                self.__result.insert(position, "COLOR")


    def getresult(self):
        return self.__result

    def iscorrect(self):
        return len(self.__result) == self.__result.count("OK")

    def getCorrect(self):
        return self.__result.count("OK")

    def getRigthColor(self):
        return self.__result.count("COLOR")
