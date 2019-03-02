
class LoadCases:

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
        fixedNodes = [2, 5]

        # Optimization Target Nodes
        # defines which nodes get submitted to the objective function for displacement minimization
        objFuncNodes = [0, 1]

        # defines how heavily displacements at these nodes are weighted relative to those in other
        # load cases -- SHOULD BE A NUMBER BETWEEN 0 AND 1

        # note to Jake -- maybe change this so that  each node has individual weight?
        objFuncWeight = 0.5


    class twist200:
        forceUp = [0, 0, 200, 0, 0, 0]
        nodesForceUp = [0, 1, forceUp]

        forceDown = [0, 0, -200, 0, 0, 0]
        nodesForceDown = [2, 3, forceDown]

        nodeForceCases = [nodesForceUp, nodesForceDown]

        fixedNodes = [0, 2]

        objFuncNodes = [0, 1]
        objFuncWeight = 1

    # Must add each load case that you wish to include while optimizing
    listLoadCases = [twist100, twist200]
