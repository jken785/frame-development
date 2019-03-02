from tubeSizes import *
from frame import *

def createBaseFrame():

    frame = Frame()

    frame.addNode("upper-left-bulkhead", 17.852, -6.929, 17.195, True, True)
    frame.addNode("lower-left-bulkhead", 17.852, -6.929, 4.82, True, True)
    frame.addNode("upper-fore-left-frontbox", 33.203, -8.69, 8.932, True, True)
    frame.addNode("lower-fore-left-frontbox", 33.652, -6.929, 4.82, True, True)
    frame.addNode("upper-aft-left-frontbox", 44.194, -8.584, 8.907, True, True)
    frame.addNode("lower-aft-left-frontbox", 43.97, -6.929, 4.82, True, True)
    frame.addNode("left-frontdamper", 40.2, -9, 17.25, True, True)
    frame.addNode("fore-upper-left-sideimpact", 44.731, -8.497, 12.5, True, True, 4, 0, 1, 2, 0, 0)
    frame.addNode("upper-left-fronthoop", 46.445, -6.53, 23.133, True, True, 3, 2, 1, 3, 1, 1)
    frame.addNode("mid-upper-left-sideimpact", 58.353, -10.751, 12.737, True, False, 5, 5, 2, 6, 0, 0)
    frame.addNode()







    return frame