"""
    Creer par Antoine Leonard
        antoine@antbig.fr
"""
import pygame
import Colors
import Line
import LineCreator


class Circle:
    def __init__(self, color, pos, size):
        self.color = color
        self.pos = pos
        self.oldposition = pos
        self.size = size
        self.__lock = False

    def Render(self, screen):
        pygame.draw.circle(screen, self.color.getcolor(), self.pos, self.size)

    def lock(self):
        self.__lock = True

    def islock(self):
        return self.__lock

    def getcolor(self):
        return self.color

class Essai:

    def __init__(self, bien_place=0, mal_place=0, combinaison = []):

        self.combinaison = combinaison
        self.bien_place = bien_place
        self.mal_place = mal_place

    def __str__(self):
        return "{} ({}, {}, {})".format(str(self.combinaison), self.bien_place, self.mal_place, self.score)

class Interface():

    def __init__(self):
        pygame.init()
        self.__fenetre = pygame.display.set_mode((300, 600))
        self.__loop = True
        self.__clock = pygame.time.Clock()
        self.__answer = LineCreator.generatenewline(4)
        self.__essais = []
        self.__background = pygame.Surface(self.__fenetre.get_size())
        self.__myfont = pygame.font.SysFont('Arial', 15)

        pygame.display.flip()

    def run(self):
        staticcircle=[]
        movableccircle=[]
        actualline = []
        actualy = 10*44
        x = 44
        y = 11*44

        for color in Colors.COLORS:
            circle = Circle(color, (x-22, y-22), 18)
            x += 44
            movableccircle.append(circle)


        while self.__loop:
            self.__fenetre.fill((0, 0, 0)) # clear screen
            self.displayBackground()
            valideline = pygame.draw.rect(self.__fenetre, (0, 0, 0), (5*44-30, actualy-35, 30, 30), 2)
            pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__loop = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for item in movableccircle:
                        if (pos[0]>=(item.pos[0]-item.size) and pos[0]<=(item.pos[0]+item.size) and pos[1]>=(item.pos[1]-item.size) and  pos[1]<=(item.pos[1]+item.size)):
                            print "click on circle ", item.getcolor()
                            if len(actualline) < 4:
                                movableccircle.remove(item)
                                actualline.append(item)
                                item.pos = (len(actualline)*44-22, actualy-22)
                    for item in actualline:
                        if (pos[0]>=(item.pos[0]-item.size) and pos[0]<=(item.pos[0]+item.size) and pos[1]>=(item.pos[1]-item.size) and  pos[1]<=(item.pos[1]+item.size)):
                            pass
                    

                    if valideline.collidepoint(pos) and len(actualline) == 4:
                        print "click on valid"
                        actualy -= 44
                        line = Line.Line()
                        for item in actualline:
                            staticcircle.append(item)
                            line.addcolor(item.getcolor())
                        del actualline[:]
                        del movableccircle[:]
                        x = 44
                        y = 11*44
                        for color in Colors.COLORS:
                            circle = Circle(color, (x-22, y-22), 18)
                            x += 44
                            movableccircle.append(circle)
                        result = line.compareto(self.__answer)
                        essai = Essai(result.getCorrect(), result.getRigthColor(), line)
                        self.__essais.append(essai)

            for item in staticcircle:
                item.Render(self.__fenetre)
            for item in movableccircle:
                item.Render(self.__fenetre)
            for item in actualline:
                item.Render(self.__fenetre)
            e = 0
            for essai in self.__essais:
                label = self.__myfont.render("Bien place: {}".format(essai.bien_place), 1, (255, 255, 0))
                self.__fenetre.blit(label, (44*4+10, 10*44-44*e-40))
                label2 = self.__myfont.render("Mal place: {}".format(essai.mal_place), 1, (255, 255, 0))
                self.__fenetre.blit(label2, (44*4+10, 10*44-44*e-20))
                pygame.draw.line(self.__fenetre, (0, 0, 0), (44*4, 10*44-44*e), (44*6, 10*44-44*e))
                e += 1
            pygame.display.flip()
            self.__clock.tick(100)

    def displayBackground(self):
        self.__background.fill((72, 131, 151))
        self.__fenetre.blit(self.__background, (0, 0))
        for col in range(4):
            pygame.draw.line(self.__fenetre, (0, 0, 0), (44+44*col, 0), (44+44*col, 44*10))
        for li in range(10):
            pygame.draw.line(self.__fenetre, (0, 0, 0), (0, 44+44*li), (44*4, 44+44*li))