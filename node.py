
class Node:

    def __init__(self, frame, name, x, y, z):
        self.name = name
        self.frame = frame
        self.x = x
        self.y = y
        self.z = z
        self.tubes = []
        self.forcesApplied = [0, 0, 0, 0, 0, 0]
        self.fixtures = [0, 0, 0, 0, 0, 0]

    def updateConnectingTubes(self):
        for tube in self.tubes:
            if self.frame.tubes.__contains__(tube):
                continue
            else:
                self.tubes.remove(tube)

        for tube in self.frame.tubes:
            if self.tubes.__contains__(tube):
                continue
            else:
                if tube.nodeTo == self or tube.nodeFrom == self:
                    self.tubes.append(tube)

    def setForcesApplied(self, x, y, z, xMom, yMom, zMom):
        self.forcesApplied = [x, y, z, xMom, yMom, zMom]

    def setFixtures(self, x, y, z, xMom, yMom, zMom):
        self.fixtures = [x, y, z, xMom, yMom, zMom]

    def forcesToString(self):
        x = self.forcesApplied.__getitem__(0)
        y = self.forcesApplied.__getitem__(1)
        z = self.forcesApplied.__getitem__(2)
        xMom = self.forcesApplied.__getitem__(3)
        yMom = self.forcesApplied.__getitem__(4)
        zMom = self.forcesApplied.__getitem__(5)
        return "({0}, {1}, {2}, {3}, {4}, {5})".format(x, y, z, xMom, yMom, zMom)

    def setFixtures(self, x, y, z, xMom, yMom, zMom):
        self.fixtures = [x, y, z, xMom, yMom, zMom]

    def fixturesToString(self):
        x = self.fixtures.__getitem__(0)
        y = self.fixtures.__getitem__(1)
        z = self.fixtures.__getitem__(2)
        xMom = self.fixtures.__getitem__(3)
        yMom = self.fixtures.__getitem__(4)
        zMom = self.fixtures.__getitem__(5)
        return "({0}, {1}, {2}, {3}, {4}, {5})".format(x, y, z, xMom, yMom, zMom)

    def coordsToString(self):
        return "({0}, {1}, {2})".format(self.x, self.y, self.z)


