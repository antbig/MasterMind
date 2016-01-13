"""
    MasterMind
    par Antoine Leonard et Hakim Kebli

"""
import Colors
import Resolver
import Line


line = Line.Line()

line.addcolor(Colors.BLACK)
line.addcolor(Colors.GREEN)
line.addcolor(Colors.RED)
line.addcolor(Colors.BLUE)

input = Resolver.IA(line.getnbcolor())

print line
correct = False

tentative = 0

while not correct:
    tentative += 1
    while not input.askforanswer():
        pass
    answer = input.getline()
    result = answer.compareto(line)
    stringresult = ""
    for r in result.getresult():
        stringresult += r+" "
    print answer, "(", stringresult, ")"
    correct = result.iscorrect()
    input.setResult(result)
print "Termine en ", str(tentative), " tentatives"
