
if __name__ == "__main__":
    # Important Sim Parameters
    # ----------------------------
    numGenerations = 25
    numSeeds = 2
    numChildrenPerSeed = 5
    maxNumRandNodes = 2
    maxNumRandTubes = 5

    weightMultiplier = 0.0075
    maxDispOfAnyTargetNode = 0.31
    maxAvgDisp = 0.271
    maxWeight = 59.51

    useOriginalBaseFrame = True
    # ----------------------------

    # Plotting parameters
    # ----------------------------
    finalDisplacementScaling = 15
    graphUpdatePeriod = 1
    plotCurrentFrame = False
    # ----------------------------

    from createFrame import *
    from createBaseFrame import *
    import copy
    import matplotlib.pyplot as plt
    import time
    from loadCases import *
    import os
    import datetime
    import multiprocessing as mp

    currentDateTime = datetime.datetime.now()
    workingDir = os.getcwd()
    path = "%s\\results" % workingDir
    if os.path.isdir(path) is False:
        os.mkdir(path)
    timestamp = currentDateTime.strftime("%Y-%m-%d %Hh %Mm %Ss")
    simFolderPath = "%s\\results\\%s" % (workingDir, timestamp)
    os.mkdir(simFolderPath)
    consOutPath = "%s\\consoleOuput.txt" % simFolderPath
    consoleOutput = open(consOutPath, "w")

    def printOut(line):
        print(line)
        consoleOutput.write(line)
        consoleOutput.write("\n")

    printOut("--PARAMETERS--")
    printOut("\nNumber of Generations: %i" % numGenerations)
    printOut("Number of Surviving Seeds Per Generation: %i" % numSeeds)
    printOut("Number of Children Per Seed Per Generation: %i" % numChildrenPerSeed)
    numFramesAnalyzed = numGenerations * numSeeds * numChildrenPerSeed
    printOut("\nYou have elected to analyze %i frames" % numFramesAnalyzed)
    printOut("across %i generations (i.e. %i per generation)" % (numGenerations, int(numFramesAnalyzed/numGenerations)))
    printOut("\nMaximum number of mutated tubes per individual: %i" % maxNumRandTubes)
    printOut("Maximum number of mutated nodes per individual: %i" % maxNumRandNodes)
    printOut("\nMaximum displacement allowed for any target node: %.5f inches" % maxDispOfAnyTargetNode)
    printOut("Maximum average displacement allowed for all target nodes: %.5f inches" % maxAvgDisp)
    printOut("Maximum weight allowed: %.3f pounds" % maxWeight)
    printOut("\nFrame mass is weighted at %f in the objective function" % weightMultiplier)
    if useOriginalBaseFrame:
        printOut("\nUsing createBaseFrame() to construct the initial seeds")
    else:
        printOut("\nUsing createFrame() to construct the initial seeds")

    def sortingKey(elem):
        return elem[0]

    # Time the simulation
    start = time.time()

    # Set up graphs (change size of figure's window using the first line below)
    fig = plt.figure(figsize=(12,9))
    grid = plt.GridSpec(6, 4, hspace=0.8, wspace=0.2)
    ax1 = fig.add_subplot(grid[0:2, :2], title="Score/Weight vs Generations")
    ax1.set_ylabel('Objective Function Score')
    ax2 = fig.add_subplot(grid[2:4, :2], title="Avg Displacement vs Generations")
    ax2.set_ylabel('Inches')
    ax3 = fig.add_subplot(grid[4:6, :2], title="Weight vs Generations")
    ax3.set_ylabel('Pounds')
    if plotCurrentFrame:
        ax4 = fig.add_subplot(grid[3:6, 2:], projection='3d')
        ax5 = fig.add_subplot(grid[0:3, 2:], projection='3d')
        ax5.view_init(azim=-135, elev=35)
    else:
        ax4 = fig.add_subplot(grid[0:, 2:], title="Maximum Frame", projection='3d')
    ax4.view_init(azim=-135, elev=35)
    ax1.grid()
    ax2.grid()
    ax3.grid()

    # Initialize variables
    maxScorePerWeight = 0
    averageDisp = 0

    maxScoresPerWeight = []
    weights = []
    averageDisps = []
    iterations = []
    if useOriginalBaseFrame:
        baseFrame = createBaseFrame()
    else:
        baseFrame = createFrame()
    baseFrameScorePerWeight, dispList, baseFrameAvgDisp = baseFrame.solveAllLoadCases(weightMultiplier)
    printOut("\nBase Frame Weight: %.3f" % baseFrame.weight)
    printOut("Base Frame Score: %.3f" % baseFrameScorePerWeight)
    printOut("Base Frame Avg. Disp.: %.5f" % baseFrameAvgDisp)
    printOut("Base Frame Max Disp of A Target Node: %.5f" % max(dispList))

    maxScoresPerWeight.append(baseFrameScorePerWeight)
    weights.append(baseFrame.weight)
    averageDisps.append(baseFrameAvgDisp)
    iterations.append(0)

    maxFrame = baseFrame
    errorFlag = False
    seeds = []
    for i in range(numSeeds):
        seeds.append(copy.deepcopy(maxFrame))

    ax1.plot(iterations, maxScoresPerWeight)
    ax2.plot(iterations, averageDisps)
    ax3.plot(iterations, weights)
    maxFrame.plotAni(ax4, "Maximum Frame")
    if plotCurrentFrame:
        maxFrame.plotAni(ax5, "Current Frame")
    # fig.suptitle("Starting in 3")
    # plt.pause(1)
    # fig.suptitle("Starting in 2")
    # plt.pause(1)
    # fig.suptitle("Starting in 1")
    # plt.pause(1)
    # fig.suptitle("Genetic Simulation - Geometry and Thickness")
    # plt.pause(.001)

    printOut("\n--START--")

