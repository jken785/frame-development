from tubeSizes import *
from frame import *


def createBaseFrame():
    frame = Frame()

    # note you should add groups, like for main-hoop, so it stays vertical but can move in x
    # symmetric pair could be a type of group

    # especially useful for tubes modelled as multiple tubes, but are actually one tube (i.e. roll hoop)

    frame.addNode("upper-left-bulkhead", 17.016, -7.472, 17.675, True, True)
    frame.addNode("lower-left-bulkhead", 17.016, -7.472, 5.3, True, True)
    frame.addNode("upper-fore-left-frontbox", 32.770, -7.802, 9.532, True, True)
    frame.addNode("lower-fore-left-frontbox", 33.816, -7.372, 5.3, True, True)
    frame.addNode("upper-aft-left-frontbox", 44.464, -7.802, 9.532, True, True)
    frame.addNode("lower-aft-left-frontbox", 43.903, -7.372, 5.3, True, True)
    frame.addNode("left-frontdamper", 40.2, -8.999, 17.249, True, True)
    frame.addNode("fore-upper-left-sideimpact", 44.728, -8.004, 11.524, True, True, 4, 0, 1, 2, 0, 0)
    frame.addNode("upper-left-fronthoop", 46.192, -5.982, 22.572, True, True, 3, 2, 1, 3, 1, 1)
    frame.addNode("mid-upper-left-sideimpact", 56.6, -10.158, 12.134, True, False, 5, 5, 2, 6, 0, 0)
    frame.addNode("left-lower-mainhoop", 73.35, -13.25, 2, True, True, 0, 0, 2, 3, 0, 0, "MainHoop")
    frame.addNode("left-sideimpact-mainhoop", 73.35, -13.250, 13, True, True, 0, 0, 1, 4, 0, 0, "MainHoop")
    frame.addNode("left-harnessbar-mainhoop", 73.35, -10.550, 24.017, True, True, "MainHoop")
    frame.addNode("left-brace-mainhoop", 73.35, -6.729, 38.7, True, True, 0, 0, 0, 2, 0, 2, "MainHoop")
    frame.addNode("nipple-mainhoop", 73.35, 0, 44.4, False, True, 0, 0, 0, 0, 3, 1, "MainHoop")
    frame.addNode("seat-crossbrace", 58.9, 0, 3.747, False, True, 1, 1, 0, 0, 1, 1)
    frame.addNode("frontbox-crossbrace", 40.2, 0, 5.3, False, True, 2, 1, 0, 0, 0, 1)
    frame.addNode("left-rockernode", 40.200, -7.372, 5.3, True, True)
    frame.addNode("engine-to-harness", 75.898, -9.598, 24.017, True, True)
    frame.addNode("foremost-enginemount", 79.906, -8.093, 14.250, False, True)
    frame.addNode("end-of-bend-harness", 76.85, -7.3, 24.017, True, True)
    frame.addNode("upper-fore-rearbox", 93.168, -8.594, 10.839, True, True)
    frame.addNode("lower-fore-rearbox", 92.861, -6.241, 5.696, True, True)
    frame.addNode("lower-mid-rearbox", 98.62, -6.394, 4.198, True, True)
    frame.addNode("lower-aft-rearbox", 105.870, -6.394, 5.695, True, True)
    frame.addNode("upper-aft-rearbox", 106.473, -8.818, 10.854, True, True)
    frame.addNode("upper-mid-rearbox", 99.5, -8.701, 10.846, True, True)
    frame.addNode("upper-rearRockerPlane", 99.5, -6.819, 13.545, True, True, 1, 1, 1, 1, 2, 1, "RockerPlane")
    frame.addNode("rear-arb", 99.5, -2.45, 15, True, True, 1, 1, 0, 0, 3, 0, "RockerPlane")
    frame.addNode("fore-rear-arb", 99.5, -1.2, 15, True, True)
    frame.addNode("aft-rear-arb", 99.5, -0.7, 15.5, True, True)
    frame.addNode("upper-aft-enginemount", 93.723, -5.263, 15.775, False, True)
    frame.addNode("upper-aft-enginemount-mirror", 93.723, 4.952, 15.775, False, True)
    frame.addNode("lower-aft-enginemount", 93.741, -4.907, 6.552, True, True)
    frame.addNode("foremost-enginemount-mirror", 79.23, 8.092, 13.755, False, True)
    frame.addNode("rear-v-towbar", 105.87, 0, 5.77, False, True)
    frame.addNode("sideimpact-driverbrace", 51.245, -8.012, 17.505, True, True)
    frame.addNode("mainhoop-driverbrace", 73.350, -12.146, 17.505, True, True)
    frame.addNode("sideimpact-driverbrace-uppersupport", 62.297, -10.079, 17.505, True, True)
    frame.addNode("sideimpact-driverbrace-lowersupport", 62.297, -11.198, 12.427, True, True)
    frame.addNode("fronthoop-steeringwheelmount", 46.381, -1.879, 24.000, True, True)
    frame.addNode("steeringwheel", 47.941, 0, 18.282, False, True)

    frame.addTube(SQ_1x49, SQ_1x49, "upper-left-bulkhead", "lower-left-bulkhead", True, True)
    frame.addTube(SQ_1x49, SQ_1x49, "upper-left-bulkhead", "upper-left-bulkhead#m", False, True)
    frame.addTube(SQ_1x49, SQ_1x49, "lower-left-bulkhead", "lower-left-bulkhead#m", False, True)
    frame.addTube(RD_1x65, RD_1x65, "upper-left-bulkhead", "upper-left-fronthoop", True, True)
    frame.addTube(RD_1x49, RD_1x49, "upper-left-bulkhead", "upper-fore-left-frontbox", True, True)
    frame.addTube(RD_1x49, RD_1x49, "lower-left-bulkhead", "upper-fore-left-frontbox", True, True)

    # the rest (besides roll hoops)
    frame.addTube(RD_1x49, RD_1x49, "lower-left-bulkhead", 'lower-fore-left-frontbox', True, True, "LowerFrontAArm")
    frame.addTube(RD_1x49, RD_1x49, "lower-fore-left-frontbox", "left-rockernode", True, True, "LowerFrontAArm")
    frame.addTube(RD_1x49, RD_1x49, "left-rockernode", "lower-aft-left-frontbox", True, True, "LowerFrontAArm")
    frame.addTube(RD_1x49, RD_1x49, "lower-fore-left-frontbox", "upper-fore-left-frontbox", True, True)
    frame.addTube(RD_1x49, RD_1x49, "lower-fore-left-frontbox", "upper-aft-left-frontbox", True, True)
    frame.addTube(RD_1x49, RD_1x49, "upper-fore-left-frontbox", "upper-aft-left-frontbox", True, True)
    frame.addTube(RD_1x49, RD_5x35, "upper-fore-left-frontbox", "fore-upper-left-sideimpact", True, True)
    frame.addTube(RD_1x35, RD_5x35, "upper-fore-left-frontbox", "left-frontdamper", True, True)
    frame.addTube(RD_1x35, RD_5x35, "left-frontdamper", "upper-left-fronthoop", True, True)
    frame.addTube(RD_1x49, RD_5x35, "left-frontdamper", "fore-upper-left-sideimpact", True, True)

    # front roll hoop
    frame.addTube(RD_1x95, RD_1x95, "lower-aft-left-frontbox", "upper-aft-left-frontbox", True, True, "FrontRollHoop")
    frame.addTube(RD_1x95, RD_1x95, "upper-aft-left-frontbox", "fore-upper-left-sideimpact", True, True,
                  "FrontRollHoop")
    frame.addTube(RD_1x95, RD_1x95, "fore-upper-left-sideimpact", "upper-left-fronthoop", True, True, "FrontRollHoop")
    frame.addTube(RD_1x95, RD_1x95, "upper-left-fronthoop", "upper-left-fronthoop#m", False, True, "FrontRollHoop")

    frame.addTube(RD_75x28, RD_375x28, "upper-left-fronthoop", "mid-upper-left-sideimpact", True, True)
    frame.addTube(SQ_1x49, RD_375x28, "fore-upper-left-sideimpact", "mid-upper-left-sideimpact", True, True,
                  "UpperSideImpact")
    frame.addTube(SQ_1x49, RD_375x28, "lower-aft-left-frontbox", "mid-upper-left-sideimpact", True, True)
    frame.addTube(SQ_1x49, RD_375x28, "lower-aft-left-frontbox", "left-lower-mainhoop", True, True)
    frame.addTube(SQ_1x49, RD_375x28, "mid-upper-left-sideimpact", "left-sideimpact-mainhoop", True, True,
                  "UpperSideImpact")
    frame.addTube(SQ_1x49, RD_375x28, "mid-upper-left-sideimpact", "left-lower-mainhoop", True, True)

    # main roll hoop
    frame.addTube(RD_1x95, RD_1x95, "left-lower-mainhoop", "left-sideimpact-mainhoop", True, True, "MainRollHoop")
    frame.addTube(RD_1x95, RD_1x95, "left-sideimpact-mainhoop", "left-harnessbar-mainhoop", True, True, "MainRollHoop")
    frame.addTube(RD_1x95, RD_1x95, "left-harnessbar-mainhoop", "left-brace-mainhoop", True, True, "MainRollHoop")
    frame.addTube(RD_1x95, RD_1x95, "left-brace-mainhoop", "nipple-mainhoop", False, True, "MainRollHoop")
    frame.addTube(RD_1x95, RD_1x95, "nipple-mainhoop", "left-brace-mainhoop#m", False, True, "MainRollHoop")

    # crossbraces
    frame.addTube(RD_75x35, RD_375x28, "left-lower-mainhoop", "seat-crossbrace", False, True, "Crossbrace5")
    frame.addTube(RD_75x35, RD_375x28, "left-lower-mainhoop#m", "seat-crossbrace", False, True, "Crossbrace5")
    frame.addTube(RD_75x35, RD_375x28, "lower-aft-left-frontbox", "seat-crossbrace", False, True, "Crossbrace4")
    frame.addTube(RD_75x35, RD_375x28, "lower-aft-left-frontbox#m", "seat-crossbrace", False, True, "Crossbrace4")

    # use these to test the isRequired property
    frame.addTube(SQ_625x35, RD_375x28, "lower-aft-left-frontbox", "frontbox-crossbrace", False, False, "Crossbrace3")
    frame.addTube(SQ_625x35, RD_375x28, "lower-aft-left-frontbox#m", "frontbox-crossbrace", False, False, "Crossbrace3")
    frame.addTube(SQ_1x35, RD_375x28, "left-rockernode", "frontbox-crossbrace", False, False, "Crossbrace2")
    frame.addTube(SQ_1x35, RD_375x28, "left-rockernode#m", "frontbox-crossbrace", False, False, "Crossbrace2")
    frame.addTube(RD_625x28, RD_375x28, "lower-fore-left-frontbox", "lower-fore-left-frontbox#m", False, False,
                  "Crossbrace1")

    frame.addTube(RD_1x49, RD_375x28, "left-sideimpact-mainhoop", "engine-to-harness", True, True)
    frame.addTube(RD_625x28, RD_375x28, "engine-to-harness", "foremost-enginemount", False, True)
    frame.addTube(RD_625x28, RD_375x28, "foremost-enginemount-mirror", "engine-to-harness#m", False, True)
    frame.addTube(RD_1x49, RD_375x28, "left-sideimpact-mainhoop", "foremost-enginemount", False, True)
    frame.addTube(RD_1x49, RD_375x28, "left-sideimpact-mainhoop#m", "foremost-enginemount-mirror", False, True)
    frame.addTube(RD_1x65, RD_375x28, "left-brace-mainhoop", "upper-fore-rearbox", True, True)
    frame.addTube(RD_1x35, RD_375x28, "left-lower-mainhoop", "lower-fore-rearbox", True, True)
    frame.addTube(RD_1x49, RD_375x28, "left-lower-mainhoop", "upper-fore-rearbox", True, True)
    frame.addTube(RD_1x49, RD_375x28, "left-sideimpact-mainhoop", "upper-fore-rearbox", True, True)
    frame.addTube(RD_1x95, RD_1x95, "left-harnessbar-mainhoop", "engine-to-harness", True, True, "HarnessBar")
    frame.addTube(RD_1x95, RD_1x95, "engine-to-harness", "end-of-bend-harness", True, True, "HarnessBar")
    frame.addTube(RD_1x95, RD_1x95, "end-of-bend-harness", "end-of-bend-harness#m", False, True, "HarnessBar")
    frame.addTube(RD_625x49, RD_375x28, "upper-fore-rearbox", "lower-fore-rearbox", True, True)
    frame.addTube(RD_75x35, RD_375x28, "upper-fore-rearbox", "lower-mid-rearbox", True, True)
    frame.addTube(RD_75x35, RD_375x28, "lower-mid-rearbox", "upper-aft-rearbox", True, True)
    frame.addTube(RD_625x49, RD_375x28, "upper-aft-rearbox", "lower-aft-rearbox", True, True)
    frame.addTube(RD_75x49, RD_375x28, "lower-fore-rearbox", "lower-aft-enginemount", True, True)
    frame.addTube(RD_625x49, RD_375x28, "lower-aft-enginemount", "lower-mid-rearbox", False, True)
    frame.addTube(RD_5x49, RD_375x28, "lower-aft-enginemount#m", "lower-mid-rearbox#m", False, True)
    frame.addTube(RD_1x35, RD_375x28, "lower-aft-rearbox", "lower-aft-rearbox#m", False, True)
    frame.addTube(RD_75x35, RD_375x28, "upper-aft-rearbox", "rear-v-towbar", False, True)
    frame.addTube(RD_75x35, RD_375x28, "upper-aft-rearbox#m", "rear-v-towbar", False, True)
    frame.addTube(RD_1x49, RD_375x28, "upper-fore-rearbox", "upper-mid-rearbox", True, True, "UpperRearbox")
    frame.addTube(RD_1x49, RD_375x28, "upper-mid-rearbox", "upper-aft-rearbox", True, True, "upperRearbox")
    frame.addTube(RD_1x35, RD_375x28, "upper-fore-rearbox", "upper-aft-enginemount", False, True)
    frame.addTube(RD_1x35, RD_375x28, "upper-fore-rearbox#m", "upper-aft-enginemount-mirror", False, True)
    frame.addTube(RD_625x35, RD_375x28, "upper-fore-rearbox", "upper-rearRockerPlane", True, True)
    frame.addTube(RD_1x35, RD_375x28, "upper-rearRockerPlane", "upper-aft-enginemount", False, True, "toEngineMount")
    frame.addTube(RD_1x35, RD_375x28, "upper-rearRockerPlane#m", "upper-aft-enginemount-mirror", False, True,
                  "toEngineMount")
    frame.addTube(RD_1x35, RD_375x28, "upper-rearRockerPlane", "upper-aft-rearbox", True, True, "toEngineMount")
    frame.addTube(RD_5x35, RD_375x28, "upper-mid-rearbox", "upper-rearRockerPlane", True, False)
    frame.addTube(RC_1x1_5x65, RD_375x28, "rear-arb", "rear-arb#m", False, False)
    frame.addTube(RD_625x49, RD_375x28, "upper-aft-enginemount", "rear-arb", False, False)
    frame.addTube(RD_625x49, RD_375x28, "upper-aft-enginemount-mirror", "rear-arb#m", False, False)
    frame.addTube(RD_75x35, RD_375x28, "upper-aft-rearbox", "rear-arb", True, False)
    frame.addTube(RD_1x49, RD_375x28, "lower-fore-rearbox", "lower-mid-rearbox", True, True)
    frame.addTube(RD_1x49, RD_375x28, "lower-mid-rearbox", "lower-aft-rearbox", True, True)
    frame.addTube(SQ_1x35, RD_375x28, "fronthoop-steeringwheelmount", "steeringwheel", False, False)
    frame.addTube(SQ_1x35, RD_375x28, "fronthoop-steeringwheelmount#m", "steeringwheel", False, False)
    frame.addTube(RD_5x28, RD_375x28, "sideimpact-driverbrace", "sideimpact-driverbrace-uppersupport", True, True)
    frame.addTube(RD_5x28, RD_375x28, "mainhoop-driverbrace", "sideimpact-driverbrace-uppersupport", True, True)
    frame.addTube(RD_375x28, RD_375x28, "sideimpact-driverbrace-lowersupport", "sideimpact-driverbrace-uppersupport", True, True)

    # Engine tubes
    frame.addTube(RD_1xSLD, RD_1xSLD, "upper-aft-enginemount", "lower-aft-enginemount", False, True)
    frame.addTube(RD_1xSLD, RD_1xSLD, "upper-aft-enginemount-mirror", "lower-aft-enginemount#m", False, True)
    frame.addTube(RD_1xSLD, RD_1xSLD, "upper-aft-enginemount", "lower-aft-enginemount#m", False, True)
    frame.addTube(RD_1xSLD, RD_1xSLD, "upper-aft-enginemount", "foremost-enginemount", False, True)
    frame.addTube(RD_1xSLD, RD_1xSLD, "upper-aft-enginemount", "foremost-enginemount-mirror", False, True)
    frame.addTube(RD_1xSLD, RD_1xSLD, "upper-aft-enginemount", "upper-aft-enginemount-mirror", False, True)

    frame.addTube(RD_1xSLD, RD_1xSLD, "upper-aft-enginemount-mirror", "lower-aft-enginemount", False, True)
    frame.addTube(RD_1xSLD, RD_1xSLD, "upper-aft-enginemount-mirror", "foremost-enginemount", False, True)
    frame.addTube(RD_1xSLD, RD_1xSLD, "upper-aft-enginemount-mirror", "foremost-enginemount-mirror", False, True)

    frame.addTube(RD_1xSLD, RD_1xSLD, "foremost-enginemount", "foremost-enginemount-mirror", False, True)
    frame.addTube(RD_1xSLD, RD_1xSLD, "foremost-enginemount", "lower-aft-enginemount", False, True)
    frame.addTube(RD_1xSLD, RD_1xSLD, "foremost-enginemount", "lower-aft-enginemount#m", False, True)

    frame.addTube(RD_1xSLD, RD_1xSLD, "foremost-enginemount-mirror", "lower-aft-enginemount", False, True)
    frame.addTube(RD_1xSLD, RD_1xSLD, "foremost-enginemount-mirror", "lower-aft-enginemount#m", False, True)

    frame.addTube(RD_1xSLD, RD_1xSLD, "lower-aft-enginemount", "lower-aft-enginemount#m", False, True)
    return frame


