"""
    Creer par Antoine Leonard
        antoine@antbig.fr
"""
import Line
import Colors
import random


def generatenewline(nbcolor):
    line = Line.Line()
    for color in range(0, nbcolor):
        line.addcolor(random.choice(Colors.COLORS))
    return line
