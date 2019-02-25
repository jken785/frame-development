

from tube import *
from tubeSizes import *
from frame import *
from loadCases import *
from generateMatrices import *

frame = Frame()

frame.addNode("lower-left", 0, 0, 0)
frame.addNode("lower-right", 1, 0, 0)
frame.addNode("upper-right", 1, 1, 0)
frame.addNode("upper-left", 0, 1, 0)


frame.addTube(RD_5x35, "lower-left", "lower-right")
frame.addTube(RD_1x35, "lower-left", "upper-left")
frame.addTube(RD_1xSLD, "upper-left", "upper-right")
frame.addTube(RD_1x49, "upper-right", "lower-right")

frame.setLoadCase(twist200)

frame.toString()

q, w, e, r, t, y, u, i, o, p, a, s, d, f, g = generateMatrices(frame, True)





