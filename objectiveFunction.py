from loadCases import *
import numpy as np
import math

def ObjectiveFunction(displacements):
    objFuncValue = 0
    for loadCase in LoadCases.listLoadCases:
        weight = loadCase.objFuncWeight
        for node in loadCase.objFuncNodes:
            totalDisp = math.sqrt(math.pow(displacements[0,node],2)
                                  +math.pow(displacements[1,node],2)
                                  +math.pow(displacements[2,node],2))
            objFuncValue += totalDisp*weight
    return objFuncValue