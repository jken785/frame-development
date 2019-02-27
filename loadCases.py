

class twist100:
    # LOADS
    # specify forces as a list, then place that list at the end of a list of nodes affected by that force
    forceUp = [100, 0, 100, 0, 0, 0]
    nodesForceUp = [0, 5, forceUp]

    # do this again for every distinct force in the simulation
    forceDown = [-100, 0, -100, 0, 0, 0]
    nodesForceDown = [1, 4, forceDown]

    # put all the lists of nodes (followed by the forces that affect them) in one big list called "nodeForceCases"
    nodeForceCases = [nodesForceUp, nodesForceDown]

    # FIXTURES
    # to define a node's fixtures more specifically, use Frame.setFixtures(self, node, x, y, z, xMom, yMom, zMom)

    # put any nodes that you would like to complete fix in the list below:
    fixedNodes = [2, 3]

class twist200:
    # LOADS
    # specify forces as a list, then place that list at the end of a list of nodes affected by that force
    forceUp = [0, 0, 200, 0, 0, 0]
    nodesForceUp = [0, 1, forceUp]

    # do this again for every distinct force in the simulation
    forceDown = [0, 0, -200, 0, 0, 0]
    nodesForceDown = [2, 3, forceDown]

    # put all the lists of nodes (followed by the forces that affect them) in one big list called "nodeForceCases"
    nodeForceCases = [nodesForceUp, nodesForceDown]

    # FIXTURES
    # to define a node's fixtures more specifically, use Frame.setFixtures(self, node, x, y, z, xMom, yMom, zMom)

    # put any nodes that you would like to complete fix in the list below:
    fixedNodes = [0, 2]