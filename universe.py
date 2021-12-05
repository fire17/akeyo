# universe.py
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph as pg
import pyqtgraph.exporters
import pyqtgraph.opengl as gl
import time, math, random
import numpy as np
numpy = np
from xo import *
from AkeyOverse import * #Entity
rotateSpeed = [0.8]
# epsilon=1e-6
#
# import sys
# from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsEllipseItem
# from PyQt5.QtCore import Qt, QPointF
# class PlotObject(gl.GLViewWidget):


def intersect(planeNormal = [0, 0, 1], planePoint = [0, 0, 0],rayDirection = [0, 1, 1],rayPoint = [0, 0, -1],epsilon=1e-6):
	planeNormal, planePoint, rayDirection, rayPoint = np.array(planeNormal), np.array(planePoint), np.array(rayDirection), np.array(rayPoint)
	#Any point along the ray
	ndotu = planeNormal.dot(rayDirection)
	if abs(ndotu) < epsilon:
		print ("no intersection or line is within plane")

	w = rayPoint - planePoint
	si = -planeNormal.dot(w) / ndotu
	Psi = w + si * rayDirection + planePoint

	print ("intersection at", Psi)
	return Psi

def GetApexMesh(gl, xyz, scale=10/1.2, color = (.31,.05,.3,1),drawFaces=False,rows=5, cols=12):
	# md = gl.MeshData.sphere(rows=5, cols=5)
	md = gl.MeshData.sphere(rows, cols)
	x, y, z = xyz
	# apexMesh = gl.GLMeshItem(meshdata=md, smooth=False, drawFaces=drawFaces, drawEdges=True, edgeColor=color)
	apexMesh = gl.GLMeshItem(meshdata=md, smooth=False, drawFaces=True, drawEdges=True, color=color)
	color = 0,0,0,1

	# apexMesh.setColor(color)
	apexMesh.setGLOptions('additive')
	apexMesh.translate(x,y,z)
	apexMesh.scale(scale,scale,scale)
	# apexMesh.paint()

	# print(apexMesh.opts.items())
	return apexMesh
	# XXX

def GetGrids(gl, s, showWalls = True):

	gz = gl.GLGridItem()
	gz.scale(s,s,s)
	gz.translate(0, 0, -30)

	if not showWalls:
		return [gz]

	gx = gl.GLGridItem()
	gx.scale(s/2,s,s)
	gx.rotate(90, 0, 1, 0)
	gx.translate(10*s, 0, 10*s/2-30)

	gy = gl.GLGridItem()
	gy.scale(s,s/2,s)
	gy.rotate(90, 1, 0, 0)
	gy.translate(0, 10*s, 10*s/2-30)


	return gx, gy, gz

