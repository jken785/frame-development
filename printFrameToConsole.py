
from createBaseFrame import *

frame = createBaseFrame()

frame.toString('all')

frame.solveAllLoadCases(0.0075)

if frame.torStiffness is not None:
    print("%.2f N*m/deg" % frame.torStiffness)
else:
    print("no tor stiffness val")