
# NOTE: All units given in pounds and inches

# Material properties
E = 2.97e7
G = 1.16e7
density = 0.284

# A is the cross-sectional area
# I is the second moment of inertia across the cross-section
# J is the polar moment of inertia about the cross-section
class RD_5x35:
    name = "0.5 x 0.035"
    A = 0.051129
    I = 0.0013898
    J = 0.0027795
    round = True

class RD_5x49:
    name = "0.5 x 0.049"
    A = 0.0694261
    I = 0.0017860
    J = 0.0035720
    round = True

class RD_75x35:
    name = "0.75 x 0.035"
    A = 0.078618
    I = 0.0050360
    J = 0.0100720
    round = True

class RD_75x49:
    name = "0.75 x 0.049"
    A = 0.1079106
    I = 0.0066608
    J = 0.0133216
    round = True

class RD_1x35:
    name = "1 x 0.035"
    A = 0.106107
    I = 0.0123675
    J = 0.0247349
    round = True

class RD_1x49:
    name = "1 x 0.049"
    A = 0.146395
    I = 0.0165939
    J = 0.0331878
    round = True

class RD_1x65:
    name = "1 x 0.065"
    A = 0.19093
    I = 0.0209653
    J = 0.0419307
    round = True

class RD_1x83:
    name = "1 x 0.083"
    A = 0.239110
    I = 0.0253390
    J = 0.0506780
    round = True

class RD_1x95:
    name = "1 x 0.095"
    A = 0.270098
    I = 0.0279569
    J = 0.0559138
    round = True

class RD_1x120:
    name = "1 x 0.120"
    A = 0.331752
    I = 0.0327108
    J = 0.0654215
    round = True

class RD_1xSLD:
    name = "1 x Solid"
    A = 0.785398
    I = 0.0490874
    J = 0.0981748
    round = True

class SQ_1x35:
    name = "1 x 1 x 0.035"
    A = 0.1321857
    I = 0.0202877
    J = 0.0405755
    round = False

class SQ_1x49:
    name = "1 x 1 x 0.049"
    A = 0.1806335
    I = 0.0267870
    J = 0.0535739
    round = False


class SQ_1x65:
    name = "1 x 1 x 0.065"
    A = 0.2330008
    I = 0.0331999
    J = 0.0663999
    round = False


# When adding a tube, don't forget to also add its name to this list (used for random selection)
# MUST BE IN ORDER OF INCREASING OD, THEN WALL THICKNESS (AND NO SQUARE TUBES -- THOSE MUST BE SET MANUALLY)
allRoundSizes = [RD_5x35, RD_5x49, RD_75x35, RD_75x49, RD_1x35, RD_1x49, RD_1x65, RD_1x83,
            RD_1x95, RD_1x120, RD_1xSLD]
