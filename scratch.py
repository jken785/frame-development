

from loadCases import *
import loadCases
from createBaseFrame import *

import copy

import matplotlib.pyplot as plt


fig = plt.figure()
ax1 = fig.add_subplot(221, title="Score/Weight vs Iters")
ax2 = fig.add_subplot(222, title="Avg Displacement vs Iters")
ax3 = fig.add_subplot(223, title="Weight vs Iters")
fig.subplots_adjust(hspace=0.2, wspace=0.2)
ax1.grid()
ax2.grid()
ax3.grid()


iters = 25000
maxScorePerWeight = 0
maxScoresPerWeight = []
weights = []
averageDisps = []
times = []
iterations = []
averageDisp = 0
maxScore = 0
numRandTubes = 5
maxFrame = createBaseFrame()
tolerance = 0.0000001

baseFrame = createBaseFrame()
baseFrameScore = baseFrame.solveAllLoadCases()
print("\nBase Frame Weight:", baseFrame.weight)
print("\nBase Frame Score:", baseFrameScore)
baseFrameScorePerWeight, _, baseFrameAvgDisp = baseFrame.solveAllLoadCases()
maxScoresPerWeight.append(baseFrameScorePerWeight)
weights.append(baseFrame.weight)
averageDisps.append(baseFrameAvgDisp)
iterations.append(0)

for i in range(1, iters):
    frame = copy.deepcopy(maxFrame)
    for j in range(numRandTubes):
        frame.randomizeThicknessOfRandomTube()
    scorePerWeight, score, avgDisp = frame.solveAllLoadCases()

    if maxScorePerWeight < (scorePerWeight - tolerance):
        maxScorePerWeight = scorePerWeight
        maxScore = score
        averageDisp = avgDisp
        maxFrame = frame
        print("\n")
        maxFrame.toString()
        print("Max Score Per Weight:\t", maxScorePerWeight)
        print("Avg Disp. of Target Nodes:\t", averageDisp)
    if i % 10 is 0:
        ax1.plot(iterations, maxScoresPerWeight)
        ax2.plot(iterations, averageDisps)
        ax3.plot(iterations, weights)
        plt.pause(0.001)
    maxScoresPerWeight.append(maxScorePerWeight)
    averageDisps.append(averageDisp)
    iterations.append(i)
    weights.append(maxFrame.weight)


plt.show()
maxFrame.plot(25)

print('FINISHED')
# inputCommand = input("Enter your command and I will do as you wish:\n")
# exec(inputCommand)






