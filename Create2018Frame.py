from tubeSizes import *
from frame import *

def createBaseFrame():
    frame = Frame()

    # note you should add groups, like for main-hoop, so it stays vertical but can move in x
    # symmetric pair could be a type of group

    # especially useful for tubes modelled as multiple tubes, but are actually one tube (i.e. roll hoop)
    # Nodes
    frame.addNode("upper-left-bulkhead", 18.07, 7, 17.511, True, True)
    frame.addNode("lower-left-bulkhead", 18.07, 7, 5.511, True, True)
    frame.addNode("lower-left-frontbrace", 14.07, 7.448, 5.511, True, True)
    frame.addNode("lower-aft-middle-frontbrace", 14.07, 0, 5.511, False, True)
    frame.addNode("lower-foremost-middle-frontbrace", 18.07, 0, 5.511, False, True)
    frame.addNode("upper-left-frontbox", 7.07, 10.247, 13.115, True, True)
    frame.addNode("lower-left-frontbox", 7.07, 8.45, 5.511, True, True)
    frame.addNode("frontbox-crossbrace", 1.01, 0, 5.511, False, True)
    frame.addNode("lower-left-fronthoop", -5.05, 8.45, 5.511, True, True)
    frame.addNode("mid-left-fronthoop", -5.163, 10.101, 13.099, True, True)
    frame.addNode("upper-left-fronthoop", -8.904, 7.817, 23.76, True, True)
    frame.addNode("fore-sideimpact-brace", -15.922, 9.864, 17.658, True, True)
    frame.addNode("mid-upper-sideimpact-brace", -23.094, 10.684, 16.826, True, True)
    frame.addNode("mid-lower-sideimpact-brace", -23.044, 11.524, 13.182, True, True)
    frame.addNode("aft-sideimpact-brace", -37, 12.273, 15.213, True, True)
    frame.addNode("fore-upper-sideimpact", -21.082, 11.368, 13.172, True, True)
    frame.addNode("fore-lower-sideimpact", -22.5, 11, 2, True, True)
    frame.addNode("fore-mainbox-crossbrace", -12.631, 0, 3.986, False, True)
    frame.addNode("aft-mainbox-crossbrace", -29.75, 11, 2, False, True)
    frame.addNode("lower-left-mainhoop", -37, 11, 2, True, True, "MainHoop")
    frame.addNode("mid-left-mainhoop", -37, 12.635, 13.246, True, True, "MainHoop")
    frame.addNode("left-harnessbar", -37, 10.625, 22, True, True)
    frame.addNode("end-of-bend-harnessbar", -40.5, 7.987, 22, True, True)
    frame.addNode("left-brace-mainhoop", -37, 6.934, 37.2, True, True, "MainHoop")
    frame.addNode("upper-left-mainhoop", -37, 6.615, 38.511, True, True, "MainHoop")
    frame.addNode("nipple-mainhoop", -37, 0, 43, False, True, "MainHoop")
    frame.addNode("left-foremost-enginemount", -43.011, 7.576, 15.828, True, True)
    frame.addNode("left-upper-foremost-rear-suspension", -54.594, 9.75, 11.827, True, True)
    frame.addNode("left-lower-foremost-rear-suspension", -53.979, 6.519, 4.527, True, True)
    frame.addNode("left-upper-aft-rear-suspension", -63.998, 9.75, 11.827, True, True)
    frame.addNode("left-lower-aft-rear-suspension", -64.981, 6.519, 4.527, True, True)
    frame.addNode("left-upper-aft-enginemount", -56.879, 3.921, 17.353, True, True)
    frame.addNode("left-lower-aft-enginemount", -56.897, 4.503, 8.101, True, True)
    frame.addNode("left-aft-rearbox", -63.65, 0, 17.015, False, True)
    frame.addNode("left-foremost-rearbox", -57.542, 4.464, 16.838, True, True)
    frame.addNode("right-rear-enginebrace", -56.897, -5.37, 8.1, False, True)
    frame.addNode("rear-crossbrace", -59.480, 0, 4.527, False, True)

    # Tubes
    # Bulkhead -> Fronthoop
    frame.addTube(SQ_1x49, SQ_1x49, "upper-left-bulkhead", "lower-left-bulkhead", True, True)
    frame.addTube(SQ_1x49, SQ_1x49, "upper-left-bulkhead", "upper-left-bulkhead#m", False, True)
    frame.addTube(SQ_1x49, SQ_1x49, "lower-left-bulkhead", "lower-left-bulkhead#m", False, True)
    frame.addTube(RD_1x49, RD_1x49, "upper-left-bulkhead", "upper-left-frontbox", True, True)
    frame.addTube(RD_1x49, RD_1x49, "lower-left-bulkhead", "lower-left-frontbox", True, True)
    frame.addTube(RD_1x49, RD_1x49, "lower-left-bulkhead", "upper-left-frontbox", True, True)
    frame.addTube(RD_1x49, RD_1x49, "upper-left-bulkhead", "upper-left-fronthoop", True, True)
    frame.addTube(SQ_1x35, SQ_1x35, "lower-left-frontbrace", "lower-left-frontbrace#m", False, True)
    frame.addTube(SQ_1x35, SQ_1x35, "lower-aft-middle-frontbrace", "lower-foremost-middle-frontbrace", False, True)
    frame.addTube(RD_1x65, RD_1x65, "upper-left-frontbox", "upper-left-fronthoop", True, True)
    frame.addTube(RD_1x65, RD_1x65, "upper-left-frontbox", "mid-left-fronthoop", True, True)
    frame.addTube(RD_1x35, RD_1x35, "upper-left-frontbox", "lower-left-frontbox", True, True)
    frame.addTube(RD_1x49, RD_1x49, "lower-left-frontbox", "lower-left-fronthoop", True, True)
    frame.addTube(RD_1x35, RD_1x35, "lower-left-frontbox", "lower-left-fronthoop#m", False, True)
    frame.addTube(RD_1x35, RD_1x35, "lower-left-fronthoop", "lower-left-frontbox#m", False, True)
    frame.addTube(RD_1x95, RD_1x95, "lower-left-fronthoop", "mid-left-fronthoop", True, True)
    frame.addTube(RD_1x95, RD_1x95, "upper-left-fronthoop", "mid-left-fronthoop", True, True)
    frame.addTube(RD_1x95, RD_1x95, "upper-left-fronthoop", "upper-left-fronthoop#m", False, True)

    # After Fronthoop -> Mainhoop
    frame.addTube(RD_1x65, RD_1x65, "upper-left-fronthoop", "fore-upper-sideimpact", True, True)
    frame.addTube(RD_1x65, RD_1x65, "mid-left-fronthoop", "fore-upper-sideimpact", True, True)
    frame.addTube(RD_1x65, RD_1x65, "lower-left-fronthoop", "fore-upper-sideimpact", True, True)
    frame.addTube(RD_1x65, RD_1x65, "lower-left-fronthoop", "fore-lower-sideimpact", True, True)
    frame.addTube(RD_1x65, RD_1x65, "fore-upper-sideimpact", "fore-lower-sideimpact", True, True)
    frame.addTube(RD_1x65, RD_1x65, "lower-left-mainhoop", "fore-lower-sideimpact", True, True)
    frame.addTube(RD_1x65, RD_1x65, "mid-left-mainhoop", "fore-upper-sideimpact", True, True)
    frame.addTube(RD_5x35, RD_5x35, "fore-sideimpact-brace", "aft-sideimpact-brace", True, True)
    frame.addTube(RD_5x35, RD_5x35, "mid-upper-sideimpact-brace", "mid-lower-sideimpact-brace", True, True)
    frame.addTube(RD_1x35, RD_1x35, "lower-left-fronthoop", "fore-lower-sideimpact#m", False, True)
    frame.addTube(RD_1x35, RD_1x35, "fore-lower-sideimpact", "lower-left-fronthoop#m", False, True)
    frame.addTube(RD_1x35, RD_1x35, "fore-lower-sideimpact", "lower-left-mainhoop#m", False, True)
    frame.addTube(RD_1x35, RD_1x35, "lower-left-mainhoop", "fore-lower-sideimpact#m", False, True)
    frame.addTube(RD_1x95, RD_1x95, "lower-left-mainhoop", "mid-left-mainhoop", True, True)
    frame.addTube(RD_1x95, RD_1x95, "mid-left-mainhoop", "left-brace-mainhoop", True, True)
    frame.addTube(RD_1x95, RD_1x95, "left-brace-mainhoop", "upper-left-mainhoop", True, True)
    frame.addTube(RD_1x95, RD_1x95, "upper-left-mainhoop", "nipple-mainhoop", False, True)
    frame.addTube(RD_1x95, RD_1x95, "upper-left-mainhoop#m", "nipple-mainhoop", False, True)
    frame.addTube(RD_1x95, RD_1x95, "left-harnessbar", "end-of-bend-harnessbar", True, True)
    frame.addTube(RD_1x95, RD_1x95, "end-of-bend-harnessbar", "end-of-bend-harnessbar#m", False, True)

    # After Mainhoop -> Rear
    frame.addTube(RD_1x35, RD_1x35, "mid-left-mainhoop", "left-foremost-enginemount", True, True)
    frame.addTube(RD_1x35, RD_1x35, "left-harnessbar", "left-foremost-enginemount", True, True)
    frame.addTube(RD_1x65, RD_1x65, "left-brace-mainhoop", "left-upper-foremost-rear-suspension", True, True)
    frame.addTube(RD_1x49, RD_1x49, "mid-left-mainhoop", "left-upper-foremost-rear-suspension", True, True)
    frame.addTube(RD_1x49, RD_1x49, "lower-left-mainhoop", "left-upper-foremost-rear-suspension", True, True)
    frame.addTube(RD_1x35, RD_1x35, "lower-left-mainhoop", "left-lower-foremost-rear-suspension", True, True)
    frame.addTube(RD_1x35, RD_1x35, "left-lower-foremost-rear-suspension", "left-upper-foremost-rear-suspension", True,
                  True)
    frame.addTube(RD_1x49, RD_1x49, "left-upper-foremost-rear-suspension", "left-upper-aft-rear-suspension", True, True)
    frame.addTube(RD_1x35, RD_1x35, "left-lower-foremost-rear-suspension", "left-lower-aft-rear-suspension", True, True)
    frame.addTube(RD_1x35, RD_1x35, "left-lower-aft-rear-suspension", "left-upper-foremost-rear-suspension", True, True)
    frame.addTube(RD_1x35, RD_1x35, "left-lower-aft-rear-suspension", "left-lower-aft-enginemount", True, True)
    frame.addTube(RD_1x35, RD_1x35, "left-upper-aft-enginemount", "left-upper-aft-rear-suspension", True, True)
    frame.addTube(RD_5x35, RD_5x35, "left-lower-foremost-rear-suspension", "left-lower-aft-rear-suspension#m", False,
                  True)
    frame.addTube(RD_5x35, RD_5x35, "left-lower-aft-rear-suspension", "left-lower-foremost-rear-suspension#m", False,
                  True)
    frame.addTube(RD_5x35, RD_5x35, "right-rear-enginebrace", "rear-crossbrace", False, True)

    # Engine Tubes
    frame.addTube(RD_1xSLD, RD_1xSLD, "left-upper-aft-enginemount", "left-lower-aft-enginemount", True, True)
    frame.addTube(RD_1xSLD, RD_1xSLD, "left-upper-aft-enginemount", "left-lower-aft-enginemount#m", False, True)
    frame.addTube(RD_1xSLD, RD_1xSLD, "left-upper-aft-enginemount", "left-foremost-enginemount", False, True)
    frame.addTube(RD_1xSLD, RD_1xSLD, "left-upper-aft-enginemount", "left-foremost-enginemount#m", False, True)
    frame.addTube(RD_1xSLD, RD_1xSLD, "left-upper-aft-enginemount", "left-upper-aft-enginemount#m", False, True)

    frame.addTube(RD_1xSLD, RD_1xSLD, "left-upper-aft-enginemount#m", "left-lower-aft-enginemount", False, True)
    frame.addTube(RD_1xSLD, RD_1xSLD, "left-upper-aft-enginemount#m", "left-foremost-enginemount", False, True)
    frame.addTube(RD_1xSLD, RD_1xSLD, "left-upper-aft-enginemount#m", "left-foremost-enginemount-#m", False, True)

    frame.addTube(RD_1xSLD, RD_1xSLD, "left-foremost-enginemount", "left-foremost-enginemount-#m", False, True)
    frame.addTube(RD_1xSLD, RD_1xSLD, "left-foremost-enginemount", "left-lower-aft-enginemount", False, True)
    frame.addTube(RD_1xSLD, RD_1xSLD, "left-foremost-enginemount", "left-lower-aft-enginemount#m", False, True)

    frame.addTube(RD_1xSLD, RD_1xSLD, "left-foremost-enginemount#m", "left-lower-aft-enginemount", False, True)
    frame.addTube(RD_1xSLD, RD_1xSLD, "left-foremost-enginemount#m", "left-lower-aft-enginemount#m", False, True)

    frame.addTube(RD_1xSLD, RD_1xSLD, "left-lower-aft-enginemount", "left-lower-aft-enginemount#m", False, True)

    return frame










