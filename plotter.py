from tube import *
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from tubeSizes import *
from mpld3 import *

def plotFrameAni(frame, axes, title):
    axes.clear()
    axes.set_aspect('equal')
    axes.set_title(title)
    setEqualScaling(frame, axes)

    for tube in frame.tubes:
        plot(tube, axes)

def plotFrame(frame, displacedScaling, figPath=None):
    fig = plt.figure(figsize=(12,9))
    fig.suptitle(frame.loadCase.name)
    axes = fig.gca(projection='3d')
    axes.set_aspect('equal')
    axes.view_init(azim=-135, elev=35)
    setEqualScaling(frame, axes)

    for tube in frame.tubes:
        plot(tube, axes)
    if frame.displacements is not None:
        for tube in frame.tubes:
            plotDisplacedTube(frame, tube, axes, displacedScaling)
    if figPath is not None:
        fig.savefig(figPath)
        plt.close(fig)
    else:
        plt.show()


def plot(tube, axes):
    xStart = tube.nodeFrom.x
    yStart = tube.nodeFrom.y
    zStart = tube.nodeFrom.z
    xEnd = tube.nodeTo.x
    yEnd = tube.nodeTo.y
    zEnd = tube.nodeTo.z
    axes.plot([xStart, xEnd], [yStart, yEnd], [zStart, zEnd], tube.size.color, linewidth = tube.size.linewidth)

def plotDisplacedTube(frame, tube, axes, displacedScaling):
    fromIndex = frame.nodes.index(tube.nodeFrom)
    toIndex = frame.nodes.index(tube.nodeTo)
    xStart = tube.nodeFrom.x + displacedScaling*frame.displacements[0, fromIndex]
    yStart = tube.nodeFrom.y + displacedScaling*frame.displacements[1, fromIndex]
    zStart = tube.nodeFrom.z + displacedScaling*frame.displacements[2, fromIndex]
    xEnd = tube.nodeTo.x + displacedScaling*frame.displacements[0, toIndex]
    yEnd = tube.nodeTo.y + displacedScaling*frame.displacements[1, toIndex]
    zEnd = tube.nodeTo.z + displacedScaling*frame.displacements[2, toIndex]
    axes.plot([xStart, xEnd], [yStart, yEnd], [zStart, zEnd], '#f44277', linestyle='dotted', linewidth=1)

def setEqualScaling(frame, axes):
    X = []
    Y = []
    Z = []
    for node in frame.nodes:
        X.append(node.x)
        Y.append(node.y)
        Z.append(node.z)
    X = np.array(X)
    Y = np.array(Y)
    Z = np.array(Z)
    # Taken from Stack Overflow -- creates "cubic bounding box" to get equal axis lengths
    max_range = np.array([X.max() - X.min(), Y.max() - Y.min(), Z.max() - Z.min()]).max() / 2.0
    mid_x = (X.max() + X.min()) * 0.5
    mid_y = (Y.max() + Y.min()) * 0.5
    mid_z = (Z.max() + Z.min()) * 0.5
    axes.set_xlim(mid_x - max_range, mid_x + max_range)
    axes.set_ylim(mid_y - max_range, mid_y + max_range)
    axes.set_zlim(mid_z - max_range, mid_z + max_range)
    # -------------------------------------------------------------------------------------
