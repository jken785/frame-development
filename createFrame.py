from tubeSizes import *
from frame import *
from createBaseFrame import *

def createFrame():

    baseFrame = createBaseFrame()
    frame = Frame()


    # Copy and paste the simulation-generated frame .txt file here:
    # -------------------------------------------------------------


    # -------------------------------------------------------------

    for node in frame.nodes:
        for baseNode in baseFrame.nodes:
            if node.name is baseNode.name:
                node.xOrig = baseNode.xOrig
                node.yOrig = baseNode.yOrig
                node.zOrig = baseNode.zOrig

    return frame