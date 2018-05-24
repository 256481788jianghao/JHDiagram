"""Subclass of BaseMainForm, which is generated by wxFormBuilder."""

import wx
import BaseMainForm
import pickle
from JHPaintObject import *


# Implementing BaseMainForm
class MainForm( BaseMainForm.BaseMainForm ):
	def __init__( self, parent ):
		BaseMainForm.BaseMainForm.__init__( self, parent )
		
		
		self.pen = wx.Pen("green", 1, wx.SOLID)
		self.brush = wx.Brush('blue', wx.TRANSPARENT)  #透明填充
		
		#For Log Message
		self.LogTarget = wx.LogWindow(self,'LogFrame',True,False)
		wx.Log.SetActiveTarget(self.LogTarget)
		
		#paint object list
		drawPaper = JHRect()
		self.paintObjList = []
		self.paintObjList.append(drawPaper)
		
		#drag flag
		self.startDraggingObject = False
		
		#file info
		self.fileName = None
		self.isHotKeySavingFile = False


	def onSelectMenuItemHelpShowLog( self, event ):
		self.LogTarget.Show()
		
	def onMainPanelChar( self, event ):
		wx.LogMessage('onChar')
	
	def onMainPanelKeyDown( self, event ):
		if not self.isHotKeySavingFile:
			if event.ControlDown() and event.GetKeyCode() == 83:#CTRL+S
				self.isHotKeySavingFile = True
				self.onSelectMenuItemFileSave(wx.MouseEvent())
	
	def onMainPanelKeyUp( self, event ):
		if self.isHotKeySavingFile:
			if event.GetKeyCode() == 83 or event.GetKeyCode() == wx.WXK_CONTROL:
				self.isHotKeySavingFile = False
		
	def onSelectMenuItemFileNew( self, event ):
		self.paintObjList.clear()
		self.paintObjList.append(JHRect())
		self.__Draw()
		self.fileName = None
	
	def onSelectMenuItemFileOpen( self, event ):
		fileDialog = wx.FileDialog(self,pos=wx.Point(100,100))
		if wx.ID_OK == fileDialog.ShowModal():
			self.fileName = fileDialog.GetPath()
			try:
				fileHandle = open(self.fileName,'rb')
				openList = pickle.load(fileHandle)
				self.paintObjList.clear()
				self.paintObjList.extend(openList)
				fileHandle.close()
				self.__Draw()
			except Exception as e:
				wx.LogMessage(type(e))
				wx.LogMessage('open file err')
	
	def onSelectMenuItemFileSave( self, event ):
		if self.fileName != None:
			self.__saveFile()
		else:
			fileDialog = wx.FileDialog(self,pos=wx.Point(100,100),style=wx.FD_SAVE)
			if wx.ID_OK == fileDialog.ShowModal():
				self.fileName = fileDialog.GetPath()+'.jhd'
				self.__saveFile()
	
	def __saveFile(self):
		try:
			fileHandle = open(self.fileName,'wb')
			#FIXME:pickle can pick wx.GraphicsPath, so I remove them then add them 
			for obj in self.paintObjList:
				obj.PerpareSave()
			pickle.dump(self.paintObjList,fileHandle)
			fileHandle.close()
			self.__Draw()
		except Exception as err:
			wx.LogMessage('save file err')
		
	def onMainPanelPaint( self, event ):
		wx.LogMessage('MainPabel onPaint')
		self.__Draw()
		
	def onMainPanelLeftDown( self, event ):
		self.startDraggingObject = True
	
	def onMainPanelLeftUp( self, event ):
		self.startDraggingObject = False
	
	def onMainPanelMotion( self, event ):
		position = event.GetPosition()
		if not self.startDraggingObject:
			self.__Focus(position)
		else:
			self.__Dragging(position)
		
	def onButtonLineClick( self, event ):
		wx.LogMessage('draw Line')
		self.paintObjList.append(JHLine(10,10,200,200))
		self.paintObjList.append(JHLine(40,80,300,300))
		self.__Draw()
		
	def __Dragging(self,position):
		for obj in self.paintObjList:
			if obj.isFocus:
				obj.Dragging(position)
				break
		self.__Draw()
		
	def __Focus(self,position):
		needReDraw = False
		for obj in self.paintObjList:
			if JHFocusState.FOCUS_NONE != obj.Focus(position):
				needReDraw = True
		if needReDraw:
			self.__Draw()
				
	def __Draw( self ):
		size = self.GetClientSize()
		self.bitmap = wx.Bitmap(size.width, size.height)
		dc = wx.BufferedDC(wx.ClientDC(self.m_panel_main), self.bitmap)
		gc = wx.GraphicsContext.Create(dc)
		if gc:
			paperSize = dc.GetSize()
			self.paintObjList[0].ReSize(paperSize)
			for obj in self.paintObjList:
				obj.Draw(gc)
		else:
			wx.LogMessage('__Draw gc create failed')
