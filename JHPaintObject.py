
import wx

class JHColour:
	BLACK = wx.Colour(0x00,0x00,0x00)
	WHITE = wx.Colour(0xFF,0xFF,0xFF)

class JHObject:
	def __init__(self,Level = 0,Zoom = 1,BorderColour = JHColour.BLACK,BackgroundColour = JHColour.WHITE):
		self.level = Level #no use for now
		self.zoom = Zoom
		self.borderColour = BorderColour
		self.backgroundColour = BackgroundColour
		
	def Draw(self,gc):
		pass
	
	def __def__(self):
		pass
		
class JHPoint(JHObject):
	def __init__(self,X = 0,Y = 0):
		JHObject.__init__(self)
		self.point = wx.Point(X,Y)
	
	def __def__(self):
		pass
		
class JHLine(JHObject):
	def __init__(self,X0 = 0,Y0 = 0, X1= 0, Y1 = 0,Width = 1):
		JHObject.__init__(self)
		self.startPoint = JHPoint(X0,Y0)
		self.endPoint = JHPoint(X1,Y1)
		self.width = Width
		
	def Draw(self,gc):
		paintWidth = int(self.width * self.zoom + 0.5)
		pen = wx.Pen(width = paintWidth, colour = self.borderColour)
		brush = wx.Brush(colour = self.backgroundColour)
		gc.SetPen(pen)
		gc.SetBrush(brush)
		path = gc.CreatePath()
		
		startPoint = wx.Point2D(self.startPoint.point)
		endPoint = wx.Point2D(self.endPoint.point)
		path.MoveToPoint(startPoint)
		path.AddLineToPoint(endPoint)
		path.CloseSubpath()
		
		gc.StrokePath(path)
		gc.FillPath(path)
		
	def __def__(self):
		pass
		
class JHRect(JHObject):
	def __init__(self,X = 0,Y = 0,Width = 100,Height = 100,Radius = 0):
		JHObject.__init__(self)
		self.x = X
		self.y = Y
		self.width = Width
		self.height = Height
		self.radius = Radius
		
	def Draw(self,gc):
		pen = wx.Pen(colour = self.borderColour)
		brush = wx.Brush(colour = self.backgroundColour)
		gc.SetPen(pen)
		gc.SetBrush(brush)
		path = gc.CreatePath()
		path.AddRoundedRectangle(self.x, self.y, self.width, self.height,self.radius)
		gc.StrokePath(path)
		gc.FillPath(path)
		
	
	def __def__(self):
		pass