import math
import tubeSizes


class Tube:

    def __init__(self, frame, size, minSize, nodeFrom, nodeTo, isSymmetric):
        self.E = tubeSizes.E
        self.G = tubeSizes.G
        self.A = size.A
        self.I = size.I
        self.J = size.J
        self.isSymmetric = isSymmetric
        self.isRound = size.round
        self.minSize = minSize
        self.tubeSize = size.name
        self.distLoad = [0, 0, 0]
        for node in frame.nodes:
            if nodeFrom == node.name:
                self.nodeFrom = node
            if nodeTo == node.name:
                self.nodeTo = node

        self.length = self.getLength(nodeFrom, nodeTo)
        self.weight = self.getWeight(self.length)

    def changeThickness(self, size):
        self.A = size.A
        self.I = size.I
        self.J = size.J
        self.tubeSize = size.name
        self.weight = self.getWeight(self.getLength(self.nodeFrom, self.nodeTo))

    def getLength(self, nodeFrom, nodeTo):
        x = self.nodeFrom.x-self.nodeTo.x
        y = self.nodeFrom.y-self.nodeTo.y
        z = self.nodeFrom.z-self.nodeTo.z
        length = math.sqrt((x**2) + (y**2) + (z**2))
        return length

    def getWeight(self, length):
        volume = length * self.A
        density = tubeSizes.density
        return volume*density

    def toString(self):
        return self.tubeSize

