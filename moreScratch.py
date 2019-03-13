import multiprocessing as mp
from createBaseFrame import *
from createFrame import *
from createBaseFrame import *
import copy
import matplotlib.pyplot as plt
import time
from loadCases import *
import os
import datetime
import multiprocessing as mp

def generateAndSolveIndividuals(q, seeds):
    individuals = []
    for seed in seeds:
        seed.randomizeAllThicknesses()
        scorePerWeight, dispList, avgDisp = seed.solveAllLoadCases(weightMultiplier)
        if (seed.weight < maxWeight and maxDispOfAnyTargetNode > max(dispList) and maxAvgDisp > avgDisp):
            tuple = (scorePerWeight, avgDisp, individual)
            sortingList.append(tuple)
    q.put(frame)

def multithreadKernel():
    processes = []
    rets = []
    if __name__ == "__main__":
        q = mp.Queue()
        left = mp.Process(target=generateIndividuals, args=(q, 0))
        right = mp.Process(target=generateIndividuals, args=(q, 1))
        processes.append(left)
        processes.append(right)
        for p in processes:
            p.start()
        for p in processes:
            returnInds = q.get()  # will block
            rets.append(returnInds)
    for p in processes:
        p.join()
    return rets

if __name__ == "__main__":


    multithreadKernel())
    print("I might have been here more than once")