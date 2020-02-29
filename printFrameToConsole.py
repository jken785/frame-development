
from createBaseFrame import *

frame = createBaseFrame()

#Add (, 'long') after 'all' to have more verbose output
frame.toString('all')

frame.solveAllLoadCases(1)
print("\n%.2f N*m/deg" % frame.torStiffness)