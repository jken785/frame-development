from loadCases import *
import numpy as np
import math

def ObjectiveFunction(frame):
    objFuncValue = 0
    normalizer = 0
    getSigFigs = 10000
    frameWeight = frame.weight
    wFrameWeight = 5
    # this loop normalizes the objFuncWeights across all load cases
    for loadCase in LoadCases.listLoadCases:
        normalizer += loadCase.objFuncWeight

    # this loop computes the value of the objective function
    maxDisp = 0;
    for loadCase in LoadCases.listLoadCases:
        w = loadCase.objFuncWeight/normalizer
        for node in loadCase.objFuncNodes:
            totalDisp = math.sqrt(math.pow(frame.displacements[0,node],2)
                                  +math.pow(frame.displacements[1,node],2)
                                  +math.pow(frame.displacements[2,node],2))
            if totalDisp > maxDisp:
                maxDisp = totalDisp
            objFuncValue += (totalDisp*w)

    objFuncValuePerWeight = objFuncValue/(wFrameWeight*frameWeight)
    return objFuncValuePerWeight*getSigFigs, objFuncValue, maxDisp