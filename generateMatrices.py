
import numpy as np

def generateMatrices(frame, printOn):
    # Initialize empty arrays
    numTubes = frame.tubes.__len__()
    numNodes = frame.nodes.__len__()
    coord = np.empty([3, numNodes])
    con = np.empty([4, numTubes])
    fixtures = np.empty([6, numNodes])
    loads = np.empty([6, numNodes])
    E = np.empty([numTubes, 1])
    G = np.empty([numTubes, 1])
    areas = np.empty([numTubes, 1])
    I_y = np.empty([numTubes, 1])
    I_z = np.empty([numTubes, 1])
    J = np.empty([numTubes, 1])

    # If you really need distributed loads, add values to this matrix in the "tube" for-loop below
    dist = np.zeros([3, numTubes])

    # Don't really know what these matrices do, but the solver needs them
    St = np.zeros([6, numNodes])
    be = np.zeros([numTubes, 1])

    # Fill the matrices using the frame
    for i in range(numNodes):
        node = frame.nodes.__getitem__(i)
        coord[0][i] = node.x
        coord[1][i] = node.y
        coord[2][i] = node.z

        fixtures[0][i] = node.fixtures.__getitem__(0)
        fixtures[1][i] = node.fixtures.__getitem__(1)
        fixtures[2][i] = node.fixtures.__getitem__(2)
        fixtures[3][i] = node.fixtures.__getitem__(3)
        fixtures[4][i] = node.fixtures.__getitem__(4)
        fixtures[5][i] = node.fixtures.__getitem__(5)

        loads[0][i] = node.forcesApplied.__getitem__(0)
        loads[1][i] = node.forcesApplied.__getitem__(1)
        loads[2][i] = node.forcesApplied.__getitem__(2)
        loads[3][i] = node.forcesApplied.__getitem__(3)
        loads[4][i] = node.forcesApplied.__getitem__(4)
        loads[5][i] = node.forcesApplied.__getitem__(5)

    for i in range(numTubes):
        tube = frame.tubes.__getitem__(i)
        nodeFromIndex = frame.nodes.index(tube.nodeFrom)
        nodeToIndex = frame.nodes.index(tube.nodeTo)
        con[0][i] = nodeFromIndex + 1
        con[1][i] = nodeToIndex + 1
        con[2][i], con[3][i] = 1, 1

        E[i] = tube.size.E
        G[i] = tube.size.G
        areas[i] = tube.size.A
        I_y[i] = tube.size.I
        I_z[i] = tube.size.I
        J[i] = tube.size.J

    if printOn:
        print(coord, "\n")
        print(fixtures, "\n")
        print(loads, "\n")
        print(con, "\n")
        print(E, "\n")
        print(G, "\n")
        print(areas, "\n")
        print(I_y, "\n")
        print(I_z, "\n")
        print(J, "\n")

    return numTubes, numNodes, coord, con, fixtures, loads, dist, E, G, areas, I_y, I_z, J, St, be


