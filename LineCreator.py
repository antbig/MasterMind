"""
    Creer par Antoine Leonard
        antoine@antbig.fr
"""
import Line
import Colors
import random


def generatenewline(nbcolor, allowdouble=False):
    line = Line.Line()
    colors = list(Colors.COLORS)
    for id in range(0, nbcolor):
        color = random.choice(colors)
        if not allowdouble:
            colors.remove(color)
        line.addcolor(color)
    return line
