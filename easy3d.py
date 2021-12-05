# easy3d.py
from xo import *
from universe import * #InteractiveWorld, runGL
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph as pg
import pyqtgraph.exporters
import pyqtgraph.opengl as gl
import time, math, random
import numpy as np
# from akeyo import Entity


enteties = {}

def runEngine(data=None, *args,**kwargs):
    app = QtGui.QApplication([])
    world = InteractiveWorld(app)
    xo.world = [world]
    world.setup()

    simulate0 = True
    if simulate0:
        xo.apexes = [[0,0,0],[100,100,100]]
        world.load("apexes")

    world.runGL()

# xo.asyn(runEngine)
def afterStart(data = None):
    print("wait for it")
    time.sleep(3)
    add = []
    for i in range(3):
        i+=1
        for j in range(3):
            j+=1
            add.append( [i*1000,j*1000,0])
            add.append( [-i*1000,j*1000,0])
            add.append( [i*1000,-j*1000,0])
            add.append( [-i*1000,-j*1000,0])

    # xo.newApex = [0,0,0]
    print("addddddddddddd",add)
    print("addddddddddddd",add)
    print("addddddddddddd",add)
    print("addddddddddddd",add)
    print("addddddddddddd",add)
    print("addddddddddddd",add)
    print("addddddddddddd",add)
    print("addddddddddddd",add)
    xo.newApex = add[1:]

xo.asyn(afterStart)

runEngine()
time.sleep(1)
world = xo.world.value()[0]
print("!!!!!!!!!!!!!!!!!!!!")
print(world)
print("!!!!!!!!!!!!!!!!!!!!")
