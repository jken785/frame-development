

from tube import *
from tubeSizes import *
from frame import *
from loadCases import *
from generateMatrices import *

frame = Frame()

frame.addNode("lower-left", 0, 0, 0)
frame.addNode("lower-right", 1, 0, -1)
frame.addNode("upper-right", 1, 1, 0)
frame.addNode("upper-left", 0, 1, 1)


frame.addTube(RD_1x49, "lower-left", "lower-right")
frame.addTube(RD_1x49, "lower-left", "upper-left")
frame.addTube(RD_1x49, "upper-left", "upper-right")
frame.addTube(RD_1x49, "upper-right", "lower-right")

frame.setLoadCase(twist100)

frame.toString()

internalForces, displacements, reactions = frame.solve()
print(internalForces)
print(displacements)
print(reactions)


# inputCommand = input("Enter your command and I will do as you wish:\n")
# exec(inputCommand)

# q, w, e, r, t, y, u, i, o, p, a, s, d, f, g = generateMatrices(frame, True)





