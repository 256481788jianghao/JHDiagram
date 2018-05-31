
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
		self.isSelected = False
		self.dragState = JHDragState.DRAG_INIT
		self.dragTPoint = None
		self.children = []
		
	def Draw(self,gc):
		pass
		
	def Focus(self,position):
		return JHFocusState.FOCUS_NONE
		
	def Select(self,area):
		return self.isSelected
		
	def Dragging(self,position):
		pass
		
	def Contains(self,point):
		return False
		
	def PerpareSave(self):
		self.path = None
		for obj in self.children:
			obj.PerpareSave()
	
	def __def__(self):
		pass
		
class JHPoint(JHObject):
	def __init__(self,X = 0,Y = 0):
		JHObject.__init__(self)
		self.point = wx.Point(X,Y)
		
	def ReSet(self,Point):
		self.point = Point
	
	def __def__(self):
		pass
		
class JHReShapePoint(JHPoint):
	def __init__(self,X=0,Y=0):
		JHPoint.__init__(self,X,Y)
		self.flagRect = JHRect(X - 4,Y - 4, 8, 8)
		self.flagRect.borderColour = JHColour.RED
		self.flagRect.backgroundColour = JHColour.RED
		self.children.append(self.flagRect)
		
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
		self.midPoint = JHReShapePoint((X0+X1)/2,(Y0+Y1)/2)
		self.width = Width
		self.isDragStartPoint = False
		self.children.append(self.startPoint)
		self.children.append(self.midPoint)
		self.children.append(self.endPoint)
		
	def Focus(self,position):
		if self.isSelected:
			self.isFocus = True
		else:
			self.isFocus = False
	
	def Select(self,rect):
		pos = rect.GetPosition()
		if rect.IsEmpty():
			rect.ReSize(wx.Size(2,2))
		size = rect.GetSize()
		centerPos = pos + rect.GetSize()/2
		dis = self.DistanceToPoint(centerPos)
		disP = wx.Point2D(pos).GetDistance(wx.Point2D(centerPos))
		if disP > dis:
			self.isSelected = True
		else:
			self.isSelected = False
			
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
			self.midPoint.Move(dx,dy)
		else:
			vector = position - self.dragTPoint
			self.dragTPoint = position
			dx = vector.x
			dy = vector.y
			if self.isDragStartPoint:
				self.startPoint.Move(dx,dy)
			else:
				self.endPoint.Move(dx,dy)
			tPoint = (self.startPoint.point + self.endPoint.point)/2
			diff = tPoint - self.midPoint.point
			self.midPoint.Move(diff.x,diff.y)
	
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
			self.midPoint.Draw(gc)
		
	def __def__(self):
		pass
		
class JHRect(JHObject):
	def __init__(self,X = 0,Y = 0,Width = 100,Height = 100,Radius = 0):
		JHObject.__init__(self)
		startPoint = wx.Point(X,Y)
		size = wx.Size(Width,Height)
		self.rect = wx.Rect(startPoint,size)
		self.radius = Radius
		
	def ReSize(self, Size):
		self.rect.SetSize(Size)
		
	def Offset(self,dx,dy):
		self.rect.Offset(dx,dy)
		
	def SetPosition(self, pos):
		self.rect.SetPosition(pos)
		
	def SetTopLeft(self, p):
		self.rect.SetTopLeft(p)
		
	def SetBottomRight(self,p):
		self.rect.SetBottomRight(p)
		
	def GetPosition(self):
		return self.rect.GetPosition()
		
	def GetSize(self):
		return self.rect.GetSize()
		
	def IsEmpty(self):
		return self.rect.IsEmpty()
	
		
	def Contains(self,point):
		return self.rect.Contains(point)
		
	def Draw(self,gc):
		pen = wx.Pen(colour = self.borderColour)
		brush = wx.Brush(colour = self.backgroundColour)
		gc.SetPen(pen)
		gc.SetBrush(brush)
		self.path = gc.CreatePath()
		self.path.AddRoundedRectangle(self.rect.X,self.rect.Y,self.rect.Width,self.rect.Height,self.radius)
		gc.StrokePath(self.path)
		gc.FillPath(self.path)
		
	
	def __def__(self):
		pass