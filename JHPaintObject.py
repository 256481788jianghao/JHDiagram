
import wx
import math

class JHDragState:
	DRAG_INIT = 0
	DRAG_MOVING = 1
	DRAG_SHAPEPOINT = 2

class JHFocusState:
	FOCUS_ON = 0
	FOCUS_OFF = 1
	FOCUS_NONE = 2

class JHColour:
	BLACK = wx.Colour(0x00,0x00,0x00)
	WHITE = wx.Colour(0xFF,0xFF,0xFF)
	RED = wx.Colour(0xFF,0x00,0x00)

class JHObject:
	def __init__(self,Level = 0,Zoom = 1):
		self.level = Level #no use for now
		self.zoom = Zoom
		self.borderColour = JHColour.BLACK
		self.backgroundColour = JHColour.WHITE
		self.path = None
		self.isFocus = False
		self.dragState = JHDragState.DRAG_INIT
		self.dragTPoint = None
		
	def Draw(self,gc):
		pass
		
	def Focus(self,position):
		return JHFocusState.FOCUS_NONE
		
	def Dragging(self,position):
		pass
	
	def __def__(self):
		pass
		
class JHPoint(JHObject):
	def __init__(self,X = 0,Y = 0):
		JHObject.__init__(self)
		self.point = wx.Point(X,Y)
	
	def __def__(self):
		pass
		
class JHReShapePoint(JHPoint):
	def __init__(self,X=0,Y=0):
		JHPoint.__init__(self,X,Y)
		self.flagRect = JHRect(X - 4,Y - 4, 8, 8)
		self.flagRect.borderColour = JHColour.RED
		self.flagRect.backgroundColour = JHColour.RED
		
	def Move(self,dx,dy):
		self.point = self.point + wx.Size(dx,dy)
		self.flagRect.Offset(dx,dy)
	def Contains(self,point):
		return self.flagRect.Contains(point)
		
	def Draw(self,gc):
		self.flagRect.Draw(gc)
		
	def __def__(self):
		pass
		
class JHLine(JHObject):
	def __init__(self,X0 = 0,Y0 = 0, X1= 0, Y1 = 0,Width = 1):
		JHObject.__init__(self)
		self.startPoint = JHReShapePoint(X0,Y0)
		self.endPoint = JHReShapePoint(X1,Y1)
		self.width = Width
		self.isDragStartPoint = False
		
	def Focus(self,position):
		if not self.isFocus and self.Contains(position):
			self.isFocus = True
			return JHFocusState.FOCUS_ON
		elif self.isFocus and not self.Contains(position):
			self.isFocus = False
			self.dragState = JHDragState.DRAG_INIT
			return JHFocusState.FOCUS_OFF
		else:
			return JHFocusState.FOCUS_NONE
			
	def Dragging(self,position):
		if JHDragState.DRAG_INIT == self.dragState:
			self.dragTPoint = position
			if self.startPoint.Contains(position):
				self.isDragStartPoint = True
				self.dragState = JHDragState.DRAG_SHAPEPOINT
				wx.LogMessage('drag start')
			elif self.endPoint.Contains(position):
				self.isDragStartPoint = False
				self.dragState = JHDragState.DRAG_SHAPEPOINT
				wx.LogMessage('drag end')
			else:
				self.dragState = JHDragState.DRAG_MOVING
				wx.LogMessage('drag move')
		elif JHDragState.DRAG_MOVING == self.dragState:
			vector = position - self.dragTPoint
			self.dragTPoint = position
			dx = vector.x
			dy = vector.y
			self.startPoint.Move(dx,dy)
			self.endPoint.Move(dx,dy)
		else:
			vector = position - self.dragTPoint
			self.dragTPoint = position
			dx = vector.x
			dy = vector.y
			if self.isDragStartPoint:
				self.startPoint.Move(dx,dy)
			else:
				self.endPoint.Move(dx,dy)
	
	def Contains(self,point):
		if self.DistanceToPoint(point) < 5 and self.path.GetBox().Contains(wx.Point2D(point)):
			return True
		return False
		
	def DistanceToPoint(self,point):
		x0 = self.startPoint.point.x
		y0 = self.startPoint.point.y
		x1 = self.endPoint.point.x
		y1 = self.endPoint.point.y
		b = x1 - x0
		a = y0 - y1
		c = - y0*x1 + y1*x0
		return abs(a*point.x+b*point.y+c)/math.sqrt(a**2+b**2)
		
	def Draw(self,gc):
		paintWidth = int(self.width * self.zoom + 0.5)
		pen = wx.Pen(width = paintWidth, colour = self.borderColour)
		brush = wx.Brush(colour = self.backgroundColour)
		gc.SetPen(pen)
		gc.SetBrush(brush)
		self.path = gc.CreatePath()
		
		startPoint = wx.Point2D(self.startPoint.point)
		endPoint = wx.Point2D(self.endPoint.point)
		self.path.MoveToPoint(startPoint)
		self.path.AddLineToPoint(endPoint)
		self.path.CloseSubpath()
		
		gc.StrokePath(self.path)
		gc.FillPath(self.path)
		
		if self.isFocus:
			self.startPoint.Draw(gc)
			self.endPoint.Draw(gc)
		
	def __def__(self):
		pass
		
class JHRect(JHObject):
	def __init__(self,X = 0,Y = 0,Width = 100,Height = 100,Radius = 0):
		JHObject.__init__(self)
		startPoint = wx.Point(X,Y)
		size = wx.Size(Width,Height)
		self.rect = wx.Rect(startPoint,size)
		self.radius = Radius
		
	def ReSize(self, Width, Height):
		size = wx.Size(Width,Height)
		ReSize(size)
	def ReSize(self, Size):
		self.rect.SetSize(Size)
		
	def Offset(self,dx,dy):
		self.rect.Offset(dx,dy)
		
	def Contains(self,point):
		return self.rect.Contains(point)
		
	def Draw(self,gc):
		pen = wx.Pen(colour = self.borderColour)
		brush = wx.Brush(colour = self.backgroundColour)
		gc.SetPen(pen)
		gc.SetBrush(brush)
		path = gc.CreatePath()
		path.AddRoundedRectangle(self.rect.X,self.rect.Y,self.rect.Width,self.rect.Height,self.radius)
		gc.StrokePath(path)
		gc.FillPath(path)
		
	
	def __def__(self):
		pass