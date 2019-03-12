
# NOTE: All units given in pounds and inches
# Use http://www.perbang.dk/rgbgradient/ for color selection

# Material properties
E = 2.97e7
G = 1.16e7
density = 0.284

halfLineWidth = 1
threeQuartLinewidth = 2
oneLinewidth = 3
solidLinewidth = 4

# A is the cross-sectional area
# I is the second moment of inertia across the cross-section
# J is the polar moment of inertia about the cross-section
class RD_5x35:
    name = "0.5 x 0.035"
    string = "RD_5x35"
    E = E
    G = G
    A = 0.051129
    I = 0.0013898
    J = 0.0027795
    linewidth = halfLineWidth
    color = '#ffe12e'
    round = True

class RD_5x49:
    name = "0.5 x 0.049"
    string = "RD_5x49"
    E = E
    G = G
    A = 0.0694261
    I = 0.0017860
    J = 0.0035720
    linewidth = halfLineWidth
    color = '#d9c03a'
    round = True

class RD_75x35:
    name = "0.75 x 0.035"
    string = "RD_75x35"
    E = E
    G = G
    A = 0.078618
    I = 0.0050360
    J = 0.0100720
    linewidth = threeQuartLinewidth
    color = '#fdff2e'
    round = True

class RD_75x49:
    name = "0.75 x 0.049"
    string = "RD_75x49"
    E = E
    G = G
    A = 0.1079106
    I = 0.0066608
    J = 0.0133216
    linewidth = threeQuartLinewidth
    color = '#dcdb5b'
    round = True

class RD_1x35:
    name = "1 x 0.035"
    string = "RD_1x35"
    E = E
    G = G
    A = 0.106107
    I = 0.0123675
    J = 0.0247349
    linewidth = oneLinewidth
    color = '#77ff2e'
    round = True

class RD_1x49:
    name = "1 x 0.049"
    string = "RD_1x49"
    E = E
    G = G
    A = 0.146395
    I = 0.0165939
    J = 0.0331878
    linewidth = oneLinewidth
    color = '#23f23e'
    round = True

class RD_1x65:
    name = "1 x 0.065"
    string = "RD_1x65"
    E = E
    G = G
    A = 0.19093
    I = 0.0209653
    J = 0.0419307
    linewidth = oneLinewidth
    color = '#18e697'
    round = True

class RD_1x83:
    name = "1 x 0.083"
    string = "RD_1x83"
    E = E
    G = G
    A = 0.239110
    I = 0.0253390
    J = 0.0506780
    linewidth = oneLinewidth
    color = '#0fc7da'
    round = True

class RD_1x95:
    name = "1 x 0.095"
    string = "RD_1x95"
    E = E
    G = G
    A = 0.270098
    I = 0.0279569
    J = 0.0559138
    linewidth = oneLinewidth
    color = "#075bce"
    round = True

class RD_1x120:
    name = "1 x 0.120"
    string = "RD_1x120"
    E = E
    G = G
    A = 0.331752
    I = 0.0327108
    J = 0.0654215
    linewidth = oneLinewidth
    color = '#0b00c2'
    round = True

class RD_1xSLD:
    name = "1 x Solid"
    string = "RD_1xSLD"
    E = E
    G = G
    A = 0.785398
    I = 0.0490874
    J = 0.0981748
    linewidth = solidLinewidth
    color = '#000000'
    round = True

class SQ_1x35:
    name = "1 x 1 x 0.035"
    string = "SQ_1x35"
    E = E
    G = G
    A = 0.1321857
    I = 0.0202877
    J = 0.0405755
    linewidth = oneLinewidth
    color = '#ff2ee7'
    round = False

class SQ_1x49:
    name = "1 x 1 x 0.049"
    string = "SQ_1x49"
    E = E
    G = G
    A = 0.1806335
    I = 0.0267870
    J = 0.0535739
    linewidth = oneLinewidth
    color = '#cc44c3'
    round = False


class SQ_1x65:
    name = "1 x 1 x 0.065"
    string = "SQ_1x65"
    E = E
    G = G
    A = 0.2330008
    I = 0.0331999
    J = 0.0663999
    linewidth = oneLinewidth
    color = '#9a5b9f'
    round = False


# When adding a tube, don't forget to also add its name to this list (used for random selection)
# MUST BE IN ORDER OF INCREASING OD, THEN WALL THICKNESS (AND NO SQUARE TUBES -- THOSE MUST BE SET MANUALLY)
allRoundSizes = [RD_5x35, RD_5x49, RD_75x35, RD_75x49, RD_1x35, RD_1x49, RD_1x65, RD_1x83,
            RD_1x95, RD_1x120]
