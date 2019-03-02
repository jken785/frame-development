

from loadCases import *
import loadCases
from createBaseFrame import *
from objectiveFunction import *
import math

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


iters = 5000
maxScorePerWeight = 0
maximumDisp = 0
maxScore = 0
maxFrame = None
tolerance = 0.0001

baseFrame = createBaseFrame()
baseFrameScore = baseFrame.solveAllLoadCases()
print("\nBase Frame Weight:", baseFrame.weight)
print("\nBase Frame Score:", baseFrameScore)

for i in range(iters):
    frame = createBaseFrame()
    frame.randomizeAllThicknesses()
    scorePerWeight, score, maxDisp = frame.solveAllLoadCases()
    if maxScorePerWeight < (scorePerWeight - tolerance):
        maxScorePerWeight = scorePerWeight
        maxScore = score
        maximumDisp = maxDisp
        maxFrame = frame
    if i % 100 is 0 and i is not 0:
        print("\nAfter", i,"iterations:")
        maxFrame.toString()
        print("Max Score Per Weight:\t",maxScorePerWeight)
        print("Max Score (just displacement):\t", maxScore)
        print("Max Displacement:\t", maximumDisp)


maxFrame.plot(25)

print(scores)
print(weights)
print('FINISHED')
# inputCommand = input("Enter your command and I will do as you wish:\n")
# exec(inputCommand)






