import random
import numpy as np
from node import *
import generateMatrices
from solver import *
from generateMatrices import *
from objectiveFunction import *
from plotter import *
from loadCases import *
from math import *


class Frame:

    def __init__(self):
        self.tubes = []
        self.nodes = []
        self.geometryOptNodes = []
        self.torStiffness = None
        self.weight = None
        self.internalForces = None
        self.displacements = None
        self.reactions = None
        # Should have a list of the required nodes, which should be the only nodes
        # accessed by loadCases/objectiveFunction b/c it wont be possible to remove them

    def computeTorStiffness(self):
        frontUpperLeftAArmNodeFore = 4
        frontUpperLeftAArmNodeAft = 8
        frontLowerLeftAArmNodeFore = 6
        frontLowerLeftAArmNodeAft = 10

        nodeToMeasureStiffnessAt = 8

        # Z height of center of rotation, located along car's centerline
        zCenter = 10

        # How close the two radii should be for while-loop end condition
        finalTolerance = 0.001

        y = self.nodes[nodeToMeasureStiffnessAt].y
        z = self.nodes[nodeToMeasureStiffnessAt].z
        radius = sqrt(pow(y, 2) + pow(z - zCenter, 2))
        displacedY = y + self.displacements[1][nodeToMeasureStiffnessAt]
        displacedZ = z + self.displacements[2][nodeToMeasureStiffnessAt]
        displacedRadius = sqrt(pow(displacedY, 2) + pow(displacedZ - zCenter, 2))

        if abs(y) > abs(displacedY) and abs(z) > abs(displacedZ):
            while abs(displacedRadius - radius) > finalTolerance:
                if displacedRadius > radius:
                    zCenter -= finalTolerance / 2
                else:
                    zCenter += finalTolerance / 2
                radius = sqrt(pow(y, 2) + pow(z - zCenter, 2))
                displacedRadius = sqrt(pow(displacedY, 2) + pow(displacedZ - zCenter, 2))
        else:
            while abs(displacedRadius - radius) > finalTolerance:
                if displacedRadius < radius:
                    zCenter -= finalTolerance / 2
                else:
                    zCenter += finalTolerance / 2
                radius = sqrt(pow(y, 2) + pow(z - zCenter, 2))
                displacedRadius = sqrt(pow(displacedY, 2) + pow(displacedZ - zCenter, 2))
        print("Center at z = ", zCenter, "inches")

        distBetweenNodeBeforeAndAfterDisp = sqrt(pow(y - displacedY, 2) + pow(z - displacedZ, 2))
        angle = 2 * degrees(asin((distBetweenNodeBeforeAndAfterDisp / 2) / radius))

        # Assumes couple moment
        torque = 2 * LoadCases.twist.forceUpUpper[2] * self.nodes[frontUpperLeftAArmNodeFore].y
        torque += 2 * LoadCases.twist.forceUpUpper[2] * self.nodes[frontUpperLeftAArmNodeAft].y
        torque += 2 * LoadCases.twist.forceUpLower[2] * self.nodes[frontLowerLeftAArmNodeFore].y
        torque += 2 * LoadCases.twist.forceUpLower[2] * self.nodes[frontLowerLeftAArmNodeAft].y

        torStiffness = (torque * 0.112984)
        torStiffness /= angle

        self.torStiffness = abs(torStiffness)

    def getDisplacements(self):
        numTubes, numNodes, coord, con, fixtures, loads, dist, E, G, areas, I_y, I_z, J, St, be = generateMatrices(self, False)
        _, displacements, _ = Solver(numTubes, numNodes, coord, con, fixtures, loads, dist, E, G, areas, I_y, I_z, J, St, be)
        return displacements

    def solveAllLoadCases(self, weightMultiplier):
        scorePerWeight = 0
        avgDisps = []
        allTargetNodeDisps = []
        for loadCase in LoadCases.listLoadCases:
            self.setLoadCase(loadCase)
            scorePerWeightToAdd, dispList, avgDisplacement = self.solve(weightMultiplier)
            if loadCase is LoadCases.twist:
                self.computeTorStiffness()
            scorePerWeight += scorePerWeightToAdd
            avgDisps.append(avgDisplacement)
            for disp in dispList:
                allTargetNodeDisps.append(disp)
        avgDisp = sum(avgDisps)/len(avgDisps)
        return scorePerWeight, allTargetNodeDisps, avgDisp

    def solve(self, weightMultiplier):
        numTubes, numNodes, coord, con, fixtures, loads, dist, E, G, areas, I_y, I_z, J, St, be = generateMatrices(self, False)
        internalForces, displacements, reactions = Solver(numTubes, numNodes, coord, con, fixtures, loads, dist, E, G, areas, I_y, I_z, J, St, be)
        self.internalForces = internalForces
        self.displacements = displacements
        self.reactions = reactions
        scorePerWeight, dispList, maxDisp = ObjectiveFunction(self, self.loadCase, weightMultiplier)
        return scorePerWeight, dispList, maxDisp

    def setLoadCase(self, loadCase):
        for node in self.nodes:
            node.setFixtures(0, 0, 0, 0, 0, 0)
            node.setForcesApplied(0, 0, 0, 0, 0, 0)
        for i in range(loadCase.nodeForceCases.__len__()):
            forceCase = loadCase.nodeForceCases.__getitem__(i)
            forces = forceCase.__getitem__(forceCase.__len__() - 1)
            x = forces.__getitem__(0)
            y = forces.__getitem__(1)
            z = forces.__getitem__(2)
            xMom = forces.__getitem__(3)
            yMom = forces.__getitem__(4)
            zMom = forces.__getitem__(5)
            for j in range(forceCase.__len__() - 1):
                index = forceCase.__getitem__(j)
                self.nodes.__getitem__(index).setForcesApplied(x, y, z, xMom, yMom, zMom)
        for index in loadCase.fixedNodes:
            self.nodes.__getitem__(index).setFixtures(1, 1, 1, 1, 1, 1)
        self.loadCase = loadCase

    def setFixtures(self, nodeIndex, x, y, z, xMom, yMom, zMom):
        fixNode = self.nodes.__getitem__(nodeIndex)
        fixNode.setFixtures(x, y, z, xMom, yMom, zMom)

    def getSymmetricTube(self, tube):
        if tube.nodeFrom.name.endswith("#m") and tube.nodeTo.name.endswith("#m"):
            symNodeFrom = tube.nodeFrom.name.split("#m")[0]
            symNodeTo = tube.nodeTo.name.split("#m")[0]
        else:
            symNodeFrom = tube.nodeFrom.name + "#m"
            symNodeTo = tube.nodeTo.name + "#m"
        for searchTube in self.tubes:
            if searchTube.nodeFrom.name == symNodeFrom and searchTube.nodeTo.name == symNodeTo:
                return searchTube
        return None

    def getSymmetricNode(self, node):
        if node.name.endswith("#m"):
            symName = node.name.split("#m")[0]
        else:
            symName = node.name + "#m"
        for searchNode in self.nodes:
            if searchNode.name == symName:
                return searchNode
        return None


    def changeTubeThickness(self, index, size):
        tube = self.tubes.__getitem__(index)
        tube.changeThickness(size)
        if tube.isSymmetric:
            symTube = self.getSymmetricTube(tube)
            symTube.changeThickness(size)
        if tube.group is not None:
            for testTube in self.tubes:
                if testTube.group is tube.group:
                    testTube.changeThickness(size)
        self.getWeight()

    def randomizeThicknessOfRandomTube(self):
        randTube = random.choice(self.tubes)
        index = self.tubes.index(randTube)
        if randTube.isRound and randTube.size is not RD_1xSLD:
            sizeIndex = allRoundSizes.index(randTube.minSize)
            availableSizes = allRoundSizes[sizeIndex:len(allRoundSizes)]
            thickness = random.choice(availableSizes)
            self.changeTubeThickness(index, thickness)

    # will not allow changes to square tubes
    def randomizeThickness(self, index):
        tube = self.tubes.__getitem__(index)
        if tube.isRound and tube.size is not RD_1xSLD:
            sizeIndex = allRoundSizes.index(tube.minSize)
            availableSizes = allRoundSizes[sizeIndex:len(allRoundSizes)]
            thickness = random.choice(availableSizes)
            self.changeTubeThickness(index, thickness)

    # optimization: should only randomize one tube in each symmetric pair -- also maybe implement lists of the symmetric
    # pair to prevent repeat look-ups
    def randomizeAllThicknesses(self):
        for i in range(len(self.tubes)):
            self.randomizeThickness(i)

    def changeNodeLocation(self, index, x, y, z):
        node = self.nodes.__getitem__(index)
        deltaX = x - node.x
        node.changeLocation(x, y, z)
        if node.isSymmetric:
            symNode = self.getSymmetricNode(node)
            symNode.changeLocation(x, -y, z)
        if node.hasXGroup:
            for xGroupNode in self.geometryOptNodes:
                if xGroupNode.hasXGroup:
                    if xGroupNode.xGroup == node.xGroup:
                        xGroupNode.x += deltaX
        for tube in self.tubes:
            tube.length = tube.getLength(tube.nodeFrom, tube.nodeFrom)
            tube.weight = tube.getWeight(tube.length)
        self.getWeight()

    def randomizeLocationOfRandomNode(self):
        yOnCenterline = False
        node = random.choice(self.geometryOptNodes)
        index = self.nodes.index(node)
        xPos = node.xOrig + node.maxXPosDev
        xNeg = node.xOrig - node.maxXNegDev
        if node.yOrig is 0:
            yOnCenterline = True
        else:
            yPos = node.yOrig + node.maxYPosDev
            yNeg = node.yOrig - node.maxYNegDev
        zPos = node.zOrig + node.maxZPosDev
        zNeg = node.zOrig - node.maxZNegDev

        newX = random.uniform(xNeg, xPos)
        if yOnCenterline:
            newY = 0
        else:
            newY = random.uniform(yNeg, yPos)
        newZ = random.uniform(zPos, zNeg)

        self.changeNodeLocation(index, newX, newY, newZ)

    def randomizeAllNodeLocations(self):
        for node in self.geometryOptNodes:
            yOnCenterline = False
            index = self.nodes.index(node)
            xPos = node.xOrig + node.maxXPosDev
            xNeg = node.xOrig - node.maxXNegDev
            if node.yOrig is 0:
                yOnCenterline = True
            else:
                yPos = node.yOrig + node.maxYPosDev
                yNeg = node.yOrig - node.maxYNegDev
            zPos = node.zOrig + node.maxZPosDev
            zNeg = node.zOrig - node.maxZNegDev

            newX = random.uniform(xNeg, xPos)
            if yOnCenterline:
                newY = 0
            else:
                newY = random.uniform(yNeg, yPos)
            newZ = random.uniform(zPos, zNeg)

            self.changeNodeLocation(index, newX, newY, newZ)

    def splitTubeRandomly(self):
        # Should split a tube at a random point along its length and add a node there,
        # then it should reconstruct that tube, but with two elements
        # Should potentially allow for more variation in geometry optimization
        return "TODO"

    def removeTubeRandomly(self):
        # Note, you need to check the randint() docs to make sure the range is right
        numTubes = len(self.tubes)
        randIndex = random.randint(0, numTubes-1)
        self.removeTube(randIndex)


    def removeNodeRandomly(self):
        # Should remove a random node and its tubes
        return "TODO"

    def addANodeAndTubesRandomly(self):
        return "TODO"

    def addTubeRandomly(self):
        nodeFrom = random.choice(self.nodes)
        nodeTo = random.choice(self.nodes)
        alreadyExists = False
        for tube in self.tubes:
            if tube.nodeFrom is nodeFrom or tube.nodeTo is nodeFrom:
                if tube.nodeFrom is nodeTo or tube.nodeTo is nodeTo:
                    alreadyExists = True
        while nodeFrom.isSymmetric is False or nodeTo.isSymmetric is False or nodeFrom is nodeTo or alreadyExists:
            nodeFrom = random.choice(self.nodes)
            nodeTo = random.choice(self.nodes)
            alreadyExists = False
            for tube in self.tubes:
                if tube.nodeFrom is nodeFrom or tube.nodeTo is nodeFrom:
                    if tube.nodeFrom is nodeTo or tube.nodeTo is nodeTo:
                        alreadyExists = True
        thickness = random.choice(allRoundSizes)
        self.addTube(thickness, RD_5x35, nodeFrom.name, nodeTo.name, True, False)

    def addNode(self, name: object, x: object, y: object, z: object, isSymmetric: object, isRequired: object, maxXPosDev: object = None, maxXNegDev: object = None,
                maxYPosDev: object = None,
                maxYNegDev: object = None,
                maxZPosDev: object = None,
                maxZNegDev: object = None,
                xGroup: object = None) -> object:
        node = Node(self, name, x, y, z, isSymmetric, isRequired, maxXPosDev, maxXNegDev, maxYPosDev, maxYNegDev, maxZPosDev, maxZNegDev, xGroup)
        self.nodes.append(node)
        if isSymmetric:
            symName = name + "#m"
            symNode = Node(self, symName, x, -y, z, isSymmetric, isRequired, maxXPosDev, maxXNegDev, maxYNegDev, maxYPosDev, maxZPosDev, maxZNegDev, xGroup)
            self.nodes.append(symNode)
            if symNode.geometryOptPossible:
                self.geometryOptNodes.append(symNode)
        if node.geometryOptPossible:
            self.geometryOptNodes.append(node)

    def removeNode(self, index):
        node = self.nodes.__getitem__(index)
        if node.isSymmetric:
            symNode = self.getSymmetricNode(node)
            for tube in symNode.tubes:
                self.tubes.remove(tube)
            self.nodes.remove(symNode)
            if symNode.geometryOptPossible:
                self.geometryOptNodes.remove(symNode)
        if node.geometryOptPossible:
            self.geometryOptNodes.remove(node)
        for tube in node.tubes:
            self.tubes.remove(tube)
        self.nodes.remove(node)
        for node in self.nodes:
            node.updateConnectingTubes()

    def addTube(self, size, minSize, nodeFrom, nodeTo, isSymmetric, isRequired, group=None):
        tube = Tube(self, size, minSize, nodeFrom, nodeTo, isSymmetric, isRequired, group)
        self.tubes.append(tube)
        tube.nodeFrom.tubes.append(tube)
        tube.nodeTo.tubes.append(tube)
        if isSymmetric:
            symNodeFrom = nodeFrom + "#m"
            symNodeTo = nodeTo + "#m"
            symTube = Tube(self, size, minSize, symNodeFrom, symNodeTo, isSymmetric, isRequired, group)
            self.tubes.append(symTube)
            symTube.nodeFrom.tubes.append(symTube)
            symTube.nodeTo.tubes.append(symTube)
        self.getWeight()

    def removeTube(self, index):
        tube = self.tubes.__getitem__(index)
        if tube.isRequired:
            if tube.isSymmetric:
                symTube = self.getSymmetricTube(tube)
                self.tubes.remove(symTube)
            self.tubes.remove(tube)
            for node in self.nodes:
                node.updateConnectingTubes()
            self.getWeight()

    def getWeight(self):
        weight = 0
        for tube in self.tubes:
            weight += tube.weight
        self.weight = weight
        return weight

    def toString(self, printType=None, long=None):
        if printType == "all":
            self._printTubes(long)
            self._printNodes(long)
        if printType == "nodes":
            self._printNodes(long)
        if printType == "tubes":
            self._printTubes(long)
        print("Total Weight:", '%.3f' % self.weight, "lbs")

    def _printTubes(self, long):
        print("\nTUBES:", self.tubes.__len__(), "total")
        print("----------\n")
        index = 0
        if long is 'long':
            for tube in self.tubes:
                print("\n#", index, "\n", tube.toString(), "going from", tube.nodeFrom.name, "to",
                      tube.nodeTo.name)
                print("  From:", tube.nodeFrom.coordsToString(), "to", tube.nodeTo.coordsToString())
                print("  Weight:", '%.3f' % tube.weight, "lbs\t\tLength:", '%.3f' % tube.length, "inches")
                if tube.isRequired and tube.isSymmetric:
                    print("  Required and Symmetric\n")
                elif tube.isRequired:
                    print("  Required\n")
                elif tube.isSymmetric:
                    print("  Symmetric\n")
                index += 1
        else:
            for tube in self.tubes:
                print("#", index, "-", tube.toString(), "going from", tube.nodeFrom.name, "to",
                      tube.nodeTo.name)
                index += 1

    def _printNodes(self, long):
        print("\nNODES:", self.nodes.__len__(), "total")
        print("----------\n")
        index = 0
        if long is 'long':
            for node in self.nodes:
                print("#", index, "Name:", node.name, "\tCoordinates:", node.coordsToString())
                print("\tHas forces:\t\t", node.forcesToString())
                print("\tWith fixtures:\t", node.fixturesToString())
                if node.isRequired and node.isSymmetric:
                    print("\tRequired and Symmetric")
                elif node.isRequired:
                    print("\tRequired")
                elif node.isSymmetric:
                    print("\tSymmetric")
                print("\tConnects tubes:")
                for tube in node.tubes:
                    print("\t  ", "Tube No.", self.tubes.index(tube), "-->", tube.toString())
                print("\n")
                index += 1
        else:
            for node in self.nodes:
                print("#", index, "Name:", node.name, "with coordinates:", node.coordsToString())
                index += 1

    def plot(self, displacedScaling, figPath=None):
        plotFrame(self, displacedScaling, figPath)

    def plotAni(self, axes, title):
        plotFrameAni(self, axes, title)

    def toTextFile(self, path):
        createFramePath = "%s/createMaxFrame.txt" % path
        createFrameFile = open(createFramePath, "w")

        for node in self.nodes:
            if not node.name.endswith("#m"):
                if node.geometryOptPossible:
                    if node.hasXGroup:
                        createFrameFile.write("\tframe.addNode('%s',%f, %f, %f, %r, %r, %f, %f, %f, %f, %f, %f, '%s')\n" %
                                              (node.name, node.x, node.y, node.z, node.isSymmetric, node.isRequired,
                                               node.maxXPosDev, node.maxXNegDev, node.maxYPosDev, node.maxYNegDev,
                                               node.maxZPosDev, node.maxZNegDev, node.xGroup))
                    else:
                        createFrameFile.write("\tframe.addNode('%s',%f, %f, %f, %r, %r, %f, %f, %f, %f, %f, %f)\n" %
                                              (node.name, node.x, node.y, node.z, node.isSymmetric, node.isRequired,
                                               node.maxXPosDev, node.maxXNegDev, node.maxYPosDev, node.maxYNegDev,
                                               node.maxZPosDev, node.maxZNegDev))
                else:
                    createFrameFile.write("\tframe.addNode('%s',%f, %f, %f, %r, %r)\n" %
                                          (node.name, node.x, node.y, node.z, node.isSymmetric, node.isRequired))
        alreadyFoundSymmetricPair = False
        for tube in self.tubes:
            if tube.isSymmetric and alreadyFoundSymmetricPair is False:
                if tube.group is not None:
                    createFrameFile.write("\tframe.addTube(%s, %s, '%s', '%s', %r, %r, '%s')\n" %
                                          (tube.size.string, tube.minSize.string, tube.nodeFrom.name, tube.nodeTo.name,
                                           tube.isSymmetric, tube.isRequired, tube.group))
                else:
                    createFrameFile.write("\tframe.addTube(%s, %s, '%s', '%s', %r, %r)\n" %
                                          (tube.size.string, tube.minSize.string, tube.nodeFrom.name, tube.nodeTo.name,
                                           tube.isSymmetric, tube.isRequired))

                alreadyFoundSymmetricPair = True
            elif not tube.isSymmetric:
                if tube.group is not None:
                    createFrameFile.write("\tframe.addTube(%s, %s, '%s', '%s', %r, %r, '%s')\n" %
                                          (tube.size.string, tube.minSize.string, tube.nodeFrom.name, tube.nodeTo.name,
                                           tube.isSymmetric, tube.isRequired, tube.group))
                else:
                    createFrameFile.write("\tframe.addTube(%s, %s, '%s', '%s', %r, %r)\n" %
                                          (tube.size.string, tube.minSize.string, tube.nodeFrom.name, tube.nodeTo.name,
                                           tube.isSymmetric, tube.isRequired))
            else:
                alreadyFoundSymmetricPair = False

        createFrameFile.close()
