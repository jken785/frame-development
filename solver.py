import numpy as np
import math


def cart2sph(x, y, z):
    hxy = np.hypot(x, y)
    r = np.hypot(hxy, z)
    el = np.arctan2(z, hxy)
    az = np.arctan2(y, x)
    return az, el, r


def Solver(numTubes, numNodes, coord, con, fixtures, loads, dist, E, G, areas, I_y, I_z, J, St, be):
    con = np.array(con)
    Ni = np.zeros((12, 12, numTubes))
    S = np.zeros((6*numNodes, 6*numNodes))
    Pf = np.zeros((np.size(S[:,1]), 1))
    Q = np.zeros((12, numTubes))
    Qfi = Q.copy()
    Ei = Q.copy()
    for i in range(numTubes):
        H = con[:, i]
        h0 = int(H[0])
        h1 = int(H[1])
        C = np.subtract(coord[:, h1-1], coord[:, h0-1])
        e = np.append(np.arange(6*h0-6, 6*h0), np.arange(6*h1-6, 6*h1))
        c = be[i]
        a, b, L = cart2sph(C[0], C[2], C[1])
        ca = math.cos(a)
        sa = math.sin(a)
        cb = math.cos(b)
        sb = math.sin(b)
        cc = math.cos(c)
        sc = math.sin(c)
        r1 = np.array([[1, 0, 0], [0, cc, sc], [0, -sc, cc]])
        r2 = np.array([[cb, sb, 0], [-sb, cb, 0], [0, 0, 1]])
        r3 = np.array([[ca, 0, sa], [0, 1, 0], [-sa, 0, ca]])
        r = np.matmul(np.matmul(r1, r2), r3) # this might not be how you are supposed to do matrix multiplication
        T = np.kron(np.eye(4), r) # this could be source of error (index-related on eye())
        co = 2*L*np.array([6/L, 3, 2*L, L])
        x = areas[i]*(math.pow(L, 2))
        y = I_y[i]*co
        z = I_z[i]*co
        g = (G[i]*J[i]*math.pow(L, 2))/E[i]
        K1 = np.diag([x, z[0], y[0]])
        K2 = np.array([[0, 0, 0], [0, 0, z[1]], [0, -y[1], 0]])
        K3 = np.diag([g, y[2], z[2]])
        K4 = np.diag([-g, y[3], z[3]])
        row1 = np.concatenate((np.concatenate((K1, K2), axis = 1), np.concatenate((-K1, K2), axis=1)), axis = 1)
        row2 = np.concatenate((np.concatenate((K2.transpose(), K3), axis = 1), np.concatenate((-K2.transpose(), K4), axis=1)), axis = 1)
        row3 = np.concatenate((np.concatenate((-K1, -K2), axis=1), np.concatenate((K1, -K2), axis=1)), axis=1)
        row4 = np.concatenate((np.concatenate((K2.transpose(), K4), axis=1), np.concatenate((-K2.transpose(), K3), axis=1)), axis=1)
        kInter = np.concatenate((np.concatenate((row1, row2)), np.concatenate((row3, row4))))
        K = (E[i]/math.pow(L, 3))*kInter
        w = dist[:,i]
        K = np.array(K, dtype=float)
        Qf = (-math.pow(L, 2)/12)*np.array((6*w[0]/L, 6*w[1]/L, 6*w[2]/L, 0, -w[2], w[1], 6*w[0]/L, 6*w[1]/L, 6*w[2]/L, 0, w[2], -w[1])).transpose()
        StTemp = np.array(St.flatten())
        Ste = StTemp[e]
        Qfs = np.matmul(np.matmul(K, T), Ste)
        A = np.diag([0, -0.5, 0.5])
        B = np.zeros((3, 3))
        B[1][2] = 1.5/L
        B[2][1] = -1.5/L
        W = np.diag([1, 0, 0])
        Z = np.zeros((3, 3))
        M = np.eye(12)
        p = np.arange(4, 7)
        q = np.arange(10, 13)
        caseTest = 2*int(H[2]) + int(H[3])

        # Will never enter this code unless the two 1's aren't appended to every element of the "con" matrix
        # AKA: Code has NOT been debugged!
        if caseTest == 0:
            B = (2*B)/3
            M[:, [p, q]] = np.array([-B, -B], [W, Z], [B, B], [Z, W])
        elif caseTest == 1:
            M[:, p] = np.array([[-B], [W], [B], [A]])
        elif caseTest == 2:
            M[:, q] = np.array([[-B], [A], [B], [W]])
        # End of non-debugged code

        Ni[:, :, i] = np.matmul(K, T)
        toAdd = np.matmul(T.transpose(), Ni[:,:,i])
        for j in range(np.size(e)):
            for k in range(np.size(e)):
                S[e[j],e[k]] += toAdd[j, k]
        Qfi[:, i] = np.matmul(M, Qf.transpose())
        toAdd = np.matmul(np.matmul(T.transpose(), M), np.add(Qf, Qfs))
        for j in range(np.size(e)):
            Pf[e[j]] += toAdd[j]
        Ei[:, i] = e
    V = 1 - (np.logical_or(fixtures, St))
    vFlat = V.flatten('F')
    index = 0
    f = []
    for j in range(np.size(vFlat)):
        if vFlat[j] != 0:
            f.append(index)
        index += 1
    f = np.array(f)
    loads = np.array(loads).flatten('F')[f]
    relevantS = np.empty((np.size(f), np.size(f)))
    for j in range(np.size(f)):
        for k in range(np.size(f)):
            relevantS[j, k] = S[f[j],f[k]]
    fixedEndForces = Pf[f].transpose()
    forcesSubtracted = np.subtract(loads, fixedEndForces)
    vResults = np.linalg.solve(relevantS, forcesSubtracted.transpose())
    vFlat = np.array(vFlat, dtype=float)
    for j in range(np.size(vResults)):
        vFlat[f[j]] = vResults[j]
    V = vFlat.reshape((6, numNodes), order='F')
    RInter = np.matmul(S, vFlat)
    R = RInter.reshape((6, numNodes), order='F')
    R = R.flatten('F')
    R[f] = 0
    R = R.reshape((6, numNodes), order='F')
    V = V + St
    for i in range(numTubes):
        ni = Ni[:, :, i]
        indices = np.array(Ei[:, i], dtype=int)
        vei = V.flatten('F')[indices]
        inter = np.matmul(ni, vei.transpose())
        Q[:, i] = inter + Qfi[:, i]
    return Q, V, R


