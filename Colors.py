"""
    Creer par Antoine Leonard
        antoine@antbig.fr
"""


class Color:

    def __init__(self, name, r, g, b, id):
        self.__name = name
        self.__r = r
        self.__g = g
        self.__b = b
        self.__id = id

    def getname(self):
        return self.__name

    def getid(self):
        return self.__id

    def getdisplayname(self):
        return self.__name+ "("+ str(self.__id)+ ")"

    def __str__(self):
        return self.__name+ "("+ str(self.__id)+ ")"

RED = Color("rouge", 255, 0, 0, 1)
GREEN = Color("vert", 0, 255, 0, 2)
BLUE = Color("bleu", 0, 0, 255, 3)
YELLOW = Color("jaune", 248, 255, 1, 4)
PURPLE = Color("violet", 170, 0, 238, 5)
PINK = Color("rose", 255, 40, 255, 6)
#WHITE = Color("blanc", 255, 255, 255, 7)
#BLACK = Color("noir", 0, 0, 0, 8)


COLORS = [RED, GREEN, BLUE, YELLOW, PURPLE, PINK]

def getcolorfromname(name):
    for color in COLORS:
        if color.getname() == name or str(color.getid()) == name:
            return color
    return 0