def TestApexes(gl, s):
	ApexesMesh = list()
	print(gl,"#################################")
	print(gl,"#################################")
	print(gl,"#################################")
	print(gl,"#################################")
	# ApexesMesh.append(GetApexMesh(gl,(0,-10*s,0)	, rows = x1, color = (1,.05,.3,.5)))
	# ApexesMesh.append(GetApexMesh(gl,(-10*s,-10*s,7*s)	, scale = 170 , rows = x	, color = (.5,.01,.3,.5)))
	# ApexesMesh.append(GetApexMesh(gl, (-10*s,0,10)	, scale = 17,color = (1,(.5*y)%1,(.1*s)%1,(.5*x)%1))
	# ApexesMesh.append(GetApexMesh(gl, (0,0,0)	, scale = 200,color = (1,(.5*y)%1,(.1*s)%1,(.5*x)%1))
	x, y = 1,2
	x+=1
	y+=1
	ApexesMesh.append(GetApexMesh(gl, (0,y*s*20,x*s*20), rows = x, cols = 5	, scale = 200,color = (.1,(.5*y)%1,(.1*s)%1,(.1*x)%1)))
	x+=1
	y+=1
	ApexesMesh.append(GetApexMesh(gl, (0,y*s*20,x*s*20), rows = x, cols = 5	, scale = 200,color = (.21,(.5*y)%1,(.1*s)%1,(.1*x)%1)))
	x+=1
	y+=1
	ApexesMesh.append(GetApexMesh(gl, (0,y*s*20,x*s*20), rows = x, cols = 5	, scale = 200,color = (.31,(.5*y)%1,(.1*s)%1,1)))
	x+=1
	y+=1
	ApexesMesh.append(GetApexMesh(gl, (0,y*s*20,x*s*20), rows = x, cols = 5	, scale = 200,color = (.41,(.5*y)%1,(.1*s)%1,(.1*x)%1)))
	x+=1
	y+=1
	ApexesMesh.append(GetApexMesh(gl, (0,y*s*20,x*s*20), rows = x, cols = 5	, scale = 200,color = (.51,(.5*y)%1,(.1*s)%1,(.1*x)%1)))
	x+=1
	y+=1
	ApexesMesh.append(GetApexMesh(gl, (0,y*s*20,x*s*20), rows = x, cols = 5	, scale = 200,color = (1,(.5*y)%1,(.1*s)%1,(.1*x)%1)))
	return ApexesMesh
	x, y = 5,1
	# x+=1
	# y+=1
	# ApexesMesh.append(GetApexMesh(gl, (0,y*s*20,x*s*20), rows = x, cols = 5	, scale = 200,color = (1,(.5*y)%1,(.1*s)%1,(.5*x)%1)))
	# x+=1
	# # y+=1
	# ApexesMesh.append(GetApexMesh(gl, (0,y*s*20,x*s*20), rows = x, cols = 5	, scale = 200,color = (1,(.5*y)%1,(.1*s)%1,(.5*x)%1)))
	# x+=1
	# y+=1
	# ApexesMesh.append(GetApexMesh(gl, (0,y*s*20,x*s*20), rows = x, cols = 5	, scale = 200,color = (1,(.5*y)%1,(.1*s)%1,(.5*x)%1)))
	# x+=1
	# # y+=1
	# ApexesMesh.append(GetApexMesh(gl, (0,y*s*20,x*s*20), rows = x, cols = 5	, scale = 200,color = (1,(.5*y)%1,(.1*s)%1,(.5*x)%1)))
	# x+=1
	# # y+=1
	# ApexesMesh.append(GetApexMesh(gl, (0,y*s*20,x*s*20), rows = x, cols = 5	, scale = 200,color = (1,(.5*y)%1,(.1*s)%1,(.5*x)%1)))
	# x+=1
	# x, y = 4,8
	# y+=1
	# ApexesMesh.append(GetApexMesh(gl, (0,y*s*20,x*s*20), rows = x, cols = 5	, scale = 200,color = (1,(.5*y)%1,(.1*s)%1,(.5*x)%1)))
	# y+=1
	# ApexesMesh.append(GetApexMesh(gl, (0,y*s*20,x*s*20), rows = x, cols = 5	, scale = 200,color = (1,(.5*y)%1,(.1*s)%1,(.5*x)%1)))
	# x+=1
	# # y+=1
	# ApexesMesh.append(GetApexMesh(gl, (0,y*s*20,x*s*20), rows = x, cols = 5	, scale = 200,color = (1,(.5*y)%1,(.1*s)%1,(.5*x)%1)))
	# x+=1
	# y+=1
	# ApexesMesh.append(GetApexMesh(gl, (0,y*s*20,x*s*20), rows = x, cols = 5	, scale = 200,color = (1,(.5*y)%1,(.1*s)%1,(.5*x)%1)))
	# x+=1
	# # y+=1
	# ApexesMesh.append(GetApexMesh(gl, (0,y*s*20,x*s*20), rows = x, cols = 5	, scale = 200,color = (1,(.5*y)%1,(.1*s)%1,(.5*x)%1)))
	# x+=1
	# # y+=1
	# ApexesMesh.append(GetApexMesh(gl, (0,y*s*20,x*s*20), rows = x, cols = 5	, scale = 200,color = (1,(.5*y)%1,(.1*s)%1,(.5*x)%1)))
	# x+=1
	# y+=1
	# ApexesMesh.append(GetApexMesh(gl, (0,y*s*20,x*s*20), rows = x, cols = 5	, scale = 200,color = (1,(.5*y)%1,(.1*s)%1,(.5*x)%1)))
	return ApexesMesh


def rotate(self):
	print("Rotating",self)
	rotateSpeed = self["build"]["rotateSpeed"]
	i = 0
	while(i < 1000):
		if self["build"]["rotate"]:
			self.mesh.rotate(8*(rotateSpeed*rotateSpeed),0,26,100, local=True)
		time.sleep(0.01)
		i +=1 

class Apex(Entity):
	def __init__(self,*args,**kwargs):
		print("New Apex Created!",args,kwargs)
		kwargs["rotate"] = True
		kwargs["rotateSpeed"] = 0.4
		self["build"] = kwargs
		self.mesh = None

		if args is not None and len(args)>0:
			print("AAAAAAAAAA",args,type(args[0]))
			if "GLMeshItem" in str(type(args[0])):
				self.mesh = args[0]

		if self.mesh is None:
			simple = True
			if simple:
				if args and len(args)>0:
					print("aaaaaaaaaaaa",args)
					self["build"]["point_on_plane"] = args[0]

				if "rows" not in self["build"]:
					self["build"]["rows"] = 3
					self["build"]["cols"] = 5
					self["build"]["scale"] = 200
					tf = (time.time()/1000)%1
					r,g,b,a = 0.7,0.1,0.7, 0.5
					self["build"]["color"] = ((r*tf)%1,(g*tf)%1,(b*tf)%1,0.3)

				# self.mesh = GetApexMesh(gl, self["build"]["point_on_plane"], rows = 3, cols = 5	, scale = 200,color = ((r*tf)%1,(g*tf)%1,(b*tf)%1,0.3))
				self.mesh = GetApexMesh(gl, self["build"]["point_on_plane"], rows = self["build"]["rows"], cols = self["build"]["cols"]	, scale = self["build"]["scale"],color = self["build"]["color"])
		xo.asyn(rotate,self)



