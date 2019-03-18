from tubeSizes import *
from frame import *
from createBaseFrame import *

def createFrame():

    baseFrame = createBaseFrame()
    frame = Frame()


    # Copy and paste the simulation-generated frame .txt file here:
    # -------------------------------------------------------------
    frame.addNode('upper-left-bulkhead', 17.852000, -6.929000, 17.195000, True, True)
    frame.addNode('lower-left-bulkhead', 17.852000, -6.929000, 4.820000, True, True)
    frame.addNode('upper-fore-left-frontbox', 33.203000, -8.690000, 8.932000, True, True)
    frame.addNode('lower-fore-left-frontbox', 33.652000, -6.929000, 4.820000, True, True)
    frame.addNode('upper-aft-left-frontbox', 44.194000, -8.584000, 8.907000, True, True)
    frame.addNode('lower-aft-left-frontbox', 43.970000, -6.929000, 4.820000, True, True)
    frame.addNode('left-frontdamper', 40.200000, -9.000000, 17.250000, True, True)
    frame.addNode('fore-upper-left-sideimpact', 45.327688, -9.829629, 12.500000, True, True, 4.000000, 0.000000,
                  1.000000, 2.000000, 0.000000, 0.000000)
    frame.addNode('upper-left-fronthoop', 45.356789, -5.598524, 22.613878, True, True, 3.000000, 2.000000, 1.000000,
                  3.000000, 1.000000, 1.000000)
    frame.addNode('mid-upper-left-sideimpact', 63.296942, -10.521527, 12.737000, True, False, 5.000000, 5.000000,
                  2.000000, 6.000000, 0.000000, 0.000000)
    frame.addNode('left-lower-mainhoop', 73.150000, -11.268104, 2.000000, True, True, 0.000000, 0.000000, 2.000000,
                  3.000000, 0.000000, 0.000000, 'MainHoop')
    frame.addNode('left-sideimpact-mainhoop', 73.150000, -12.212001, 12.993000, True, True, 0.000000, 0.000000,
                  1.000000, 4.000000, 0.000000, 0.000000, 'MainHoop')
    frame.addNode('left-harnessbar-mainhoop', 73.150000, -10.550000, 23.100000, True, True)
    frame.addNode('left-brace-mainhoop', 73.150000, -6.347881, 36.547623, True, True, 0.000000, 0.000000, 0.000000,
                  2.000000, 0.000000, 2.000000, 'MainHoop')
    frame.addNode('nipple-mainhoop', 73.150000, 0.000000, 43.245750, False, True, 0.000000, 0.000000, 0.000000,
                  0.000000, 3.000000, 1.000000, 'MainHoop')
    frame.addNode('seat-crossbrace', 59.318430, 0.000000, 2.220164, False, True, 1.000000, 1.000000, 0.000000, 0.000000,
                  1.000000, 1.000000)
    frame.addNode('frontbox-crossbrace', 40.806898, 0.000000, 4.092631, False, True, 2.000000, 1.000000, 0.000000,
                  0.000000, 0.000000, 1.000000)
    frame.addNode('left-rockernode', 40.200000, -6.929000, 4.820000, True, True)
    frame.addNode('engine-to-harness', 75.698000, -9.598000, 23.100000, True, True)
    frame.addNode('foremost-enginemount', 79.706000, -7.667500, 14.875000, False, True)
    frame.addNode('end-of-bend-harness', 76.650000, -7.300000, 23.100000, True, True)
    frame.addNode('upper-fore-rearbox', 93.554400, -8.600000, 10.944000, True, True)
    frame.addNode('lower-fore-rearbox', 92.265000, -7.500000, 5.907000, True, True)
    frame.addNode('lower-mid-rearbox', 97.543000, -6.238000, 4.911900, True, True)
    frame.addNode('lower-aft-rearbox', 103.246000, -6.237800, 5.904000, True, True)
    frame.addNode('upper-aft-rearbox', 105.572000, -9.056000, 10.968800, True, True)
    frame.addNode('upper-mid-rearbox', 99.500000, -8.825800, 10.956300, True, True)
    frame.addNode('upper-rearRockerPlane', 98.019233, -6.929259, 12.806176, True, True, 1.000000, 1.000000, 1.000000,
                  1.000000, 2.000000, 1.000000, 'RockerPlane')
    frame.addNode('pyramid', 98.626256, 0.000000, 18.641427, False, True, 1.000000, 1.000000, 0.000000, 0.000000,
                  3.000000, 0.000000, 'RockerPlane')
    frame.addNode('upper-aft-enginemount', 93.523300, -4.262500, 16.400000, True, True)
    frame.addNode('lower-aft-enginemount', 93.541300, -3.656500, 7.177000, True, True)
    frame.addNode('foremost-enginemount-mirror', 79.030000, 7.648000, 14.380000, False, True)
    frame.addTube(SQ_1x49, SQ_1x49, 'upper-left-bulkhead', 'lower-left-bulkhead', True, True)
    frame.addTube(SQ_1x49, SQ_1x49, 'upper-left-bulkhead', 'upper-left-bulkhead#m', False, True)
    frame.addTube(SQ_1x49, SQ_1x49, 'lower-left-bulkhead', 'lower-left-bulkhead#m', False, True)
    frame.addTube(RD_1x65, RD_1x65, 'upper-left-bulkhead', 'upper-left-fronthoop', True, True)
    frame.addTube(RD_1x49, RD_1x49, 'upper-left-bulkhead', 'upper-fore-left-frontbox', True, True)
    frame.addTube(RD_1x49, RD_1x49, 'lower-left-bulkhead', 'upper-fore-left-frontbox', True, True)
    frame.addTube(RD_5x35, RD_5x35, 'lower-left-bulkhead', 'lower-fore-left-frontbox', True, True, 'LowerFrontAArm')
    frame.addTube(RD_5x35, RD_5x35, 'lower-fore-left-frontbox', 'left-rockernode', True, True, 'LowerFrontAArm')
    frame.addTube(RD_5x35, RD_5x35, 'left-rockernode', 'lower-aft-left-frontbox', True, True, 'LowerFrontAArm')
    frame.addTube(RD_5x35, RD_5x35, 'lower-fore-left-frontbox', 'upper-fore-left-frontbox', True, True)
    frame.addTube(RD_5x35, RD_5x35, 'lower-fore-left-frontbox', 'upper-aft-left-frontbox', True, True)
    frame.addTube(RD_5x35, RD_5x35, 'upper-fore-left-frontbox', 'upper-aft-left-frontbox', True, True)
    frame.addTube(RD_1x35, RD_5x35, 'upper-fore-left-frontbox', 'fore-upper-left-sideimpact', True, True)
    frame.addTube(RD_75x35, RD_5x35, 'upper-fore-left-frontbox', 'left-frontdamper', True, True)
    frame.addTube(RD_5x35, RD_5x35, 'left-frontdamper', 'upper-left-fronthoop', True, True)
    frame.addTube(RD_5x35, RD_5x35, 'left-frontdamper', 'fore-upper-left-sideimpact', True, True)
    frame.addTube(RD_1x95, RD_1x95, 'lower-aft-left-frontbox', 'upper-aft-left-frontbox', True, True, 'FrontRollHoop')
    frame.addTube(RD_1x95, RD_1x95, 'upper-aft-left-frontbox', 'fore-upper-left-sideimpact', True, True,
                  'FrontRollHoop')
    frame.addTube(RD_1x95, RD_1x95, 'fore-upper-left-sideimpact', 'upper-left-fronthoop', True, True, 'FrontRollHoop')
    frame.addTube(RD_1x95, RD_1x95, 'upper-left-fronthoop', 'upper-left-fronthoop#m', False, True, 'FrontRollHoop')
    frame.addTube(RD_1x35, RD_5x35, 'upper-left-fronthoop', 'mid-upper-left-sideimpact', True, True)
    frame.addTube(RD_1x83, RD_5x35, 'fore-upper-left-sideimpact', 'mid-upper-left-sideimpact', True, True,
                  'UpperSideImpact')
    frame.addTube(RD_5x35, RD_5x35, 'upper-aft-left-frontbox', 'mid-upper-left-sideimpact', True, True)
    frame.addTube(RD_5x35, RD_5x35, 'lower-aft-left-frontbox', 'mid-upper-left-sideimpact', True, True)
    frame.addTube(RD_1x35, RD_5x35, 'lower-aft-left-frontbox', 'left-lower-mainhoop', True, True)
    frame.addTube(RD_1x83, RD_5x35, 'mid-upper-left-sideimpact', 'left-sideimpact-mainhoop', True, True,
                  'UpperSideImpact')
    frame.addTube(RD_1x95, RD_1x95, 'left-lower-mainhoop', 'left-sideimpact-mainhoop', True, True, 'MainRollHoop')
    frame.addTube(RD_1x95, RD_1x95, 'left-sideimpact-mainhoop', 'left-harnessbar-mainhoop', True, True, 'MainRollHoop')
    frame.addTube(RD_1x95, RD_1x95, 'left-harnessbar-mainhoop', 'left-brace-mainhoop', True, True, 'MainRollHoop')
    frame.addTube(RD_1x95, RD_1x95, 'left-brace-mainhoop', 'nipple-mainhoop', False, True, 'MainRollHoop')
    frame.addTube(RD_1x95, RD_1x95, 'nipple-mainhoop', 'left-brace-mainhoop#m', False, True, 'MainRollHoop')
    frame.addTube(RD_1x35, RD_5x35, 'left-lower-mainhoop', 'seat-crossbrace', False, True, 'Crossbrace5')
    frame.addTube(RD_1x35, RD_5x35, 'left-lower-mainhoop#m', 'seat-crossbrace', False, True, 'Crossbrace5')
    frame.addTube(RD_1x35, RD_5x35, 'lower-aft-left-frontbox', 'seat-crossbrace', False, True, 'Crossbrace4')
    frame.addTube(RD_1x35, RD_5x35, 'lower-aft-left-frontbox#m', 'seat-crossbrace', False, True, 'Crossbrace4')
    frame.addTube(RD_1x35, RD_5x35, 'lower-aft-left-frontbox', 'frontbox-crossbrace', False, False, 'Crossbrace3')
    frame.addTube(RD_1x35, RD_5x35, 'lower-aft-left-frontbox#m', 'frontbox-crossbrace', False, False, 'Crossbrace3')
    frame.addTube(RD_5x35, RD_5x35, 'left-rockernode', 'frontbox-crossbrace', False, False, 'Crossbrace2')
    frame.addTube(RD_5x35, RD_5x35, 'left-rockernode#m', 'frontbox-crossbrace', False, False, 'Crossbrace2')
    frame.addTube(RD_5x35, RD_5x35, 'lower-fore-left-frontbox', 'frontbox-crossbrace', False, False, 'Crossbrace1')
    frame.addTube(RD_5x35, RD_5x35, 'lower-fore-left-frontbox#m', 'frontbox-crossbrace', False, False, 'Crossbrace1')
    frame.addTube(RD_5x35, RD_5x35, 'left-sideimpact-mainhoop', 'engine-to-harness', True, True)
    frame.addTube(RD_1x35, RD_5x35, 'engine-to-harness', 'foremost-enginemount', False, True)
    frame.addTube(RD_1x35, RD_5x35, 'foremost-enginemount-mirror', 'engine-to-harness#m', False, True)
    frame.addTube(RD_1x120, RD_5x35, 'left-sideimpact-mainhoop', 'foremost-enginemount', False, True)
    frame.addTube(RD_1x120, RD_5x35, 'left-sideimpact-mainhoop#m', 'foremost-enginemount-mirror', False, True)
    frame.addTube(RD_5x35, RD_5x35, 'left-brace-mainhoop', 'upper-fore-rearbox', True, True)
    frame.addTube(RD_1x65, RD_5x35, 'left-lower-mainhoop', 'lower-fore-rearbox', True, True)
    frame.addTube(RD_5x35, RD_5x35, 'left-lower-mainhoop', 'upper-fore-rearbox', True, True)
    frame.addTube(RD_5x35, RD_5x35, 'left-sideimpact-mainhoop', 'upper-fore-rearbox', True, True)
    frame.addTube(RD_1x95, RD_1x95, 'left-harnessbar-mainhoop', 'engine-to-harness', True, True, 'HarnessBar')
    frame.addTube(RD_1x95, RD_1x95, 'engine-to-harness', 'end-of-bend-harness', True, True, 'HarnessBar')
    frame.addTube(RD_1x95, RD_1x95, 'end-of-bend-harness', 'end-of-bend-harness#m', False, True, 'HarnessBar')
    frame.addTube(RD_5x35, RD_5x35, 'upper-fore-rearbox', 'lower-fore-rearbox', True, True)
    frame.addTube(RD_5x35, RD_5x35, 'upper-fore-rearbox', 'lower-mid-rearbox', True, True)
    frame.addTube(RD_5x35, RD_5x35, 'lower-mid-rearbox', 'upper-aft-rearbox', True, True)
    frame.addTube(RD_5x35, RD_5x35, 'upper-aft-rearbox', 'lower-aft-rearbox', True, True)
    frame.addTube(RD_1x35, RD_5x35, 'lower-fore-rearbox', 'lower-aft-enginemount', True, True)
    frame.addTube(RD_1x49, RD_5x35, 'lower-aft-enginemount', 'lower-mid-rearbox', True, True)
    frame.addTube(RD_5x35, RD_5x35, 'lower-aft-rearbox', 'lower-aft-rearbox#m', False, True)
    frame.addTube(RD_5x35, RD_5x35, 'upper-aft-rearbox', 'upper-aft-rearbox#m', False, True)
    frame.addTube(RD_5x35, RD_5x35, 'upper-fore-rearbox', 'upper-mid-rearbox', True, True, 'UpperRearbox')
    frame.addTube(RD_5x35, RD_5x35, 'upper-mid-rearbox', 'upper-aft-rearbox', True, True, 'upperRearbox')
    frame.addTube(RD_5x35, RD_5x35, 'upper-fore-rearbox', 'upper-aft-enginemount', True, True)
    frame.addTube(RD_5x35, RD_5x35, 'upper-fore-rearbox', 'upper-rearRockerPlane', True, True)
    frame.addTube(RD_5x35, RD_5x35, 'upper-rearRockerPlane', 'upper-aft-enginemount', True, True, 'toEngineMount')
    frame.addTube(RD_5x35, RD_5x35, 'upper-rearRockerPlane', 'upper-aft-rearbox', True, True, 'toEngineMount')
    frame.addTube(RD_5x49, RD_5x35, 'upper-mid-rearbox', 'upper-rearRockerPlane', True, False)
    frame.addTube(RD_5x35, RD_5x35, 'upper-rearRockerPlane', 'pyramid', False, False)
    frame.addTube(RD_5x35, RD_5x35, 'upper-rearRockerPlane#m', 'pyramid', False, False)
    frame.addTube(RD_5x35, RD_5x35, 'upper-aft-rearbox', 'pyramid', False, False)
    frame.addTube(RD_5x35, RD_5x35, 'upper-aft-rearbox#m', 'pyramid', False, False)
    frame.addTube(RD_1x65, RD_5x35, 'upper-aft-enginemount', 'pyramid', False, False)
    frame.addTube(RD_1x49, RD_5x35, 'upper-aft-enginemount#m', 'pyramid', False, False)
    frame.addTube(RD_1x49, RD_5x35, 'lower-fore-rearbox', 'lower-mid-rearbox', True, True)
    frame.addTube(RD_1x65, RD_5x35, 'lower-mid-rearbox', 'lower-aft-rearbox', True, True)
    frame.addTube(RD_1xSLD, RD_1xSLD, 'upper-aft-enginemount', 'lower-aft-enginemount', True, True)
    frame.addTube(RD_1xSLD, RD_1xSLD, 'upper-aft-enginemount', 'lower-aft-enginemount#m', False, True)
    frame.addTube(RD_1xSLD, RD_1xSLD, 'upper-aft-enginemount', 'foremost-enginemount', False, True)
    frame.addTube(RD_1xSLD, RD_1xSLD, 'upper-aft-enginemount', 'foremost-enginemount-mirror', False, True)
    frame.addTube(RD_1xSLD, RD_1xSLD, 'upper-aft-enginemount', 'upper-aft-enginemount#m', False, True)
    frame.addTube(RD_1xSLD, RD_1xSLD, 'upper-aft-enginemount#m', 'lower-aft-enginemount', False, True)
    frame.addTube(RD_1xSLD, RD_1xSLD, 'upper-aft-enginemount#m', 'foremost-enginemount', False, True)
    frame.addTube(RD_1xSLD, RD_1xSLD, 'upper-aft-enginemount#m', 'foremost-enginemount-mirror', False, True)
    frame.addTube(RD_1xSLD, RD_1xSLD, 'foremost-enginemount', 'foremost-enginemount-mirror', False, True)
    frame.addTube(RD_1xSLD, RD_1xSLD, 'foremost-enginemount', 'lower-aft-enginemount', False, True)
    frame.addTube(RD_1xSLD, RD_1xSLD, 'foremost-enginemount', 'lower-aft-enginemount#m', False, True)
    frame.addTube(RD_1xSLD, RD_1xSLD, 'foremost-enginemount-mirror', 'lower-aft-enginemount', False, True)
    frame.addTube(RD_1xSLD, RD_1xSLD, 'foremost-enginemount-mirror', 'lower-aft-enginemount#m', False, True)
    frame.addTube(RD_1xSLD, RD_1xSLD, 'lower-aft-enginemount', 'lower-aft-enginemount#m', False, True)

    # -------------------------------------------------------------

    for node in frame.nodes:
        for baseNode in baseFrame.nodes:
            if node.name is baseNode.name:
                node.xOrig = baseNode.xOrig
                node.yOrig = baseNode.yOrig
                node.zOrig = baseNode.zOrig

    return frame