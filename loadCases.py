
class LoadCases:

    class twist:
        name = "Torsional Stiffness"
        # LOADS
        # specify forces as a list, then place that list at the end of a list of nodes affected by that force

        # Upper forces on a-arm nodes on the left side of the car
        forceUpUpper = [0, 0, 100, 0, 0, 0]
        nodesForceUpUpper = [4, 8, forceUpUpper]
        #nodesForceUpUpper = [38, 46, forceUpUpper]

        forceUpLower = [0, 0, 100, 0, 0, 0]
        nodesForceUpLower = [6, 10, forceUpLower]
        #nodesForceUpLower = [40, 44, forceUpLower]

        # do this again for every distinct force in the simulation

        # Down forces on a-arm nodes on the right side of the car (use mirrored "%m" node numbers)
        forceDownUpper = [0, 0, -100, 0, 0, 0]
        nodesForceDownUpper = [5, 9, forceDownUpper]
        #nodesForceDownUpper = [39, 47, forceDownUpper]

        forceDownLower = [0, 0, -100, 0, 0, 0]
        nodesForceDownLower = [7, 11, forceDownLower]
        #nodesForceDownLower = [41, 45, forceDownLower]

        # put all the lists of nodes (followed by the forces that affect them) in one big list called "nodeForceCases"
        nodeForceCases = [nodesForceUpUpper, nodesForceUpLower, nodesForceDownUpper, nodesForceDownLower]

        # FIXTURES
        # to define a node's fixtures more specifically, use Frame.setFixtures(self, node, x, y, z, xMom, yMom, zMom)

        # put any nodes that you would like to complete fix (since a moment is applied on the car) in the list below:
        #Fixed rear nodes
        fixedNodes = [44, 45, 46, 47]

        #Fixed front nodes
        #fixedNodes = [4, 5, 6, 7]

        # Optimization Target Nodes
        # defines which nodes get submitted to the objective function for displacement minimization
        objFuncNodes = [4, 6, 8, 10]

        # defines how heavily displacements at these nodes are weighted relative to those in other load cases

        # note to Jake -- maybe change this so that each node has individual weight?
        objFuncWeight = 1

        def setForceUpUpper(self, x, y, z, xMom, yMom, zMom):
            return

    class suspLoads:
        name = "Suspension Loads"
        damperForce = [0, 0, 200, 0, 0, 0]
        damperLoadNodes = [7, 29, damperForce]

        rockerForceRight = [0, 300, 0, 0, 0, 0]
        rockerForceRightNodes = [28, rockerForceRight]

        rockerForceLeft = [0, -300, 0, 0, 0, 0]
        rockerForceLeftNodes = [18, rockerForceLeft]


        nodeForceCases = [damperLoadNodes, rockerForceRightNodes, rockerForceLeftNodes]

        # Try to put fixed nodes some distance away from the fixed nodes
        fixedNodes = [11, 12, 13, 14, 15]

        objFuncNodes = [6, 22, 23, 24, 25, 26, 27]
        objFuncWeight = 0.5

    # Must add each load case that you wish to include while optimizing
    listLoadCases = [twist, suspLoads]