def generateIndividuals(q, seeds):
    global maxWeight
    global maxDispOfAnyTargetNode
    global maxAvgDisp
    global weightMultiplier
    global numGenerations
    global numSeeds
    global numChildrenPerSeed
    individuals = []
    for seed in seeds:
        theSameInd = copy.deepcopy(seed)
        individuals.append(theSameInd)
        for i in range(1, numChildrenPerSeed):
            individual = copy.deepcopy(seed)
            randomizeThicknessNotGeometry = random.choice((True, False))
            if randomizeThicknessNotGeometry:
                numRandTubes = random.randint(1, maxNumRandTubes)
                for j in range(numRandTubes):
                    individual.randomizeThicknessOfRandomTube()
            else:
                numRandNodes = random.randint(1, maxNumRandNodes)
                for j in range(numRandNodes):
                    individual.randomizeLocationOfRandomNode()
            individuals.append(individual)
            # if plotCurrentFrame:
            #     individual.plotAni(ax5, "Current Frame")
            #     plt.pause(0.000000000000001)


    sortingList = []
    for individual in individuals:
        scorePerWeight, dispList, avgDisp = individual.solveAllLoadCases(weightMultiplier)
        if (individual.weight < maxWeight and maxDispOfAnyTargetNode > max(dispList) and maxAvgDisp > avgDisp):
            tuple = (scorePerWeight, avgDisp, individual)
            sortingList.append(tuple)

    q.put(0)

