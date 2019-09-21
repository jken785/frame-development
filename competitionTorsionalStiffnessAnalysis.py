
from Create2019Frame import *
from loadCases import *
import plotter


frame = createBaseFrame()
frame.toString('nodes')
# you change this
forcesOnScales = [28, 70, 109, 142]
# ---------------

for i in range(len(forcesOnScales)):

    torqueOnFrame = (55)*forcesOnScales[i] # in ft-lbs
    forceToApplyToFrameNodes = torqueOnFrame/37.4#(((6.93*2)+(8.69*2))) # based on math I have a photo of

    LoadCases.twist.forceUpUpper[2] = forceToApplyToFrameNodes
    LoadCases.twist.forceUpLower[2] = forceToApplyToFrameNodes

    LoadCases.twist.forceDownUpper[2] = -forceToApplyToFrameNodes
    LoadCases.twist.forceDownLower[2] = -forceToApplyToFrameNodes



    frame.setLoadCase(LoadCases.twist)

    displacements = frame.getDisplacements()
    displacements = displacements * -1

    print(displacements[2][7], displacements[2][19], displacements[2][25], displacements[2][41])

#plotter.plotFrame(frame, 20)
