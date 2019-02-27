from tubeSizes import *
from frame import *

def createBaseFrame():
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

    return frame