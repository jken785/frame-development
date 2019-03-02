

from loadCases import *
import loadCases
from createBaseFrame import *
from objectiveFunction import *


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D




frame = createBaseFrame()





frame.toString('all')

# _, displacements, _= frame.solve()
# val1 = ObjectiveFunction(displacements)
# print("val1:",val1)
#
# frame.setLoadCase(LoadCases.twist200)
# _, displacements, _= frame.solve()
# val2 = ObjectiveFunction(displacements)
# print("val2:", val2)
#
# score = frame.solveAllLoadCases()
# print("Score:",score)


frame.plot(25)

# inputCommand = input("Enter your command and I will do as you wish:\n")
# exec(inputCommand)






