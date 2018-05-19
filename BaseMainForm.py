# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jan 23 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class BaseMainForm
###########################################################################

class BaseMainForm ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 577,391 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		self.m_menubar_mainform = wx.MenuBar( 0 )
		self.SetMenuBar( self.m_menubar_mainform )
		
		self.m_toolBar_mainform = self.CreateToolBar( wx.TB_HORIZONTAL, wx.ID_ANY ) 
		self.m_toolBar_mainform.Realize() 
		
		self.m_statusBar_mainform = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )
		bSizer_b0 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer_b1_1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer_b2_1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer_b3_1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_panel_main = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel_main.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		bSizer_b3_1.Add( self.m_panel_main, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_scrollBar_main_v = wx.ScrollBar( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SB_VERTICAL )
		bSizer_b3_1.Add( self.m_scrollBar_main_v, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer_b2_1.Add( bSizer_b3_1, 1, wx.EXPAND, 5 )
		
		self.m_scrollBar_main_h = wx.ScrollBar( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SB_HORIZONTAL )
		bSizer_b2_1.Add( self.m_scrollBar_main_h, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer_b1_1.Add( bSizer_b2_1, 1, wx.EXPAND, 5 )
		
		
		bSizer_b0.Add( bSizer_b1_1, 4, wx.EXPAND, 5 )
		
		bSizer_b1_2 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_choicebook_box = wx.Choicebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.CHB_DEFAULT )
		self.m_scrolledWindow_box_list = wx.ScrolledWindow( self.m_choicebook_box, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow_box_list.SetScrollRate( 5, 5 )
		self.m_choicebook_box.AddPage( self.m_scrolledWindow_box_list, u"base", False )
		bSizer_b1_2.Add( self.m_choicebook_box, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer_b0.Add( bSizer_b1_2, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer_b0 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

