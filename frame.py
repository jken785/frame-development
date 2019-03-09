import random
from node import *
import generateMatrices
from solver import *
from generateMatrices import *
from objectiveFunction import *
from plotter import *


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

    def getTorStiffness(self):
        return 0

    def solveAllLoadCases(self):
        scorePerWeight = 0
        avgDisp = 0
        for loadCase in LoadCases.listLoadCases:
            self.setLoadCase(loadCase)
            scorePerWeightToAdd, dispList, avgDisplacement = self.solve()
            scorePerWeight += scorePerWeightToAdd
            avgDisp += avgDisplacement
        return scorePerWeight, dispList, avgDisp

    def solve(self):
        numTubes, numNodes, coord, con, fixtures, loads, dist, E, G, areas, I_y, I_z, J, St, be = generateMatrices(self, False)
        internalForces, displacements, reactions = Solver(numTubes, numNodes, coord, con, fixtures, loads, dist, E, G, areas, I_y, I_z, J, St, be)
        self.internalForces = internalForces
        self.displacements = displacements
        self.reactions = reactions
        scorePerWeight, dispList, maxDisp = ObjectiveFunction(self)
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
        if tube.isRound:
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


    def addNode(self, name, x, y, z, isSymmetric, isRequired, maxXPosDev=None, maxXNegDev=None, maxYPosDev=None, maxYNegDev=None, maxZPosDev=None, maxZNegDev=None,xGroup=None):
        node = Node(self, name, x, y, z, isSymmetric, isRequired, maxXPosDev, maxXNegDev, maxYPosDev, maxYNegDev, maxZPosDev, maxZNegDev, xGroup)
        self.nodes.append(node)
        if isSymmetric:
            symName = name + "#m"
            symNode = Node(self, symName, x, -y, z, isSymmetric, isRequired, maxXPosDev, maxXNegDev, maxYNegDev, maxYPosDev, maxZPosDev, maxZNegDev, xGroup)
            self.nodes.append(symNode)
        if node.geometryOptPossible:
            self.geometryOptNodes.append(node)

    def removeNode(self, index):
        node = self.nodes.__getitem__(index)
        if node.isSymmetric:
            symNode = self.getSymmetricNode(node)
            for tube in symNode.tubes:
                self.tubes.remove(tube)
            self.nodes.remove(symNode)
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

    def plot(self, displacedScaling):
        plotFrame(self, displacedScaling)

    def plotAni(self, axes):
        plotFrameAni(self, axes)



