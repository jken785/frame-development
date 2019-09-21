
from createBaseFrame import *

frame = createBaseFrame()

frame.toString('all')

frame.solveAllLoadCases(1)
print("\n%.2f N*m/deg" % frame.torStiffness)