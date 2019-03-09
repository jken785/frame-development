import math
import tubeSizes


class Tube:

    def __init__(self, frame, size, minSize, nodeFrom, nodeTo, isSymmetric, isRequired, group):
        self.size = size
        self.isRequired = isRequired
        self.isSymmetric = isSymmetric
        self.isRound = size.round
        self.minSize = minSize
        self.tubeSizeString = size.name
        self.distLoad = [0, 0, 0]
        for node in frame.nodes:
            if nodeFrom == node.name:
                self.nodeFrom = node
            if nodeTo == node.name:
                self.nodeTo = node
        if group is not None:
            self.group = group
        else:
            self.group = None

        self.length = self.getLength(nodeFrom, nodeTo)
        self.weight = self.getWeight(self.length)

    def changeThickness(self, size):
        self.size = size
        self.tubeSizeString = size.name
        self.weight = self.getWeight(self.getLength(self.nodeFrom, self.nodeTo))

    def getLength(self, nodeFrom, nodeTo):
        x = self.nodeFrom.x-self.nodeTo.x
        y = self.nodeFrom.y-self.nodeTo.y
        z = self.nodeFrom.z-self.nodeTo.z
        length = math.sqrt((x**2) + (y**2) + (z**2))
        return length

    def getWeight(self, length):
        if self.size is not tubeSizes.RD_1xSLD:
            volume = length * self.size.A
            density = tubeSizes.density
            return volume*density
        else:
            return 0

    def toString(self):
        return self.tubeSizeString

