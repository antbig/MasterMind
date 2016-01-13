"""
    Creer par Antoine Leonard
        antoine@antbig.fr
"""


class Color:

    def __init__(self, name, r, g, b):
        self.__name = name
        self.__r = r
        self.__g = g
        self.__b = b

    def getname(self):
        return self.__name

RED = Color("rouge", 255, 0, 0)
GREEN = Color("vert", 0, 255, 0)
BLUE = Color("bleu", 0, 0, 255)
YELLOW = Color("jaune", 248, 255, 1)
PURPLE = Color("violet", 170, 0, 238)
PINK = Color("rose", 255, 40, 255)
WHITE = Color("blanc", 255, 255, 255)
BLACK = Color("noir", 0, 0, 0)


COLORS = [RED, GREEN, BLUE, YELLOW, PURPLE, PINK, WHITE, BLACK]
