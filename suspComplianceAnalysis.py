from createBaseFrame import *
import numpy
import math

frame = createBaseFrame()
#frame.toString('nodes')

load = 200
magnitude = math.sqrt(3*(math.pow(load, 2)))

class frontSuspLoads:
    forceApplied = [0, 0, 0, 0, 0, 0]
    nodeLoaded = [12, forceApplied]

    nodeForceCases = [nodeLoaded]

    fixedNodes = [38, 39, 40, 41, 44, 45, 46, 47]

    objFuncNodes = [12]

    def updateLoadCase(self, loadCaseTuple):
        self.forceApplied = [loadCaseTuple[1][0], loadCaseTuple[1][1], loadCaseTuple[1][2],
                             loadCaseTuple[1][3], loadCaseTuple[1][4], loadCaseTuple[1][5]]
        self.nodeLoaded = [loadCaseTuple[0], self.forceApplied]
        self.nodeForceCases = [self.nodeLoaded]
        self.objFuncNodes = [loadCaseTuple[0]]
        self.name = loadCaseTuple[2]

class rearSuspLoads:
    forceApplied = [0, 0, 0, 0, 0, 0]
    nodeLoaded = [12, forceApplied]

    nodeForceCases = [nodeLoaded]

    fixedNodes = [4, 5, 6, 7, 8, 9, 10, 11]

    objFuncNodes = [12]

    def updateLoadCase(self, loadCaseTuple):
        self.forceApplied = [loadCaseTuple[1][0], loadCaseTuple[1][1], loadCaseTuple[1][2],
                             loadCaseTuple[1][3], loadCaseTuple[1][4], loadCaseTuple[1][5]]
        self.nodeLoaded = [loadCaseTuple[0], self.forceApplied]
        self.nodeForceCases = [self.nodeLoaded]
        self.objFuncNodes = [loadCaseTuple[0]]
        self.name = loadCaseTuple[2]



# Format: [nodeLoaded, [x, y, z, xMom, yMom, zMom]]
frontLoadCaseInfo = [(4, [load, load, load, 0, 0, 0], 'Upper-fore-left Front A-Arm'),
                     #(5, [load, load, load, 0, 0, 0], 'Upper-fore-right Front A-Arm'),
                     (6, [load, load, load, 0, 0, 0], 'Lower-fore-left Front A-Arm'),
                     #(7, [load, load, load, 0, 0, 0], 'Lower-fore-right Front A-Arm'),
                     (8, [load, load, load, 0, 0, 0], 'Upper-aft-left Front A-Arm'),
                     #(9, [load, load, load, 0, 0, 0], 'Upper-aft-right Front A-Arm'),
                     (10, [load, load, load, 0, 0, 0], 'Lower-aft-left Front A-Arm'),
                     #(11, [load, load, load, 0, 0, 0], 'Lower-aft-right Front A-Arm'),
                     (12, [load, load, load, 0, 0, 0], 'Left Front Damper'),
                     #(13, [load, load, load, 0, 0, 0], 'Right Front Damper'),
                     (31, [load, load, load, 0, 0, 0], 'Left Front Rocker Node')]
                     #(32, [load, load, load, 0, 0, 0], 'Right Front Rocker Node')

rearLoadCaseInfo = [(38, [load, load, load, 0, 0, 0], 'Upper-fore-left Rear A-Arm'),
                    #(39, [load, load, load, 0, 0, 0], 'Upper-fore-right Rear A-Arm'),
                    (40, [load, load, load, 0, 0, 0], 'Lower-fore-left Rear A-Arm'),
                    #(41, [load, load, load, 0, 0, 0], 'Lower-fore-right Rear A-Arm'),
                    (44, [load, load, load, 0, 0, 0], 'Lower-aft-left Rear A-Arm'),
                    #(45, [load, load, load, 0, 0, 0], 'Lower-aft-right Rear A-Arm'),
                    (46, [load, load, load, 0, 0, 0], 'Upper-aft-left Rear A-Arm'),
                    #(47, [load, load, load, 0, 0, 0], 'Upper-aft-right Rear A-Arm'),
                    (50, [load, load, load, 0, 0, 0], 'Left Rear Rocker'),
                    #(51, [load, load, load, 0, 0, 0], 'Right Rear Rocker'),
                    (52, [load, load, load, 0, 0, 0], 'Left Rear Damper')]
                    #(52, [load, load, load, 0, 0, 0], 'Right Rear Damper')]

front = frontSuspLoads()
rear = rearSuspLoads()

for case in frontLoadCaseInfo:
    front.updateLoadCase(case)
    frame.setLoadCase(front)
    disps = frame.getDisplacements()
    print(case[2], ":")
    print("had deflections:", disps[:,case[0]][:3])
    print("under loads:", case[1], "\n")

for case in rearLoadCaseInfo:
    rear.updateLoadCase(case)
    frame.setLoadCase(rear)
    disps = frame.getDisplacements()
    print(case[2], ":")
    print("had deflections:", disps[:, case[0]][:3])
    print("under loads:", case[1], "\n")



