from tubeSizes import *
from frame import *

def create2017Frame():

    frame = Frame()

    frame.addNode("upper-left-bulkhead", 17.07, 7.3, 18.51, True, True)
    frame.addNode("lower-left-bulkhead", 17.07, 7.35, 5.51, True, True)
    frame.addNode("pedalbar-left", 13.07, 7.98, 5.51, True, True)
    frame.addNode("upper-fore-left-frontbox", 7.07, 10.25, 13.12, True, True)
    frame.addNode("lower-fore-left-frontbox", 7.07, 8.45, 5.51, True, True)
    frame.addNode("upper-aft-left-frontbox", -5.03, 10.25, 13.12, True, True)
    frame.addNode("lower-aft-left-frontbox", -5.05, 8.45, 5.51, True, True)
    frame.addNode("left-frontdamper", 0, 8.45, 5.51, True, True)
    frame.addNode("upper-left-fronthoop", -7.8, 7.84, 23.77, True, True)
    frame.addNode("mid-upper-left-sideimpact", -24.01, 11.45, 13.19, True, True)
    frame.addNode("mid-lower-left-sideimpact", -25, 10.98, 2.04, True, True)
    frame.addNode("left-lower-mainhoop", -43, 11, 2.01, True, True)
    frame.addNode("left-sideimpact-mainhoop", -43, 12.75, 13.26, True, True)
    frame.addNode("left-harnessbar-mainhoop", -43, 10.84, 22.01, True, True)
    frame.addNode("left-brace-mainhoop", -43, 7.61, 36.79, True, True)
    frame.addNode("left-upmost-mainhoop", -43, 2.61, 42.59, True, True)
    frame.addNode("frontbox-crossbrace", 1.01, 0, 5.51, False, True)
    frame.addNode("rearbox-crossbrace", -61.35, 0, 4.53, False, True)
    frame.addNode("foremost-enginemount-left", -44.73, 7.4, 15.77, False, True)
    frame.addNode("foremost-enginemount-right", -44.05, -7.58, 15.28, False, True)
    frame.addNode("lower-aft-left-enginemount", -58.56, 4.55, 8.07, True, True)
    frame.addNode("upper-aft-left-enginemount", -58.55, 3.91, 17.29, True, True)
    frame.addNode("upper-fore-rearbox", -56.85, 9.75, 11.83, True, True)
    frame.addNode("upper-aft-rearbox", -66.554, 9.75, 11.827, True, True)
    frame.addNode("lower-fore-rearbox", -55.85, 6.52, 4.53,True, True)
    frame.addNode("lower-aft-rearbox", -66.85, 6.52, 4.53, True, True)
    frame.addNode("trampoline-left", -60.49, 5.33, 15.96, True, True)
    frame.addNode("rear-damper-left", -67.5, 0.3, 15.93, True, True)
   # frame.addNode("seat-crossbrace1", -33.99, 0, 2.02, False, True)
    #frame.addNode("seat-crossbrace2", -13.73, 0, 4, False, True)

    frame.addTube(SQ_1x49, RD_5x35, "upper-left-bulkhead","lower-left-bulkhead", True, True)
    frame.addTube(SQ_1x49, RD_5x35, "upper-left-bulkhead", "upper-left-bulkhead#m", False, True)
    frame.addTube(SQ_1x49, RD_5x35, "lower-left-bulkhead", "lower-left-bulkhead#m", False, True)

    frame.addTube(RD_1x49, RD_5x35, "upper-left-bulkhead", "upper-left-fronthoop", True, True)
    frame.addTube(RD_1x49, RD_5x35, "upper-left-bulkhead", "upper-fore-left-frontbox", True, True)
    frame.addTube(RD_1x49, RD_5x35, "lower-left-bulkhead", "upper-fore-left-frontbox", True, True)

    frame.addTube(RD_1x49, RD_5x35, "lower-left-bulkhead", 'pedalbar-left', True, True)
    frame.addTube(RD_5x49, RD_5x35, "pedalbar-left", "pedalbar-left#m", False, True)
    frame.addTube(RD_1x49, RD_5x35, "pedalbar-left", "lower-fore-left-frontbox", True, True)
    frame.addTube(RD_1x49, RD_5x35, "lower-fore-left-frontbox", "left-frontdamper", True, True)
    frame.addTube(RD_1x49, RD_5x35, "left-frontdamper", "lower-aft-left-frontbox", True, True)
    frame.addTube(RD_1x65, RD_5x35, "upper-fore-left-frontbox", "upper-aft-left-frontbox", True, True)
    frame.addTube(RD_1x65, RD_5x35, "upper-fore-left-frontbox", "upper-left-fronthoop", True, True)


    frame.addTube(RD_1x49, RD_5x35, "lower-fore-left-frontbox", "left-frontdamper", True, True, "LowerFrontAArm")
    frame.addTube(RD_1x49, RD_5x35, "left-frontdamper", "lower-aft-left-frontbox", True, True, "LowerFrontAArm")


    frame.addTube(RD_1x35, RD_5x35, "lower-fore-left-frontbox", "upper-fore-left-frontbox", True, True)
    frame.addTube(RD_1x65, RD_5x35, "upper-fore-left-frontbox", "upper-aft-left-frontbox", True, True)

    # front roll hoop
    frame.addTube(RD_1x95, RD_1x95, "lower-aft-left-frontbox", "upper-aft-left-frontbox", True, True, "FrontRollHoop")
    frame.addTube(RD_1x95, RD_1x95, "upper-aft-left-frontbox", "upper-left-fronthoop",True, True, "FrontRollHoop")
    frame.addTube(RD_1x95, RD_1x95, "upper-left-fronthoop", "upper-left-fronthoop#m", False, True, "FrontRollHoop")

    frame.addTube(RD_1x65, RD_5x35, "upper-left-fronthoop", "mid-upper-left-sideimpact", True, True)
    frame.addTube(RD_1x65, RD_5x35, "lower-aft-left-frontbox", "mid-upper-left-sideimpact", True, True)
    frame.addTube(RD_1x65, RD_5x35, "lower-aft-left-frontbox", "mid-upper-left-sideimpact", True, True)
    frame.addTube(RD_1x65, RD_5x35, "lower-aft-left-frontbox", "mid-lower-left-sideimpact", True, True)
    frame.addTube(RD_1x65, RD_5x35, "mid-lower-left-sideimpact", "left-lower-mainhoop", True, True)
    frame.addTube(RD_1x65, RD_5x35, "mid-lower-left-sideimpact", "mid-upper-left-sideimpact", True, True)
    frame.addTube(RD_1x65, RD_5x35, "mid-upper-left-sideimpact", "left-sideimpact-mainhoop", True, True, "UpperSideImpact")
    frame.addTube(RD_5x49, RD_5x35, "mid-upper-left-sideimpact", "left-harnessbar-mainhoop", True, True)

    # main roll hoop
    frame.addTube(RD_1x95, RD_1x95, "left-lower-mainhoop", "left-sideimpact-mainhoop", True, True, "MainRollHoop")
    frame.addTube(RD_1x95, RD_1x95, "left-sideimpact-mainhoop", "left-harnessbar-mainhoop", True, True, "MainRollHoop")
    frame.addTube(RD_1x95, RD_1x95, "left-harnessbar-mainhoop", "left-brace-mainhoop", True, True, "MainRollHoop")
    frame.addTube(RD_1x95, RD_1x95, "left-brace-mainhoop", "left-upmost-mainhoop", True, True, "MainRollHoop")
    frame.addTube(RD_1x95, RD_1x95, "left-upmost-mainhoop", "left-upmost-mainhoop#m", False, True, "MainRollHoop")

    frame.addTube(RD_1x95, RD_1x95, "left-harnessbar-mainhoop", "left-harnessbar-mainhoop#m", False, True)
    frame.addTube(RD_1x35, RD_5x35, "left-sideimpact-mainhoop", "foremost-enginemount-left", False, True)
    frame.addTube(RD_1x35, RD_5x35, "left-sideimpact-mainhoop#m", "foremost-enginemount-right", False, True)

    # crossbraces
    frame.addTube(RD_1x35, RD_5x35, "left-lower-mainhoop", "seat-crossbrace1", False, True, "Crossbrace5")
    frame.addTube(RD_1x35, RD_5x35, "left-lower-mainhoop#m", "seat-crossbrace1", False, True, "Crossbrace5")
    frame.addTube(RD_1x35, RD_5x35, "mid-lower-left-sideimpact", "seat-crossbrace1", False, True, "Crossbrace4")
    frame.addTube(RD_1x35, RD_5x35, "mid-lower-left-sideimpact#m", "seat-crossbrace1", False, True, "Crossbrace4")
    frame.addTube(RD_1x65, RD_5x35, "mid-lower-left-sideimpact", "seat-crossbrace2", False, True, "Crossbrace4")
    frame.addTube(RD_1x65, RD_5x35, "mid-lower-left-sideimpact#m", "seat-crossbrace2", False, True, "Crossbrace4")
    frame.addTube(RD_1x65, RD_5x35, "seat-crossbrace2", "lower-aft-left-frontbox", False, True)
    frame.addTube(RD_1x65, RD_5x35, "seat-crossbrace2", "lower-aft-left-frontbox#m", False, True)

    # use these to test the isRequired property
    frame.addTube(RD_1x35, RD_5x35, "lower-aft-left-frontbox", "frontbox-crossbrace", False, False, "Crossbrace3")
    frame.addTube(RD_1x35, RD_5x35, "lower-aft-left-frontbox#m", "frontbox-crossbrace", False, False, "Crossbrace3")
    frame.addTube(RD_5x49, RD_5x35, "left-frontdamper", "frontbox-crossbrace", False, False, "Crossbrace2")
    frame.addTube(RD_5x49, RD_5x35, "left-frontdamper#m", "frontbox-crossbrace", False, False, "Crossbrace2")
    frame.addTube(RD_1x35, RD_5x35, "lower-fore-left-frontbox", "frontbox-crossbrace", False, False, "Crossbrace1")
    frame.addTube(RD_1x35, RD_5x35, "lower-fore-left-frontbox#m", "frontbox-crossbrace", False, False, "Crossbrace1")

    frame.addTube(RD_1x35, RD_5x35, "left-harnessbar-mainhoop", "foremost-enginemount-left", False, True)
    frame.addTube(RD_1x35, RD_5x35, "foremost-enginemount-right", "left-harnessbar-mainhoop#m", False, True)

    frame.addTube(RD_1x65, RD_5x35, "left-brace-mainhoop", "upper-fore-rearbox", True, True)
    frame.addTube(RD_1x35, RD_5x35, "left-lower-mainhoop", "lower-fore-rearbox", True, True)
    frame.addTube(RD_1x49, RD_5x35, "left-lower-mainhoop", "upper-fore-rearbox", True, True)
    frame.addTube(RD_1x49, RD_5x35, "left-sideimpact-mainhoop", "upper-fore-rearbox", True, True)

    frame.addTube(RD_5x49, RD_5x35, "upper-fore-rearbox", "lower-fore-rearbox", True, True)
    frame.addTube(RD_5x49, RD_5x35, "upper-fore-rearbox", "lower-aft-rearbox", True, True)
    frame.addTube(RD_5x49, RD_5x35, "upper-aft-rearbox", "lower-aft-rearbox", True, True)
    frame.addTube(RD_1x35, RD_5x35, "upper-fore-rearbox", "upper-aft-rearbox", True, True)
    frame.addTube(RD_1x35, RD_5x35, "lower-fore-rearbox", "lower-aft-rearbox", True, True)

    frame.addTube(RD_1x35, RD_5x35, "lower-fore-rearbox", "lower-aft-left-enginemount", True, True)
    frame.addTube(RD_1x35, RD_5x35, "lower-aft-rearbox", "lower-aft-rearbox#m", False, True)

    frame.addTube(RD_1x35, RD_5x35, "upper-aft-rearbox", "trampoline-left", True, True)
    frame.addTube(RD_1x35, RD_5x35, "trampoline-left", "upper-aft-left-enginemount", True, True)
    frame.addTube(RD_1x35, RD_5x35, "trampoline-left", "rear-damper-left", True, True)
    frame.addTube(RD_1x35, RD_5x35, "rear-damper-left", "rear-damper-left#m", False, True)

    frame.addTube(RD_5x49, RD_5x35, "lower-fore-rearbox", "rearbox-crossbrace", False, True)
    frame.addTube(RD_5x49, RD_5x35, "rearbox-crossbrace", "lower-aft-rearbox", False, True)
    frame.addTube(RD_5x49, RD_5x35, "rearbox-crossbrace", "lower-aft-rearbox#m", False, True)
    frame.addTube(RD_5x49, RD_5x35, "rearbox-crossbrace", "lower-aft-left-enginemount#m", False, True)

    # Engine tubes

    engineTubeThickness = RD_1xSLD

    frame.addTube(engineTubeThickness, RD_1xSLD, "upper-aft-left-enginemount", "lower-aft-left-enginemount", True, True)
    frame.addTube(engineTubeThickness, RD_1xSLD,"upper-aft-left-enginemount","lower-aft-left-enginemount#m",False,True)
    frame.addTube(engineTubeThickness, RD_1xSLD, "upper-aft-left-enginemount", "foremost-enginemount-left", False, True)
    frame.addTube(engineTubeThickness, RD_1xSLD, "upper-aft-left-enginemount", "foremost-enginemount-right", False, True)
    frame.addTube(engineTubeThickness, RD_1xSLD, "upper-aft-left-enginemount", "upper-aft-left-enginemount#m", False, True)

    frame.addTube(engineTubeThickness, RD_1xSLD, "upper-aft-left-enginemount#m", "lower-aft-left-enginemount", False, True)
    frame.addTube(engineTubeThickness, RD_1xSLD, "upper-aft-left-enginemount#m", "foremost-enginemount-left", False, True)
    frame.addTube(engineTubeThickness, RD_1xSLD, "upper-aft-left-enginemount#m", "foremost-enginemount-right", False, True)

    frame.addTube(engineTubeThickness, RD_1xSLD, "foremost-enginemount-left", "foremost-enginemount-right", False, True)
    frame.addTube(engineTubeThickness, RD_1xSLD, "foremost-enginemount-left", "lower-aft-left-enginemount", False, True)
    frame.addTube(engineTubeThickness, RD_1xSLD, "foremost-enginemount-left", "lower-aft-left-enginemount#m", False, True)

    frame.addTube(engineTubeThickness, RD_1xSLD, "foremost-enginemount-right", "lower-aft-left-enginemount", False, True)
    frame.addTube(engineTubeThickness, RD_1xSLD, "foremost-enginemount-right", "lower-aft-left-enginemount#m", False, True)

    frame.addTube(engineTubeThickness, RD_1xSLD, "lower-aft-left-enginemount", "lower-aft-left-enginemount#m", False, True)

    return frame