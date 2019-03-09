from tubeSizes import *
from frame import *

def createBaseFrame():

    frame = Frame()


    # note you should add groups, like for main-hoop, so it stays vertical but can move in x
    # symmetric pair could be a type of group

    # especially useful for tubes modelled as multiple tubes, but are actually one tube (i.e. roll hoop)


    frame.addNode("upper-left-bulkhead", 17.852, -6.929, 17.195, True, True)
    frame.addNode("lower-left-bulkhead", 17.852, -6.929, 4.82, True, True)
    frame.addNode("upper-fore-left-frontbox", 33.203, -8.69, 8.932, True, True)
    frame.addNode("lower-fore-left-frontbox", 33.652, -6.929, 4.82, True, True)
    frame.addNode("upper-aft-left-frontbox", 44.194, -8.584, 8.907, True, True)
    frame.addNode("lower-aft-left-frontbox", 43.97, -6.929, 4.82, True, True)
    frame.addNode("left-frontdamper", 40.2, -9, 17.25, True, True)
    frame.addNode("fore-upper-left-sideimpact", 44.731, -8.497, 12.5, True, True, 4, 0, 1, 2, 0, 0)
    frame.addNode("upper-left-fronthoop", 46.445, -6.53, 23.133, True, True, 3, 2, 1, 3, 1, 1)
    frame.addNode("mid-upper-left-sideimpact", 58.353, -10.751, 12.737, True, False, 5, 5, 2, 6, 0, 0)
    frame.addNode("left-lower-mainhoop", 73.15, -13.25, 2, True, True, 3, 0, 2, 3, 0, 0)
    frame.addNode("left-sideimpact-mainhoop", 73.15, -13.2, 12.993, True, True, 0, 0, 1, 4, 0, 0)
    frame.addNode("left-harnessbar-mainhoop", 73.15, -10.55, 23.1, True, True)
    frame.addNode("left-brace-mainhoop", 73.15, -6.273, 38.5, True, True, 0, 0, 0, 2, 0, 2)
    frame.addNode("nipple-mainhoop", 73.15, 0, 44.2, False, True, 0, 0, 0, 0, 3, 0)
    frame.addNode("seat-crossbrace", 59.114, 0, 3.217, False, True, 1, 1, 0, 0, 1, 1)
    frame.addNode("frontbox-crossbrace", 38.811, 0, 4.82, False, True, 2, 1, 0, 0, 0, 1)
    frame.addNode("left-rockernode", 40.2, -6.929, 4.82, True, True)
    frame.addNode("engine-to-harness", 75.698,-9.598,23.1,True,True)
    frame.addNode("foremost-enginemount", 79.706, -7.6675,14.875,False,True)
    frame.addNode("end-of-bend-harness",76.65, -7.3,23.1,True,True)
    frame.addNode("upper-fore-rearbox", 93.5544,-8.6,10.944,True,True)
    frame.addNode("lower-fore-rearbox",92.265, -7.5,5.907,True,True)
    frame.addNode("lower-mid-rearbox",97.543,-6.238,4.9119,True,True)
    frame.addNode("lower-aft-rearbox",103.246, -6.2378,5.904,True,True)
    frame.addNode("upper-aft-rearbox",105.572,-9.056,10.9688, True,True)
    frame.addNode("upper-mid-rearbox", 99.5,-8.8258,10.9563,True,True)
    frame.addNode("upper-rearRockerPlane", 99.5, -6.64,13.706,True,True)
    frame.addNode("pyramid",99.5,0,17,False,True)
    frame.addNode("upper-aft-enginemount", 93.5233,-4.2625,16.4,True,True)
    frame.addNode("lower-aft-enginemount",93.5413, -3.6565,7.177,True,True)
    frame.addNode("foremost-enginemount-mirror", 79.03,7.648,14.38,False,True)

    frame.addTube(SQ_1x49, SQ_1x49, "upper-left-bulkhead","lower-left-bulkhead", True, True)
    frame.addTube(SQ_1x49, SQ_1x49, "upper-left-bulkhead", "upper-left-bulkhead#m", False, True)
    frame.addTube(SQ_1x49, SQ_1x49, "lower-left-bulkhead", "lower-left-bulkhead#m", False, True)
    frame.addTube(RD_1x65, RD_1x65, "upper-left-bulkhead", "upper-left-fronthoop", True, True)
    frame.addTube(RD_1x49, RD_1x49, "upper-left-bulkhead", "upper-fore-left-frontbox", True, True)
    frame.addTube(RD_1x49, RD_1x49, "lower-left-bulkhead", "upper-fore-left-frontbox", True, True)

    # the rest (besides roll hoops) have been left with no minimum size as proof of concept
    frame.addTube(RD_1x49, RD_5x35, "lower-left-bulkhead", 'lower-fore-left-frontbox', True, True, "LowerFrontAArm")
    frame.addTube(RD_1x49, RD_5x35, "lower-fore-left-frontbox", "left-rockernode", True, True, "LowerFrontAArm")
    frame.addTube(RD_1x49, RD_5x35, "left-rockernode", "lower-aft-left-frontbox", True, True, "LowerFrontAArm")
    frame.addTube(RD_1x49, RD_5x35, "lower-fore-left-frontbox", "upper-fore-left-frontbox", True, True)
    frame.addTube(RD_1x49, RD_5x35, "lower-fore-left-frontbox", "upper-aft-left-frontbox", True, True)
    frame.addTube(RD_1x49, RD_5x35, "upper-fore-left-frontbox", "upper-aft-left-frontbox", True, True)
    frame.addTube(RD_1x49, RD_5x35, "upper-fore-left-frontbox", "fore-upper-left-sideimpact", True, True)
    frame.addTube(RD_1x49, RD_5x35, "upper-fore-left-frontbox", "left-frontdamper", True, True)
    frame.addTube(RD_1x49, RD_5x35, "left-frontdamper", "upper-left-fronthoop", True, True)
    frame.addTube(RD_75x35, RD_5x35, "left-frontdamper", "fore-upper-left-sideimpact", True, True)

    # front roll hoop
    frame.addTube(RD_1x95, RD_1x95, "lower-aft-left-frontbox", "upper-aft-left-frontbox", True, True, "FrontRollHoop")
    frame.addTube(RD_1x95, RD_1x95, "upper-aft-left-frontbox", "fore-upper-left-sideimpact",True, True, "FrontRollHoop")
    frame.addTube(RD_1x95, RD_1x95, "fore-upper-left-sideimpact", "upper-left-fronthoop", True, True, "FrontRollHoop")
    frame.addTube(RD_1x95, RD_1x95, "upper-left-fronthoop", "upper-left-fronthoop#m", False, True, "FrontRollHoop")

    frame.addTube(RD_75x35, RD_5x35, "upper-left-fronthoop", "mid-upper-left-sideimpact", True, True)
    frame.addTube(RD_1x65, RD_5x35, "fore-upper-left-sideimpact", "mid-upper-left-sideimpact", True, True, "UpperSideImpact")
    frame.addTube(RD_75x35, RD_5x35, "upper-aft-left-frontbox", "mid-upper-left-sideimpact", True, True)
    frame.addTube(RD_1x65, RD_5x35, "lower-aft-left-frontbox", "mid-upper-left-sideimpact", True, True)
    frame.addTube(RD_1x65, RD_5x35, "lower-aft-left-frontbox", "left-lower-mainhoop", True, True)
    frame.addTube(RD_1x65, RD_5x35, "mid-upper-left-sideimpact", "left-sideimpact-mainhoop", True, True, "UpperSideImpact")

    # main roll hoop
    frame.addTube(RD_1x95, RD_1x95, "left-lower-mainhoop", "left-sideimpact-mainhoop", True, True, "MainRollHoop")
    frame.addTube(RD_1x95, RD_1x95, "left-sideimpact-mainhoop", "left-harnessbar-mainhoop", True, True, "MainRollHoop")
    frame.addTube(RD_1x95, RD_1x95, "left-harnessbar-mainhoop", "left-brace-mainhoop", True, True, "MainRollHoop")
    frame.addTube(RD_1x95, RD_1x95, "left-brace-mainhoop", "nipple-mainhoop", False, True, "MainRollHoop")
    frame.addTube(RD_1x95, RD_1x95, "nipple-mainhoop", "left-brace-mainhoop#m", False, True, "MainRollHoop")

    # crossbraces
    frame.addTube(RD_75x35, RD_5x35, "left-lower-mainhoop", "seat-crossbrace", False, True, "Crossbrace5")
    frame.addTube(RD_75x35, RD_5x35, "left-lower-mainhoop#m", "seat-crossbrace", False, True, "Crossbrace5")
    frame.addTube(RD_75x35, RD_5x35, "lower-aft-left-frontbox", "seat-crossbrace", False, True, "Crossbrace4")
    frame.addTube(RD_75x35, RD_5x35, "lower-aft-left-frontbox#m", "seat-crossbrace", False, True, "Crossbrace4")

    # use these to test the isRequired property
    frame.addTube(RD_75x35, RD_5x35, "lower-aft-left-frontbox", "frontbox-crossbrace", False, False, "Crossbrace3")
    frame.addTube(RD_75x35, RD_5x35, "lower-aft-left-frontbox#m", "frontbox-crossbrace", False, False, "Crossbrace3")
    frame.addTube(RD_1x35, RD_5x35, "left-rockernode", "frontbox-crossbrace", False, False, "Crossbrace2")
    frame.addTube(RD_1x35, RD_5x35, "left-rockernode#m", "frontbox-crossbrace", False, False, "Crossbrace2")
    frame.addTube(RD_75x35, RD_5x35, "lower-fore-left-frontbox", "frontbox-crossbrace", False, False, "Crossbrace1")
    frame.addTube(RD_75x35, RD_5x35, "lower-fore-left-frontbox#m", "frontbox-crossbrace", False, False, "Crossbrace1")

    frame.addTube(RD_1x35, RD_5x35, "left-sideimpact-mainhoop", "engine-to-harness", True, True)
    frame.addTube(RD_5x35, RD_5x35, "engine-to-harness", "foremost-enginemount", False, True)
    frame.addTube(RD_5x35, RD_5x35, "foremost-enginemount-mirror", "engine-to-harness#m", False, True)
    frame.addTube(RD_1x35, RD_5x35, "left-sideimpact-mainhoop", "foremost-enginemount", False, True)
    frame.addTube(RD_1x35, RD_5x35, "left-sideimpact-mainhoop#m", "foremost-enginemount-mirror", False, True)
    frame.addTube(RD_1x65, RD_5x35, "left-brace-mainhoop", "upper-fore-rearbox", True, True)
    frame.addTube(RD_1x35, RD_5x35, "left-lower-mainhoop", "lower-fore-rearbox", True, True)
    frame.addTube(RD_1x49, RD_5x35, "left-lower-mainhoop", "upper-fore-rearbox", True, True)
    frame.addTube(RD_1x49, RD_5x35, "left-sideimpact-mainhoop", "upper-fore-rearbox", True, True)
    frame.addTube(RD_1x95, RD_1x95, "left-harnessbar-mainhoop", "engine-to-harness", True, True, "HarnessBar")
    frame.addTube(RD_1x95, RD_1x95, "engine-to-harness", "end-of-bend-harness", True, True, "HarnessBar")
    frame.addTube(RD_1x95, RD_1x95, "end-of-bend-harness", "end-of-bend-harness#m", False, True, "HarnessBar")
    frame.addTube(RD_75x35, RD_5x35, "upper-fore-rearbox", "lower-fore-rearbox", True, True)
    frame.addTube(RD_75x35, RD_5x35, "upper-fore-rearbox", "lower-mid-rearbox", True, True)
    frame.addTube(RD_75x35, RD_5x35, "lower-mid-rearbox", "upper-aft-rearbox", True, True)
    frame.addTube(RD_75x35, RD_5x35, "upper-aft-rearbox", "lower-aft-rearbox", True, True)
    frame.addTube(RD_75x49, RD_5x35, "lower-fore-rearbox", "lower-aft-enginemount", True, True)
    frame.addTube(RD_5x35, RD_5x35, "lower-aft-enginemount", "lower-mid-rearbox", True, True)
    frame.addTube(RD_1x49, RD_5x35, "lower-aft-rearbox", "lower-aft-rearbox#m", False, True)
    frame.addTube(RD_1x49, RD_5x35, "upper-aft-rearbox", "upper-aft-rearbox#m", False, True)
    frame.addTube(RD_1x49, RD_5x35, "upper-fore-rearbox", "upper-mid-rearbox", True, True, "UpperRearbox")
    frame.addTube(RD_1x49, RD_5x35, "upper-mid-rearbox", "upper-aft-rearbox", True, True, "upperRearbox")
    frame.addTube(RD_1x35, RD_5x35, "upper-fore-rearbox", "upper-aft-enginemount", True, True)
    frame.addTube(RD_1x35, RD_5x35, "upper-fore-rearbox", "upper-rearRockerPlane", True, True)
    frame.addTube(RD_1x35, RD_5x35, "upper-rearRockerPlane", "upper-aft-enginemount", True, True, "toEngineMount")
    frame.addTube(RD_1x35, RD_5x35, "upper-rearRockerPlane", "upper-aft-rearbox", True, True, "toEngineMount")
    frame.addTube(RD_5x49, RD_5x35, "upper-mid-rearbox", "upper-rearRockerPlane", True, False)
    frame.addTube(RD_5x35, RD_5x35, "upper-rearRockerPlane", "pyramid", False, False)
    frame.addTube(RD_5x35, RD_5x35, "upper-rearRockerPlane#m", "pyramid", False, False)
    frame.addTube(RD_1x35, RD_5x35, "upper-aft-rearbox", "pyramid", False, False)
    frame.addTube(RD_1x35, RD_5x35, "upper-aft-rearbox#m", "pyramid", False, False)
    frame.addTube(RD_1x35, RD_5x35, "upper-aft-enginemount", "pyramid", False, False)
    frame.addTube(RD_1x35, RD_5x35, "upper-aft-enginemount#m", "pyramid", False, False)
    frame.addTube(RD_1x49, RD_5x35, "lower-fore-rearbox", "lower-mid-rearbox",True,True)
    frame.addTube(RD_1x49, RD_5x35, "lower-mid-rearbox","lower-aft-rearbox",True,True)

    # Engine tubes
    frame.addTube(RD_1xSLD, RD_1xSLD, "upper-aft-enginemount", "lower-aft-enginemount", True, True)
    frame.addTube(RD_1xSLD, RD_1xSLD,"upper-aft-enginemount","lower-aft-enginemount#m",False,True)
    frame.addTube(RD_1xSLD, RD_1xSLD, "upper-aft-enginemount", "foremost-enginemount", False, True)
    frame.addTube(RD_1xSLD, RD_1xSLD, "upper-aft-enginemount", "foremost-enginemount-mirror", False, True)
    frame.addTube(RD_1xSLD, RD_1xSLD, "upper-aft-enginemount", "upper-aft-enginemount#m", False, True)

    frame.addTube(RD_1xSLD, RD_1xSLD, "upper-aft-enginemount#m", "lower-aft-enginemount", False, True)
    frame.addTube(RD_1xSLD, RD_1xSLD, "upper-aft-enginemount#m", "foremost-enginemount", False, True)
    frame.addTube(RD_1xSLD, RD_1xSLD, "upper-aft-enginemount#m", "foremost-enginemount-mirror", False, True)

    frame.addTube(RD_1xSLD, RD_1xSLD, "foremost-enginemount", "foremost-enginemount-mirror", False, True)
    frame.addTube(RD_1xSLD, RD_1xSLD, "foremost-enginemount", "lower-aft-enginemount", False, True)
    frame.addTube(RD_1xSLD, RD_1xSLD, "foremost-enginemount", "lower-aft-enginemount#m", False, True)

    frame.addTube(RD_1xSLD, RD_1xSLD, "foremost-enginemount-mirror", "lower-aft-enginemount", False, True)
    frame.addTube(RD_1xSLD, RD_1xSLD, "foremost-enginemount-mirror", "lower-aft-enginemount#m", False, True)

    frame.addTube(RD_1xSLD, RD_1xSLD, "lower-aft-enginemount", "lower-aft-enginemount#m", False, True)

    return frame