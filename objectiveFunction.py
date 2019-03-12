from loadCases import *
import math

def ObjectiveFunction(frame, currLoadCase, weightMultiplier):
    objFuncValue = 0
    normalizer = 0
    getSigFigs = 10
    frameWeight = frame.weight

    # this loop normalizes the objFuncWeights across all load cases
    for loadCase in LoadCases.listLoadCases:
        normalizer += loadCase.objFuncWeight

    # this loop computes the value of the objective function
    dispList = [];
    dispMultiplier = currLoadCase.objFuncWeight/normalizer
    for node in currLoadCase.objFuncNodes:
        totalDisp = math.sqrt(math.pow(frame.displacements[0,node],2)
                              +math.pow(frame.displacements[1,node],2)
                              +math.pow(frame.displacements[2,node],2))

        objFuncValue += (totalDisp*dispMultiplier)
        dispList.append(totalDisp)

    objFuncValuePerWeight = 1/((objFuncValue)+(weightMultiplier*frameWeight))
    avgDisp = sum(dispList) / len(dispList)

    return objFuncValuePerWeight*getSigFigs, dispList, avgDisp