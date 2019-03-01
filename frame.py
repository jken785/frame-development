import random
from tubeSizes import allRoundSizes
from node import *
from tube import *
import generateMatrices
from solver import *
from generateMatrices import *
import numpy as np


class Frame:

    def __init__(self):
        self.tubes = []
        self.nodes = []
        self.torStiffness = None
        self.weight = None
        self.internalForces = None
        self.displacements = None
        self.reactions = None

    def getTorStiffness(self):
        return 0

    def solve(self):
        numTubes, numNodes, coord, con, fixtures, loads, dist, E, G, areas, I_y, I_z, J, St, be = generateMatrices(self, False)
        internalForces, displacements, reactions = Solver(numTubes, numNodes, coord, con, fixtures, loads, dist, E, G, areas, I_y, I_z, J, St, be)
        self.internalForces = internalForces
        self.displacements = displacements
        self.reactions = reactions
        return internalForces, displacements, reactions

    def setLoadCase(self, loadCase):
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
        if tube.nodeFrom.name.endswith("-m") and tube.nodeTo.name.endswith("-m"):
            symNodeFrom = tube.nodeFrom.name.split("-m")[0]
            symNodeTo = tube.nodeTo.name.split("-m")[0]
        else:
            symNodeFrom = tube.nodeFrom.name + "-m"
            symNodeTo = tube.nodeTo.name + "-m"
        for searchTube in self.tubes:
            if searchTube.nodeFrom.name == symNodeFrom and searchTube.nodeTo.name == symNodeTo:
                return searchTube
        return None

    def getSymmetricNode(self, node):
        if node.name.endswith("-m"):
            symName = node.name.split("-m")[0]
        else:
            symName = node.name + "-m"
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


    # will not allow changes to square tubes
    def randomizeThickness(self, index):
        tube = self.tubes.__getitem__(index)
        if tube.isRound:
            sizeIndex = allRoundSizes.index(tube.minSize)
            availableSizes = allRoundSizes[sizeIndex:len(allRoundSizes) - 1]
            thickness = random.choice(availableSizes)
            self.changeTubeThickness(index, thickness)

    # optimization: should only randomize one tube in each symmetric pair -- also maybe implement lists of the symmetric
    # pair to prevent repeat look-ups
    def randomizeAllThicknesses(self):
        for i in range(len(self.tubes)):
            self.randomizeThickness(i)

    def addNode(self, name, x, y, z, isSymmetric):
        node = Node(self, name, x, y, z, isSymmetric)
        self.nodes.append(node)
        if isSymmetric:
            symName = name + "-m"
            symNode = Node(self, symName, x, -y, z, isSymmetric)
            self.nodes.append(symNode)

    def removeNode(self, index):
        node = self.nodes.__getitem__(index)
        if node.isSymmetric:
            symNode = self.getSymmetricNode(node)
            for tube in symNode.tubes:
                self.tubes.remove(tube)
            self.nodes.remove(symNode)
        for tube in node.tubes:
            self.tubes.remove(tube)
        self.nodes.remove(node)
        for node in self.nodes:
            node.updateConnectingTubes()

    def addTube(self, size, minSize, nodeFrom, nodeTo, isSymmetric):
        tube = Tube(self, size, minSize, nodeFrom, nodeTo, isSymmetric)
        self.tubes.append(tube)
        tube.nodeFrom.tubes.append(tube)
        tube.nodeTo.tubes.append(tube)
        if isSymmetric:
            symNodeFrom = nodeFrom + "-m"
            symNodeTo = nodeTo + "-m"
            symTube = Tube(self, size, minSize, symNodeFrom, symNodeTo, isSymmetric)
            self.tubes.append(symTube)
            symTube.nodeFrom.tubes.append(symTube)
            symTube.nodeTo.tubes.append(symTube)

    def removeTube(self, index):
        tube = self.tubes.__getitem__(index)
        if tube.isSymmetric:
            symTube = self.getSymmetricTube(tube)
            self.tubes.remove(symTube)
        self.tubes.remove(tube)
        for node in self.nodes:
            node.updateConnectingTubes()

    def getWeight(self):
        weight = 0
        for tube in self.tubes:
            weight += tube.weight
        self.weight = weight
        return weight

    def toString(self):
        print("TUBES:", self.tubes.__len__())
        print("----------\n")
        index = 0
        for tube in self.tubes:
            print("#",index,"\n",tube.toString(), "going from", tube.nodeFrom.coordsToString(),"to",tube.nodeTo.coordsToString())
            print("  with weight", '%.3f' % tube.weight,"lbs and length", '%.3f' % tube.length,"inches\n")
            index += 1
        print("NODES:", self.nodes.__len__())
        print("----------\n")
        index = 0
        for node in self.nodes:
            print("#", index, "Name:", node.name, "\tCoordinates:", node.coordsToString())
            print("\tHas forces:\t\t", node.forcesToString())
            print("\tWith fixtures:\t", node.fixturesToString())
            print("\tConnects tubes:")
            for tube in node.tubes:
                print("\t  ","Tube No.",self.tubes.index(tube),"with thickness",tube.toString())
            print("\n")
            index += 1
        print("Weight:",'%.3f' % self.getWeight(),"lbs")



