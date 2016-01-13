"""
    MasterMind
    par Antoine Leonard et Hakim Kebli

"""
import Colors
import PlayerInput
import Line


line = Line.Line()

line.addcolor(Colors.RED)
line.addcolor(Colors.GREEN)
line.addcolor(Colors.RED)
line.addcolor(Colors.BLUE)

input = PlayerInput.PlayerInput(line.getnbcolor())
while not input.askforanswer():
    pass
answer = input.getline()

print line
print answer
result = answer.compareto(line)
stringresult = ""
for r in result.getresult():
    stringresult += r+" "
print stringresult
