from tubeSizes import *
from frame import *

def createBaseFrame():
    frame = Frame()

    frame.addNode("lower-left", 3, 3, 3, True)
    frame.addNode("lower-right", 2, 4.5, 6, True)
    frame.addNode("anotherOne", 3, 4, 17, True)

    frame.addTube(RD_1x35, RD_5x35, "lower-left", "lower-right", True)
    frame.addTube(RD_1xSLD, RD_1x49, "lower-right", "anotherOne", True)



    return frame