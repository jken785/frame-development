

from loadCases import *
from createBaseFrame import *



frame = createBaseFrame()

frame.setLoadCase(twist100)

frame.toString()


internalForces, displacements, reactions = frame.solve()

print(internalForces,'\n')
print(displacements,'\n')
print(reactions,'\n')

# inputCommand = input("Enter your command and I will do as you wish:\n")
# exec(inputCommand)






