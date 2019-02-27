

from tube import *
from tubeSizes import *
from frame import *
from loadCases import *
from generateMatrices import *
from timeit import default_timer as timer

frame = Frame()

frame.addNode("lower-left", 0, 0, 0)
frame.addNode("lower-right", 1, 0, -1)
frame.addNode("upper-right", 1, 1, 0)
frame.addNode("upper-left", 0, 1, 1)
frame.addNode("outlier", 12, 13.45, 12)
frame.addNode("anotherOut", -2.3, 3.5, 6.7)


frame.addTube(RD_1x49, "lower-left", "lower-right")
frame.addTube(RD_1x49, "lower-left", "upper-left")
frame.addTube(RD_1x49, "upper-left", "upper-right")
frame.addTube(RD_1x49, "upper-right", "lower-right")
frame.addTube(RD_1x49, "lower-left", "outlier")
frame.addTube(RD_1x49, "outlier", "lower-right")
frame.addTube(RD_1x49, "outlier", "upper-left")
frame.addTube(RD_75x49, "lower-left", "anotherOut")
frame.addTube(RD_75x49, "anotherOut", "outlier")

frame.setLoadCase(twist100)

frame.toString()


start = timer()

internalForces, displacements, reactions = frame.solve()

print(internalForces,'\n')
print(displacements,'\n')
print(reactions,'\n')

end = timer()
print(end - start)


# inputCommand = input("Enter your command and I will do as you wish:\n")
# exec(inputCommand)

# q, w, e, r, t, y, u, i, o, p, a, s, d, f, g = generateMatrices(frame, True)