class InteractiveWorld(gl.GLViewWidget):
	""" Override GLViewWidget with enhanced behavior!!!!!!!!! DO THIS TO EVERYTHING!!! GO PARENT UP

	"""
	#: Fired in update() method to synchronize listeners.
	#sigUpdate = QtCore.Signal(float, float)
	# App = None
	# source = None

	def __init__(self, app):
		# self.gl = gl
		super(InteractiveWorld,self).__init__()
		self.app = app
		# if self.App is None:
		# 	if app is not None:
		# 		self.App = app
		# 	else:
		# 		self.App = QtGui.QApplication([])
		self.setFocusPolicy(QtCore.Qt.ClickFocus)
		self.opts = {
			# will always appear at the center of the widget
			'center': QtGui.QVector3D(0, 0, 0),
			# distance of camera from center
			'distance': 10.0,
			# horizontal field of view in degrees
			'fov':  60,
			# camera's angle of elevation in degrees
			'elevation':  30,
			# camera's azimuthal angle in degrees
			# (rotation around z-axis 0 points along x-axis)
			'azimuth': 45,
			# glViewport params; None == whole widget
			'viewport': None,
			"rotationMethod" : "quaterion",
		}
		self.hold = None
		self.frames = 0.01
		# self.opts["rotationMethod"] = "quaterion"
		self.setBackgroundColor('k')
		self.items = []
		self.noRepeatKeys = [QtCore.Qt.Key_Right, QtCore.Qt.Key_Left,
							 QtCore.Qt.Key_Up, QtCore.Qt.Key_Down,
							 QtCore.Qt.Key_PageUp, QtCore.Qt.Key_PageDown]
		self.keysPressed = {}
		self.keyTimer = QtCore.QTimer()
		self.keyTimer.timeout.connect(self.evalKeyState)

		self.makeCurrent()

		self.ray = QtGui.QVector3D(0, 0, 0)
		self.select = False

		self.Gridxy = gl.GLGridItem()
		self.Gridyz = gl.GLGridItem()
		self.Gridxz = gl.GLGridItem()
		self.Axes = gl.GLAxisItem()
		self.Gridxy.setSize(6000,2000,3)
		self.Gridxy.setSpacing(200,200,0)
		self.Gridxy.translate(3000, 0, 0)

		self.Gridyz.setSize(1800,2000,3)
		self.Gridyz.setSpacing(200,200,0)
		self.Gridyz.translate(900, 0, 0)
		self.Gridyz.rotate(-90, 0, 1, 0)



		self.Gridxz.setSize(6000,2000,3)
		self.Gridxz.setSpacing(200,200,0)
		self.Gridxz.translate(3000, -1000, 0)
		self.Gridxz.rotate(-90, 1, 0, 0)
		self.Poss = []

		self.Plot = gl.GLScatterPlotItem()

		self.addItem(self.Plot)
		self.addItem(self.Gridxy)
		self.addItem(self.Gridyz)
		self.addItem(self.Gridxz)
		self.addItem(self.Axes)
		self._downpos = []

		#self.sigUpdate.connect(self.rayCast)
		self.setWindowTitle('Center of Gravity of Parts')
		self.marked = []
		self.chosen = None
		self.remove = []
		self.keep = []
		self.clear = False
		self.newEntries = []
		xo.subscribe("newApex",self.newApex)

	def load(self,source):
		# self.clear = True
		self.source = source
		self.newEntries = xo.GetXO(source).value()
		self.knownTypes = [gl.GLMeshItem,Apex]

	def setup(self, title = "universe", bgcolor = (0,0,0), distance=1410, elevation=17, azimuth = 187 ):
		# w.setCameraPosition(distance=210, elevation=17, azimuth = 187)
		self.setWindowTitle(title)
		self.setCameraPosition(distance=distance, elevation=elevation, azimuth = azimuth)
		self.setBackgroundColor(bgcolor)
		self.show()

	def GenerateObject(self,obj):
		if type(obj) in self.knownTypes:
			print("This is already generated...")
			return obj
		else:
			print("Generating 3D... from",str(type(obj)))
			if "dict" in str(type(obj)):
				print("More details")
			elif "list" in str(type(obj)):
				print("Simple Apex")
				return Apex(obj)

	def newApex(self,data):
		all = []
		if "list" in str(type(data)) and len(data)>0 and "list" in str(type(data[0])) and len(data[0])>1:
			all = data
		else:
			all = [data]
		for a in all:
			print("@@@@@@@@@@@@@@@@@@@@@")
			print(a)
			apex = self.GenerateObject(a)
			self.addItem(apex.mesh)
			time.sleep(0.1)

	def runGL(self):
		c = 0
		tempC=0
		app = self.app
		s = scale = 8
		showWalls = True
		apexList = list()
		# rotateSpeed[0] = 1 #0.01
		# if app is None or w is None:
		# 	app = QtGui.QApplication([])
		# 	# w = gl.GLViewWidget()
		# 	# w = WorldView()
		# 	w = PlotObject()
		# v = GraphicView(app)
		# global W, GL
		# global rotateSpeed
		# W[0] = w
		# GL[0] = gl
		# global Meshs
		Meshs = {}
		temp 		= Meshs["temp"] = []
		cache 	  	= Meshs["Cache"] = []
		cacheSpin 	= Meshs["CacheSpin"] = []

		Meshs["Keep"] = {}
		gridList 	= Meshs["Keep"]["grids"] = []
		apexList 	= Meshs["Keep"]["apexes"] = []
		beaconList 	= Meshs["Keep"]["beacons"] = []
		stills 	= Meshs["Keep"]["stills"] = []
		remove 		= Meshs["Remove"] = []

		# newData = False
		'''
		if len(gridList) == 0:
			grids = GetGrids(gl, s, showWalls)
			for g in grids:
				# w.addItem(g)
				gridList.append(g)
		'''
		"""
		if True:
		# previewApex = True
		# if previewApex:
		# 	# if not ranOnce and len(apexList) == 0:
		# 	ApexesMesh = TestApexes(gl, s)
		# 	# ranOnce = True
		# 	for apex in ApexesMesh:
		# 		# cacheSpin.append(apex)
		# 		'''
		# 		apexList.append(apex)
		# 		'''
		# 		# w.addItem(apex)
		# 		# apexList.append(apex)
		#
		# 	points = [(0,0,0), ]
		# 	points = [(a*10,a*10,a*10) for a in range(30)]
		# 	# pointsgl = PointsToGLRainbow(points)
		# 	pointsWithColors = [[a,(0,0,0,0)] for a in points]
		# 	for a in pointsWithColors:
		# 		x,y,z,f = [round(random.random(),2) for a in range(4) ]
		# 		a[1] = (x,y,z,f)
		#
		# 	# print(pointsWithColors)
		# 	# pointsgl = PointsToGL(pointsWithColors)
		# 	pointsgl = []
		# 	for pp in pointsWithColors:
		# 		pos = pp[0]
		# 		defColor = pp[1]
		#
		# 		mesh = GetPointMesh(gl, pos, oColor = defColor, Size = 9)
		# 		# pointsgl.append(mesh)
		# 		'''
		# 		cache.append(mesh)
		# 		'''
		#
		# 	# points = [(0,0,0), ]
		# 	pointers = [(a*-10,a*-10,a*10) for a in range(30)]
		# 	pointers = [[a,[a[0],a[1]-100,a[2]+100]] for a in pointers]
		# 	# pointsgl = PointsToGLRainbow(points)
		# 	pointersWithColors = [[a,(0,0,0,0)] for a in pointers]
		# 	for a in pointersWithColors:
		# 		x,y,z,f = [round(random.random(),2) for a in range(4) ]
		# 		a[1] = (x,y,z,f)
		#
		# 	# print(pointsWithColors)
		# 	# pointsgl = PointsToGL(pointsWithColors)
		# 	# pointsgl = []
		# 	for pp in pointersWithColors:
		# 		pos = pp[0]
		# 		defColor = pp[1]
		# 		# print("pos[0],pos[1]",pos[0],pos[1])
		# 		mesh = GetPointerMesh(gl, pos[0],pos[1], oColor = defColor, lineColor=defColor, lineWidth=3, dotSize=3)
		#
		# 		for m in mesh:
		# 			m.color = (1,1,1,1)
		# 			# pointsgl.append(m)
		# 			'''
		# 			cache.append(m)
		# 			'''
		# 			# cacheSpin.append(m)
		#
		# 	# ranOnce = True
		# 	# for pp in pointsgl:
		# 	# for p in pointsgl:
		# 		# print (p)
		# 		# input()
		# 		# cache.append(p)
		# 		# w.addItem(p)
		#
		# 	# for p in pointsgl:
		# 	# 	cache.append(p)
			 """
		# meshSend = [w]
		# meshSend.append(o)
		# cobj = CheckObject()
		# gd.SaveX("cobj",[cobj])
		# XXX
		clearNext = False
		# for i in range(1):
		#
		# 	ApexesMesh = TestApexes(gl, s)
		# 	ranOnce = True
		# 	for apex in ApexesMesh:
		# 		# print(("@"*30+"\n")*10)
		# 		# print(apex)
		# 		w.addItem(apex)
		# 		apexList.append(apex)
		# 		xo.apex = ["APEX",apex]
		# 	s+=10
		# shown = []
		while True:
			if True:
				pass
			if xo.run3d.value() == True:

				#Clear Scene
				remove = self.remove
				if self.clear:
					remove = self.items
					self.clear = False
				for o in remove:
					if o in self.items:
						self.removeItem(o)
					#
					# for k in Meshs["Keep"]:
					# 	if o in Meshs["Keep"][k]:
					# 		Meshs["Keep"][k].remove(o)
					#
					# if o in Meshs["Cache"]:
					# 	Meshs["Cache"].remove(o)
					#
					# if o in Meshs["CacheSpin"]:
					# 	Meshs["CacheSpin"].remove(o)
					if o in self.remove:
						self.remove.remove(o)

				######## Incoming Data
				for new in self.newEntries:
					#Generate Object
					self.newApex(new)
					# shown.append(new)

					# if new.mesh not in self.keep:
					# 	self.keep.append(new.mesh)
				self.newEntries = []
				# for new in self.newEntries:
				# 	#Generate Object
				# 	if new not in shown:
				# 		shown.append(new)
				# 		new = self.GenerateObject(new)
				# 		if new.mesh not in self.keep:
				# 			# self.addItem(new.mesh)
				# 			self.keep.append(new.mesh)
				#
				# for show in self.keep:
				# 	if show not in self.items:
				# 		self.addItem(show)
				# self.ne
				# while(len(self.newEntries)>0):
				# 	# self.newEntries.pop()
				# 	pass

					#Log new object
					# xo.

				# legacy
				# print(xo.apex)
				# if xo.newApex.value() is not None and xo.newApex.value() not in w.items:
				# 	apexList.append(xo.newApex.value())
				# 	xo.newApex = None

					# w.addItem(xo.newApex.value())
				'''
				for o in cache + cacheSpin + gridList + apexList + beaconList + stills + temp:
					if o not in w.items:
						self.addItem(o)
				'''
						# pass

				# for o in Meshs["temp"]:
				# 	if o not in w.items:
				# 		w.addItem(o)
						# remove.append(o)


				'''
				doRotate = True
				if doRotate:
					if rotateSpeed[0] > 0:
						for obj in apexList+cacheSpin:
							# print(type(obj))
							# print(obj.depthValue())
							obj.rotate(8*(rotateSpeed[0]*rotateSpeed[0]),0,26,100, local=True)
							if c%111 == 0:
								if random.choice((True,False))*random.choice((True,False))*random.choice((True,False))*random.choice((True,False))*1:
									c+=1
									print("AAAAAAAAAAAAAAAAAAAAAAA")
									print("AAAAAAAAAAAAAAAAAAAAAAA")
									print("AAAAAAAAAAAAAAAAAAAAAAA")
									print("AAAAAAAAAAAAAAAAAAAAAAA")
									obj.setGLOptions('additive')
							# obj.setColor((0.1,(c*0.1*0.1)%1,(c*0.2*0.1)%1,(c*0.2*0.1)%1))
							# obj.setEdgeColor((0.1,(c*0.1*0.1)%1,(c*0.2*0.1)%1,(c*0.2*0.1)%1))
							# obj.scale(c*0.01+10,c*0.01+10,c*0.01+10)
							# for v in obj.
							# vx,vy = 0.1*c*math.sin(c%math.pi),0.1*c*math.sin(c%math.pi)
							# print(vx,vy)
							# obj.translate(vx,vy,0)
							# obj.scale(scale,scale,scale)

						for obj in beaconList:
							# print(type(obj))
							# print(obj.depthValue())
							obj.rotate(8*(rotateSpeed[0]*rotateSpeed[0]),0,10,100, local=True)
						#
						# for apex in :
						# 	# apex.rotate(8*(rotateSpeed[0]*rotateSpeed[0]),0,26,100, local=False)
						# 	apex.rotate(8*(rotateSpeed[0]*rotateSpeed[0]),0,26,100, local=True)
				'''

				# if not newData:
				# 	#rotateSpeed[0]+=0.02
				# 	rotateSpeed[0] = round(rotateSpeed[0]+0.01,2)
				# 	newData = True
				# else:
				# 	rotateSpeed[0] = 1
				# 	dashSleep = 0.01


				c+=1
				# if c % 20 == 0:
				# 	if clearNext:
				# 		# print("EEEEEEEEEEEEEEEEEEEEEE")
				# 		clearMesh(Meshs["temp"])
				# 		clearNext = False
				# 	else:
				# 		# print("RRRRRRRRRRRRRRRRRRRRRRR")
				# 		pass
				# 	if c % 20 == 0:
				# 		# w.setBackgroundColor((9,0,23))
				# 		pass
				# 	# print("20")
				# 	# if o not in w.items:
				# 	for o in Meshs["temp"]:
				# 		clearNext = True
				# 		# print("...//////")
				# 		# print("...//////")
				# 		# print("...//////")
				# 		# print("...//////")
				# 		# print("...//////")
				# 		# print("...//////")
				# 		# print("...//////")
				# 		# clearMesh(Meshs["temp"])
				# 		# remove.append(o)
				# 		# w.addItem(o)

				if(c>1000000):
					tempC+=1
					c=0

			self.app.processEvents()
			time.sleep(self.frames)
			# print("UPDATED")


	def mousePressEvent(self, ev):
		""" Store the position of the mouse press for later use.

		"""
		print("press")
		print("Pressed button", ev.button(), "at", ev.pos())

		self.mousePos = ev.pos()
		if ev.button() == 2:
			self.select = True
		else:
			self.select = False
		intersecting = self.itemsAt((self.mousePos.x(), self.mousePos.y(), 3, 3))
		print(intersecting)
		# print (self.itemsAt((self.mousePos.x(), self.mousePos.y(), 3, 3)))
		print(intersecting)
		if len(intersecting) > 0:
			self.chosen = intersecting[0]

		self._downpos = self.mousePos

		ctrl = ev.modifiers() & QtCore.Qt.ControlModifier
		if ctrl:
			print("hold")
			self.hold = QtCore.Qt.ControlModifier

		shift = ev.modifiers() & QtCore.Qt.ShiftModifier
		if shift:
			if self.chosen is None:
				pass
				O, ray_world = self.mPosition(ev)
				intersection = intersect(rayPoint = O.tolist()[0], rayDirection = ray_world.tolist()[0])
				point_on_plane = intersection
				# xx = GetApexMesh(gl,point_on_plane)
				# ApexesMesh.append(GetApexMesh(gl, (0,y*s*20,x*s*20), rows = x, cols = 5	, scale = 200,color = (.1,(.5*y)%1,(.1*s)%1,(.1*x)%1)))
				tf = (time.time()/1000)%1
				r,g,b,a = 0.7,0.1,0.7, 0.5
				# xx = GetApexMesh(gl, point_on_plane, rows = 3, cols = 5	, scale = 200,color = ((r+tf)%1,(g+tf)%1,(b+tf)%1,(a+tf)%1))
				self.newEntries.append(Apex(point_on_plane))
				# xo.newApex = xx
				# self.addItem(apex)
				# return True
		super(InteractiveWorld, self).mousePressEvent(ev)

	def mouseMoveEvent(self, ev):
		""" Allow Shift to Move and Ctrl to Pan.

		"""
		O, ray_world = self.mPosition(ev)
		print(self.mPosition(ev))
		if self.chosen is not None:
			print("MOVING OBJECT",self.chosen)
		else:
			print("move")
		shift = ev.modifiers() & QtCore.Qt.ShiftModifier
		# ctrl = ev.modifiers() & QtCore.Qt.ControlModifier
		ctrl = ev.modifiers() & QtCore.Qt.ControlModifier
		if ctrl:
			print("hold")
			self.hold = QtCore.Qt.ControlModifier

		if self.chosen is not None:
			print("!!!!!!!!!!",self.chosen.__dir__())
			print("!!!!!!!!!!",self.chosen.viewTransform())
			print("OOOOOOO",list(O.tolist()[0]))
			print("DDDDDD",list(ray_world[0]))
			intersection = intersect(rayPoint = O.tolist()[0], rayDirection = ray_world.tolist()[0])
			point_on_plane = intersection
			# chosen
			# self.chosen.translate(-dy,-dx,0)
			self.chosen.resetTransform()
			self.chosen.translate(point_on_plane[0],point_on_plane[1],0)
			self.chosen.scale(100,100,100)
		else:
			shift = ev.modifiers() & QtCore.Qt.ShiftModifier
			if shift:
				if self.chosen is None:
					pass
					O, ray_world = self.mPosition(ev)
					intersection = intersect(rayPoint = O.tolist()[0], rayDirection = ray_world.tolist()[0])
					point_on_plane = intersection
					# xx = GetApexMesh(gl,point_on_plane)
		# ApexesMesh.append(GetApexMesh(gl, (0,y*s*20,x*s*20), rows = x, cols = 5	, scale = 200,color = (.1,(.5*y)%1,(.1*s)%1,(.1*x)%1)))
					tf = (time.time()/10)%1
					print("tf",tf)
					r,g,b,a = 0.7,0.1,0.7, 0.5
					xx = GetApexMesh(gl, point_on_plane, rows = 3, cols = 5	, scale = 200,color = ((r*tf)%1,(g*tf)%1,(b*tf)%1,0.3))
					# xx = GetApexMesh(gl, point_on_plane, rows = 3, cols = 5	, scale = 200,color = (.1,(.7)%1,(.1*4)%1,(.8)%1))
					# xo.newApex = xx
					self.newEntries.append(Apex(xx))


			# print("$$$$$$$$",self.chosen.collidingItems())

		# if shift:
		# 	y = ev.pos().y()
		# 	if not hasattr(self, '_prev_zoom_pos') or not self._prev_zoom_pos:
		# 		self._prev_zoom_pos = y
		# 		return
		# 	dy = y - self._prev_zoom_pos
		# 	def delta():
		# 		return -3* dy
		# 		return -dy * 5
		# 	ev.delta = delta
		# 	ev.delta = delta
		# 	# ev.angleData = lambda :self.angleData(ev.pos().x(),ev.pos().y())
		# 	ev.angleData = delta
		# 	self._prev_zoom_pos = y
		# 	# self.wheelEvent(ev)
		if ctrl:
			pos = ev.pos().x(), ev.pos().y()
			if not hasattr(self, '_prev_pan_pos') or not self._prev_pan_pos:
				self._prev_pan_pos = pos
				return
			dx = pos[0] - self._prev_pan_pos[0]
			dy = pos[1] - self._prev_pan_pos[1]

			self._prev_pan_pos = pos
			if self.chosen is not None:
				pass
			else:
				self.pan(dx, dy, 0, relative=True)
			print(pos)

		elif self.chosen is None and self.hold == None:
			print("No Hold")
			super(InteractiveWorld, self).mouseMoveEvent(ev)
			pass

	def mouseReleaseEvent(self, ev):

		print("release")
		""" Allow for single click to move and right click for context menu.

		Also emits a sigUpdate to refresh listeners.
		"""
		super(InteractiveWorld, self).mouseReleaseEvent(ev)
		if self._downpos == ev.pos() or True:
			x = ev.pos().x()
			y = ev.pos().y()
			if ev.button() == 2 :
				print("############")
				self.mPosition(ev)
			elif ev.button() == 1:
				print("############YYYYYYY")
				x = x - self.width() / 2
				y = y - self.height() / 2
				#self.pan(-x, -y, 0, relative=True)
				print(self.opts['center'])
				print(x,y)
		self._prev_zoom_pos = None
		self._prev_pan_pos = None
		self.chosen = None
		self.hold = None

	def keyPressEvent(self, ev):
			print(ev)

	def mPosition(self, ev=None):
		#This function is called by a mouse event
		## Get mouse coordinates saved when the mouse is clicked( incase dragging)
		if ev is not None:
			print("mmmmmmmm")
			mx = ev.pos().x()
			my = ev.pos().y()
		else:
			mx = self._downpos.x()
			my = self._downpos.y()
		print("#############, mPosition")
		#This function is called by a mouse event
		## Get mouse coordinates saved when the mouse is clicked( incase dragging)
		# mx = self._downpos.x()
		# my = self._downpos.y()
		self.Candidates = [] #Initiate a list for storing indices of picked points
		#Get height and width of 2D Viewport space
		view_w = self.width()
		view_h = self.height()
		#Convert pixel values to normalized coordinates
		x = 2.0 * mx / view_w - 1.0
		y = 1.0 - (2.0 * my / view_h)
		# Convert projection and view matrix to numpy types and inverse them
		PMi = self.projectionMatrix().inverted()[0]
		# PMi = numpy.matrix([PMi[0:4],
		#                    PMi[4:8],
		#                    PMi[8:12],
		#                    PMi[12:16]])
		VMi = self.viewMatrix().inverted()[0]
		# VMi = numpy.matrix([VMi[0:4],
		#                    VMi[4:8],
		#                    VMi[8:12],
		#                    VMi[12:16]])
		#Move to clip coordinates by chosing z= -1 and w 1 (Dont understand this part)
		# Q1: Why are we picking arbitrary -1 for z?
		ray_clip = QtGui.QVector4D(x, y, -1.0, 1.0) # get transpose for matrix multiplication
		# Q2 = Clip space should clip some of the scene depending on the zoom. How is it done? Is it implicit
		# in the transformation matrices?
		# Convert to eye space by view matrix
		ray_eye = PMi * ray_clip
		ray_eye.setZ(-1)
		ray_eye.setW(0)
		#Convert to world coordinates
		ray_world = VMi * ray_eye
		ray_world = QtGui.QVector3D(ray_world.x(), ray_world.y(), ray_world.z()) # get transpose for matrix multiplication
		ray_world.normalize()
		#ray_world = ray_world / numpy.linalg.norm(ray_world) # normalize to get the ray
		# Q3: Since we normalize this vector, does it mean the values are a b c values of a ray definition in
		# linear algebra such as z = ax+by+c
		# Now I 'll use the ray intersection with spheres. I assume every point is a sphere with a radius
		#Please see http://antongerdelan.net/opengl/raycasting.html scroll down to spehere intersection
		O = numpy.matrix(self.cameraPosition())  # camera position should be starting point of the ray
		ray_world = numpy.matrix([ray_world.x(), ray_world.y(), ray_world.z()])
		# Q4: Is this approach correct? Is starting point really the camera coordinates obtained like this?
		print("XXXXXXXXXXX",O, ray_world)
		return O, ray_world
		for i, C in enumerate(self.Poss): # Iterate over all points
			OC = O - C
			b = numpy.inner(ray_world, OC)
			b = b.item(0)
			c = numpy.inner(OC, OC)
			#Q5: When the plot function is called with pxMode = False the sizes should reflect the size of point
			#dots in world coordinates. So I assumed they were the diameter of the spheres. Is this correct? Otherwise how do I reach the
			#diameter of spheres in terms of world coordinates?
			c = c.item(0) - (self.Sizes[i]/2)**2   #numpy.square((self.Sizes[i]))
			bsqr = numpy.square(b)
			if (bsqr - c) >= 0: # means intersection
				self.Candidates.append(self.GlobalInds[i])

		print(self.Candidates)


	# def plotGLPlot(self, objs):
	# 	poss = numpy.array([0, 0, 0])
	# 	self.Poss = []
	# 	self.GlobalInds = []
	# 	weights = numpy.array(0, dtype=float)
	# 	def pswc (x) : return 10 * x**0.25 #pseudoweight calculation with exponential scaling
	# 	for obj in objs:
	# 		for i,cogs in enumerate(obj.CoG):
	# 			for cog in cogs:
	# 				#cog[1] = 0
	# 				if obj.PieceWeight[i]:
	# 					poss = numpy.vstack([poss,numpy.asarray(cog.T)])
	# 					self.Poss.append(numpy.matrix(cog.T)) # for picking stuff
	# 					self.GlobalInds.append(obj.Index[i])
	# 					pw = pswc(obj.PieceWeight[i])
	# 					weights = numpy.append(weights, pw)
	#
	#
	#
	# 	maxw = max(weights)
	# 	threshold = numpy.mean(weights)
	# 	self.Colors = numpy.empty([len(weights),4])
	# 	for i, pw in enumerate(weights):
	# 		if pw <= threshold:
	# 			c = pw / maxw
	# 			self.Colors[i] = numpy.array([c,1,0,0.7])
	# 		else:
	# 			c = 1 - pw / maxw
	# 			self.Colors[i] = numpy.array([1,c,0,0.7])
	#
	# 	self.removeItem(self.Plot)
	# 	self.Plot = gl.GLScatterPlotItem()
	# 	self.Plot.setData(pos=poss, size=weights, color=self.Colors, pxMode=False)
	# 	self.Sizes = weights
	# 	self.addItem(self.Plot)
	# 	self.show()

	# def angleData(self,x,y):
	# 	return angleD(x,y)

	#
	# def mPosition0(self, ev=None):
	# 	#This function is called by a mouse event
	# 	## Get mouse coordinates saved when the mouse is clicked( incase dragging)
	# 	if ev:
	# 		mx = ev.pos().x()
	# 		my = ev.pos().y()
	# 	else:
	# 		mx = self._downpos.x()
	# 		my = self._downpos.y()
	# 	self.Candidates = [] #Initiate a list for storing indices of picked points
	# 	#Get height and width of 2D Viewport space
	# 	view_w = self.width()
	# 	view_h = self.height()
	# 	#Convert pixel values to normalized coordinates
	# 	x = 2.0 * mx / view_w - 1.0
	# 	y = 1.0 - (2.0 * my / view_h)
	# 	# Convert projection and view matrix to numpy types and inverse them
	# 	PM = numpy.matrix([self.projectionMatrix().data()[0:4],
	# 					   self.projectionMatrix().data()[4:8],
	# 					   self.projectionMatrix().data()[8:12],
	# 					   self.projectionMatrix().data()[12:16]])
	# 	PMi = numpy.linalg.inv(PM)
	# 	VM = numpy.matrix([self.viewMatrix().data()[0:4],
	# 					   self.viewMatrix().data()[4:8],
	# 					   self.viewMatrix().data()[8:12],
	# 					   self.viewMatrix().data()[12:16]])
	# 	VMi = numpy.linalg.inv(VM)
	# 	#Move to clip coordinates by chosing z= -1 and w 1 (Dont understand this part)
	# 	# Q1: Why are we picking arbitrary -1 for z?
	# 	ray_clip = numpy.matrix([x, y, -1.0, 1.0]).T # get transpose for matrix multiplication
	# 	# Q2 = Clip space should clip some of the scene depending on the zoom. How is it done? Is it implicit
	# 	# in the transformation matrices?
	# 	# Convert to eye space by view matrix
	# 	ray_eye = PMi * ray_clip
	# 	ray_eye[2] = -1
	# 	ray_eye[3] = 0
	# 	#Convert to world coordinates
	# 	ray_world = VMi * ray_eye
	# 	ray_world = ray_world[0:3].T # get transpose for matrix multiplication
	# 	ray_world = ray_world / numpy.linalg.norm(ray_world) # normalize to get the ray
	# 	# Q3: Since we normalize this vector, does it mean the values are a b c values of a ray definition in
	# 	# linear algebra such as z = ax+by+c
	# 	# Now I 'll use the ray intersection with spheres. I assume every point is a sphere with a radius
	# 	#Please see http://antongerdelan.net/opengl/raycasting.html scroll down to spehere intersection
	# 	O = numpy.matrix(self.cameraPosition())  # camera position should be starting point of the ray
	# 	# Q4: Is this approach correct? Is starting point really the camera coordinates obtained like this?
	# 	print(O, ray_world)
	# 	for i, C in enumerate(self.Poss): # Iterate over all points
	# 		OC = O - C
	# 		b = numpy.inner(ray_world, OC)
	# 		b = b.item(0)
	# 		c = numpy.inner(OC, OC)
	# 		#Q5: When the plot function is called with pxMode = False the sizes should reflect the size of point
	# 		#dots in world coordinates. So I assumed they were the diameter of the spheres. Is this correct? Otherwise how do I reach the
	# 		#diameter of spheres in terms of world coordinates?
	# 		c = c.item(0) - numpy.square((self.Sizes[i] / 2 ))
	# 		bsqr = numpy.square(b)
	# 		if (bsqr - c) >= 0: # means intersection
	# 			self.Candidates.append(self.GlobalInds[i])
	#
	# 	print(self.Candidates)
