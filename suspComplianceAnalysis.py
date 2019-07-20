from createBaseFrame import *
import numpy
import math

frame = createBaseFrame()
#frame.toString('nodes')

load = 100
which = 1; #make -1 for compression

class frontSuspLoads:
    forceApplied = [0, 0, 0, 0, 0, 0]
    nodeLoaded = [12, forceApplied]

    nodeForceCases = [nodeLoaded]

    fixedNodes = [38, 39, 40, 41, 44, 45, 46, 47]
    #fixedNodes = [5, 4, 7, 6, 9, 8,10, 11]
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
    #fixedNodes = [ 39, 38, 41, 40, 45, 44, 47, 46]
    objFuncNodes = [12]

    def updateLoadCase(self, loadCaseTuple):
        self.forceApplied = [loadCaseTuple[1][0], loadCaseTuple[1][1], loadCaseTuple[1][2],
                             loadCaseTuple[1][3], loadCaseTuple[1][4], loadCaseTuple[1][5]]
        self.nodeLoaded = [loadCaseTuple[0], self.forceApplied]
        self.nodeForceCases = [self.nodeLoaded]
        self.objFuncNodes = [loadCaseTuple[0]]
        self.name = loadCaseTuple[2]



# Format: [nodeLoaded, [x, y, z, xMom, yMom, zMom]]
frontLoadCaseInfo = [(4, [which*.4558*load, which*-.8678*load, which*.1977*load, 0, 0, 0], 'Upper-fore-left Front A-Arm'),
                     #(5, [load, load, load, 0, 0, 0], 'Upper-fore-right Front A-Arm'),
                     (6, [which*.3662*load, which*-.9273*load, which*.07768*load, 0, 0, 0], 'Lower-fore-left Front A-Arm'),
                     #(7, [load, load, load, 0, 0, 0], 'Lower-fore-right Front A-Arm'),
                     (8, [which*-.2768*load, which*-.937*load, which*.21345*load, 0, 0, 0], 'Upper-aft-left Front A-Arm'),
                     #(9, [load, load, load, 0, 0, 0], 'Upper-aft-right Front A-Arm'),
                     (10, [which*-.239*load, which*-.9676*load, which*.08112*load, 0, 0, 0], 'Lower-aft-left Front A-Arm'),
                     #(11, [load, load, load, 0, 0, 0], 'Lower-aft-right Front A-Arm'),
                     (12, [which*0*load, which*-.331*load, which*-.944*load, 0, 0, 0], 'Left Front Damper'),
                     #(13, [load, load, load, 0, 0, 0], 'Right Front Damper'),
                     (31, [which*0*load, which*-.9679*load, which*.25133*load, 0, 0, 0], 'Left Front Rocker Node')
                     #(32, [load, load, load, 0, 0, 0], 'Right Front Rocker Node')
]
rearLoadCaseInfo = [(38, [which*.5138*load, which*-.8566*load, which*.04657*load, 0, 0, 0], 'Upper-fore-left Rear A-Arm'),
                    #(39, [load, load, load, 0, 0, 0], 'Upper-fore-right Rear A-Arm'),
                    (40, [which*.4959*load, which*-.8681*load, which*-.021785*load, 0, 0, 0], 'Lower-fore-left Rear A-Arm'),
                    #(41, [load, load, load, 0, 0, 0], 'Lower-fore-right Rear A-Arm'),
                    (44, [which*-.18435*load, which*-.9826*load, which*-.0246*load, 0, 0, 0], 'Lower-aft-left Rear A-Arm'),
                    #(45, [load, load, load, 0, 0, 0], 'Lower-aft-right Rear A-Arm'),
                    (46, [which*-.2785*load, which*-.959*load, which*.0521*load, 0, 0, 0], 'Upper-aft-left Rear A-Arm'),
                    #(47, [load, load, load, 0, 0, 0], 'Upper-aft-right Rear A-Arm'),
                    (50, [which*0*load, which*-.0156*load, which*0.999*load, 0, 0, 0], 'Left Rear Rocker'),
                    #(51, [load, load, load, 0, 0, 0], 'Right Rear Rocker'),
                    (52, [which*0*load, which*-.9943*load, which*.107*load, 0, 0, 0], 'Left Rear Damper')
                    #(52, [load, load, load, 0, 0, 0], 'Right Rear Damper')]
]
front = frontSuspLoads()
rear = rearSuspLoads()

for case in frontLoadCaseInfo:
    front.updateLoadCase(case)
    frame.setLoadCase(front)
    disps = frame.getDisplacements()
    print(case[2], ":")
    print("had deflections:", disps[:,case[0]][:3])
    print("under loads:", case[1])
    totalDeflection = math.sqrt(math.pow(disps[:,case[0]][0], 2)+math.pow(disps[:,case[0]][1], 2)+math.pow(disps[:,case[0]][2], 2))
    print("Total Deflection:", totalDeflection)
    springRate = load/totalDeflection
    print("Spring Rate of Node:", springRate, "lbs/in\n")

for case in rearLoadCaseInfo:
    rear.updateLoadCase(case)
    frame.setLoadCase(rear)
    disps = frame.getDisplacements()
    print(case[2], ":")
    print("had deflections:", disps[:, case[0]][:3])
    print("under loads:", case[1])
    totalDeflection = math.sqrt(math.pow(disps[:, case[0]][0], 2) + math.pow(disps[:, case[0]][1], 2) + math.pow(disps[:, case[0]][2], 2))
    print("Total Deflection:", totalDeflection)
    springRate = load / totalDeflection
    print("Spring Rate of Node:", springRate, "lbs/in\n")
