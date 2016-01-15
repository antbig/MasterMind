"""
    Creer par Antoine Leonard
        antoine@antbig.fr
"""
import PlayerInput
import LineCreator
import Line
import Colors
import random


class IA(PlayerInput.PlayerInput):

    def __init__(self, nbcolor, answer, doublon=False):
        super(IA, self).__init__(nbcolor)
        self.__doublon = doublon
        self.__firstTry = True
        self.__partie = []
        self.__population = []
        self.__answer = answer
        self.__generatePopulation()
        result = 0
        round = 0
        while result == 0:
            round += 1
            self.__generateChildren()
            result = self.__population[0].bien_place == nbcolor
            #print "Generation enfant tours ", round
        print(self.__population[0])

    def __generatePopulation(self):
        while len(self.__population) < 40:
            line = LineCreator.generatenewline(self.nbcolor)
            result = line.compareto(self.__answer)
            essai = Essai(result.getCorrect(), result.getRigthColor(), 5*result.getCorrect()+result.getRigthColor(), line)
            if self.__population.count(essai) == 0:
                self.__population.append(essai)
        self.__population.sort(key=lambda x: x.score, reverse=True)
        #for essai in self.__population:
        #    print essai

    def __generateChildren(self):
        self.__population = self.__population[0:20]
        parents = list(self.__population)
        while len(parents) > 0:
            father = random.choice(parents)
            parents.remove(father)
            father = father.combinaison
            mother = random.choice(parents)
            parents.remove(mother)
            mother = mother.combinaison
            splitid = random.choice(range(self.nbcolor))
            children1 = Line.Line()
            children2 = Line.Line()
            for id in range(self.nbcolor):
                if id < splitid:
                    children1.addcolor(father.getcolor(id))
                    children2.addcolor(mother.getcolor(-id))
                else:
                    children1.addcolor(mother.getcolor(id))
                    children2.addcolor(father.getcolor(-id))
            result1 = children1.compareto(self.__answer)
            essai1 = Essai(result1.getCorrect(), result1.getRigthColor(), 5*result1.getCorrect()+result1.getRigthColor(), children1)
            result2 = children2.compareto(self.__answer)
            essai2 = Essai(result2.getCorrect(), result2.getRigthColor(), 5*result2.getCorrect()+result2.getRigthColor(), children2)
            if essai1 not in self.__population:
                self.__population.append(essai1)
            if essai2 not in self.__population:
                self.__population.append(essai2)
        self.__population.sort(key=lambda x: x.score, reverse=True)

    def askforanswer(self):
        if self.__firstTry:
            self.line = self.__population[0].combinaison
            self.__firstTry = False
        return True

    def setResult(self, result):
        pass

    def getNextMove(self, oldmove):
        move = list(oldmove)
        move[-1] += 1
        for i in range(self.nbcolor, 0, -1):
            if move[i] == len(Colors.COLORS):
                move[i] = 0
                move[i-1] += 1
        return move

    def getcorrection(self, ):
        pass


class Essai:

    def __init__(self,bien_place=0,mal_place=0,score=0,combinaison=[]):

        self.combinaison = combinaison
        self.bien_place = bien_place
        self.mal_place = mal_place
        self.score = score

    def __str__(self):
        return "{} ({}, {}, {})".format(str(self.combinaison), self.bien_place, self.mal_place, self.score)