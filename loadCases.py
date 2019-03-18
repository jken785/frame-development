
class LoadCases:

    class twist:
        name = "Torsional Stiffness"
        # LOADS
        # specify forces as a list, then place that list at the end of a list of nodes affected by that force
        forceUp = [0, 0, 200, 0, 0, 0]
        nodesForceUp = [4, 6, 8, 10, forceUp]

        # do this again for every distinct force in the simulation
        forceDown = [0, 0, -200, 0, 0, 0]
        nodesForceDown = [5, 7, 9, 11, forceDown]

        # put all the lists of nodes (followed by the forces that affect them) in one big list called "nodeForceCases"
        nodeForceCases = [nodesForceUp, nodesForceDown]

        # FIXTURES
        # to define a node's fixtures more specifically, use Frame.setFixtures(self, node, x, y, z, xMom, yMom, zMom)

        # put any nodes that you would like to complete fix in the list below:
        fixedNodes = [52, 46, 47, 44, 45]

        # Optimization Target Nodes
        # defines which nodes get submitted to the objective function for displacement minimization
        objFuncNodes = [4, 5, 6, 7]

        # defines how heavily displacements at these nodes are weighted relative to those in other load cases

        # note to Jake -- maybe change this so that  each node has individual weight?
        objFuncWeight = 1


    class suspLoads:
        name = "Suspension Loads"
        damperForce = [0, 0, 200, 0, 0, 0]
        damperLoadNodes = [12, 13, damperForce]

        rockerForceRight = [0, 300, 0, 0, 0, 0]
        rockerForceRightNodes = [32, rockerForceRight]

        rockerForceLeft = [0, -300, 0, 0, 0, 0]
        rockerForceLeftNodes = [31, rockerForceLeft]


        nodeForceCases = [damperLoadNodes, rockerForceRightNodes, rockerForceLeftNodes]

        fixedNodes = [52, 46, 47, 44, 45]

        objFuncNodes = [12, 13, 31, 32]
        objFuncWeight = 1

    # Must add each load case that you wish to include while optimizing
    listLoadCases = [twist, suspLoads]
