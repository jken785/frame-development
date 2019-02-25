import random
from tubeSizes import allSizes
from node import *
from tube import *
from loadCases import *


class Frame:

    def __init__(self):
        self.tubes = []
        self.nodes = []

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

    def changeTubeThickness(self, index, size):
        tube = self.tubes.__getitem__(index)
        newTube = Tube(self, size, tube.nodeFrom.name, tube.nodeTo.name)
        self.removeTube(index)
        self.tubes.insert(index, newTube)
        for node in self.nodes:
            node.updateConnectingTubes()

    def randomizeThickness(self, index):
        thickness = random.choice(allSizes)
        self.changeTubeThickness(index, thickness)

    def randomizeAllThicknesses(self):
        for i in range(len(self.tubes)):
            self.randomizeThickness(i)

    def addNode(self, name, x, y, z):
        node = Node(self, name, x, y, z)
        self.nodes.append(node)

    def removeNode(self, index):
        node = self.nodes.__getitem__(index)
        for tube in node.tubes:
            self.tubes.remove(tube)
        self.nodes.remove(node)
        for node in self.nodes:
            node.updateConnectingTubes()

    def addTube(self, size, nodeFrom, nodeTo):
        tube = Tube(self, size, nodeFrom, nodeTo)
        self.tubes.append(tube)
        tube.nodeFrom.tubes.append(tube)
        tube.nodeTo.tubes.append(tube)

    def removeTube(self, index):
        tube = self.tubes.__getitem__(index)
        self.tubes.remove(tube)
        for node in self.nodes:
            node.updateConnectingTubes()

    def getWeight(self):
        weight = 0
        for tube in self.tubes:
            weight += tube.weight
        return weight

    def toString(self):
        print("TUBES:", self.tubes.__len__(),"\n")
        index = 0
        for tube in self.tubes:
            print("#",index,"\n",tube.toString(), "going from", tube.nodeFrom.coordsToString(),"to",tube.nodeTo.coordsToString())
            print("  with weight", '%.3f' % tube.weight,"lbs and length", '%.3f' % tube.length,"inches\n")
            index += 1
        print("NODES:", self.nodes.__len__(),"\n")
        index = 0
        for node in self.nodes:
            print("#", index, "Name:", node.name, "\tCoordinates:", node.coordsToString())
            print("\tHas forces:\t\t", node.forcesToString())
            print("\tWith fixtures:\t", node.fixturesToString())
            print("\tConnects tubes:")
            for tube in node.tubes:
                print("\t",tube.toString())
            print("\n")
            index += 1
        print("Weight:",'%.3f' % self.getWeight(),"lbs")