def multithreadKernel(seeds):
    processes = []
    rets = []
    if __name__ == "__main__":
        seedsLeft = seeds[:int(numSeeds / 2)]
        seedsRight = seeds[int(numSeeds / 2):]
        q = mp.Queue()
        left = mp.Process(target=generateIndividuals, args=(q, seedsLeft))
        right = mp.Process(target=generateIndividuals, args=(q, seedsRight))
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


    for gen in range(1, numGenerations+1):
        # Generate generation individuals
        if gen is 1:
            startOneGen = time.time()


        individuals = []
        multiReturn = multithreadKernel(seeds)

        multiReturn = np.array(multiReturn)
        multiReturn.flatten()



        # Solve generation individuals
        sortingList = []

        for i in range(len(individuals)):
            individual = individuals.__getitem__(i)
            scorePerWeight, dispList, avgDisp = individual.solveAllLoadCases(weightMultiplier)
            if (individual.weight < maxWeight and maxDispOfAnyTargetNode > max(dispList) and maxAvgDisp > avgDisp):
                tuple = (scorePerWeight, avgDisp, individual)
                sortingList.append(tuple)

        if len(sortingList) is 0:
            printOut("--ERROR--")
            printOut("Check that your maxWeight, maxDispOfAnyTargetNode and maxAvgDisp are not set too low")
            errorFlag = True
            break

        sortingList.sort(key = sortingKey, reverse=True)
        seeds.clear()
        for i in range(numSeeds):
            seeds.append(sortingList.__getitem__(i)[2])

        bestInd = sortingList.__getitem__(0)
        bestIndScore = bestInd[0]
        bestIndAvgDisp = bestInd[1]
        bestIndFrame = bestInd[2]
        if maxScorePerWeight < sortingList.__getitem__(0)[0]:
            maxScorePerWeight = bestIndScore
            averageDisp = bestIndAvgDisp
            maxFrame = bestIndFrame

        maxScoresPerWeight.append(maxScorePerWeight)
        averageDisps.append(averageDisp)
        iterations.append(gen)
        weights.append(maxFrame.weight)

        if gen % graphUpdatePeriod is 0:
            ax1.plot(iterations, maxScoresPerWeight)
            ax2.plot(iterations, averageDisps)
            ax3.plot(iterations, weights)
            maxFrame.plotAni(ax4, "Maximum Frame")
            plt.pause(0.001)

        if gen is 1:
            endOneGen = time.time()
            minutesPerGen = (endOneGen - startOneGen) / 60
            print("\nSimulation will take an estimated %.1f minutes to complete" % (minutesPerGen * (numGenerations+1)))
        printOut("\n")
        printOut("Generation No. %i" % gen)
        printOut("Max Score Per Weight:\t\t%.3f" % maxScorePerWeight)
        printOut("Avg Disp. of Target Nodes:\t%.5f" % averageDisp)
        printOut("Total Weight:\t\t\t%.3f" % maxFrame.weight)
        timeRemaining = (minutesPerGen*numGenerations) - (minutesPerGen*(gen-1))
        print("\n~%.1f minutes remaining..." % timeRemaining)


    ax1.plot(iterations, maxScoresPerWeight)
    ax2.plot(iterations, averageDisps)
    ax3.plot(iterations, weights)
    maxFrame.plotAni(ax4, "Maximum Frame")
    maxFrame.toTextFile(simFolderPath)

    if not errorFlag:
        printOut("\n--FINISHED--")

        printOut("\n--STATS--")
        end = time.time()
        minutesTaken = (end - start) / 60
        printOut("\nMinutes taken for simulation to complete: %.1f" % minutesTaken)
        printOut("That's %.2f frames per second!" % (numFramesAnalyzed/(minutesTaken*60)))
        printOut("\nTotal Number of Frames Analyzed: %i" % numFramesAnalyzed)
        printOut("\nThe best frame's score was %.3f" % (maxScorePerWeight-baseFrameScorePerWeight))
        printOut("better than the original seed frame")
        printOut("\nThe weight of the best frame was")
        printOut("%.2f pounds less than the original seed frame" % (baseFrame.weight-maxFrame.weight))
        printOut("\nThe avg. displacement of all target nodes for the best frame was")
        printOut("%.5f inches less than the original seed frame" % (baseFrameAvgDisp-averageDisp))

        # Plot graphs and frame/displacements

        figPath = '%s\\graph.png' % simFolderPath
        fig.savefig(figPath)
        for loadCase in LoadCases.listLoadCases:
            maxFrame.setLoadCase(loadCase)
            figPath = '%s\\%s.png' % (simFolderPath, loadCase.name)
            maxFrame.solve(weightMultiplier)
            maxFrame.plot(finalDisplacementScaling, figPath)

    consoleOutput.close()


