
import wx

class JHColour:
	BLACK = wx.Colour(0x00,0x00,0x00)
	WHITE = wx.Colour(0xFF,0xFF,0xFF)
	RED = wx.Colour(0xFF,0x00,0x00)

class JHObject:
	def __init__(self,Level = 0,Zoom = 1,BorderColour = JHColour.BLACK,BackgroundColour = JHColour.WHITE,IsTempObj = False):
		self.level = Level #no use for now
		self.zoom = Zoom
		self.borderColour = BorderColour
		self.backgroundColour = BackgroundColour
		self.isTempObj = IsTempObj
		self.path = None
		self.isPointOn = False
		
	def Draw(self,gc):
		pass
		
	def PointOn(self,position,paintList):
		return False
	
	def __def__(self):
		pass
		
class JHPoint(JHObject):
	def __init__(self,X = 0,Y = 0):
		JHObject.__init__(self)
		self.point = wx.Point(X,Y)
		
	def PonitOn(self,position,paintList):
		if position == self.point:
			return True
		return False
	
	def __def__(self):
		pass
		
class JHLine(JHObject):
	def __init__(self,X0 = 0,Y0 = 0, X1= 0, Y1 = 0,Width = 1):
		JHObject.__init__(self)
		self.startPoint = JHPoint(X0,Y0)
		self.endPoint = JHPoint(X1,Y1)
		self.width = Width
		
	def PointOn(self,position,paintList):
		size = wx.Size(5,5)
		startRect = wx.Rect(self.startPoint.point,size)
		endRect = wx.Rect(self.endPoint.point,size)
		if startRect.Contains(position):
			flagRect = JHRect(startRect.X,startRect.Y,startRect.Width,startRect.Height)
			flagRect.isTempObj = True
			flagRect.borderColour = JHColour.RED
			flagRect.backgroundColour = JHColour.RED
			paintList.append(flagRect)
			return True
		elif endRect.Contains(position):
			flagRect = JHRect(endRect.X,endRect.Y,endRect.Width,endRect.Height)
			flagRect.isTempObj = True
			flagRect.borderColour = JHColour.RED
			flagRect.backgroundColour = JHColour.RED
			paintList.append(flagRect)
			return True
		return False
		
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
		self.startPoint = wx.Point(X,Y)
		self.size = wx.Size(Width,Height)
		self.rect = wx.Rect(self.startPoint,self.size)
		self.radius = Radius
		
	def ReSize(self, Width, Height):
		self.size = wx.Size(Width,Height)
		self.rect = wx.Rect(self.startPoint,self.size)
	def ReSize(self, Size):
		self.size = wx.Size(Size)
		self.rect = wx.Rect(self.startPoint,self.size)
		
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