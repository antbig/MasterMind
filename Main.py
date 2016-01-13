"""
    MasterMind
    par Antoine Leonard et Hakim Kebli

"""
import LineCreator
import PlayerInput


line = LineCreator.generatenewline(6)

input = PlayerInput.PlayerInput(6)
while not input.askforanswer():
    pass
answer = input.getline()

print line
print answer

"""
response = raw_input()
choices = response.split(" ")
if len(choices) != 6:
    print "Il faut 6 couleurs"
print len(choices)
"""