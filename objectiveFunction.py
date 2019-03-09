from loadCases import *
import math

def ObjectiveFunction(frame):
    objFuncValue = 0
    normalizer = 0
    getSigFigs = 10
    frameWeight = frame.weight
    weightMultiplier = 0.0075

    # this loop normalizes the objFuncWeights across all load cases
    for loadCase in LoadCases.listLoadCases:
        normalizer += loadCase.objFuncWeight

    # this loop computes the value of the objective function
    dispList = [];
    for loadCase in LoadCases.listLoadCases:
        dispMultiplier = loadCase.objFuncWeight/normalizer
        for node in loadCase.objFuncNodes:
            totalDisp = math.sqrt(math.pow(frame.displacements[0,node],2)
                                  +math.pow(frame.displacements[1,node],2)
                                  +math.pow(frame.displacements[2,node],2))

            objFuncValue += (totalDisp*dispMultiplier)
            dispList.append(totalDisp)

    objFuncValuePerWeight = 1/((objFuncValue)+(weightMultiplier*frameWeight))
    objFuncValue = 1/objFuncValue
    avgDisp = sum(dispList) / len(dispList)

    return objFuncValuePerWeight*getSigFigs, dispList, avgDisp