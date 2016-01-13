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

COLORS = [RED, GREEN, BLUE]
