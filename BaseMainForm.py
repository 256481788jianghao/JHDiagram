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
		self.m_menu_file = wx.Menu()
		self.m_menuItem_file_new = wx.MenuItem( self.m_menu_file, wx.ID_ANY, u"New", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_file.Append( self.m_menuItem_file_new )
		
		self.m_menu_file.AppendSeparator()
		
		self.m_menuItem_file_open = wx.MenuItem( self.m_menu_file, wx.ID_ANY, u"Open", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_file.Append( self.m_menuItem_file_open )
		
		self.m_menu_file.AppendSeparator()
		
		self.m_menuItem_file_save = wx.MenuItem( self.m_menu_file, wx.ID_ANY, u"Save", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_file.Append( self.m_menuItem_file_save )
		
		self.m_menu_file.AppendSeparator()
		
		self.m_menuItem_file_saveImg = wx.MenuItem( self.m_menu_file, wx.ID_ANY, u"SaveImage", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_file.Append( self.m_menuItem_file_saveImg )
		
		self.m_menubar_mainform.Append( self.m_menu_file, u"File" ) 
		
		self.m_menu_help = wx.Menu()
		self.m_menuItem_help_show_log = wx.MenuItem( self.m_menu_help, wx.ID_ANY, u"Show Log", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_help.Append( self.m_menuItem_help_show_log )
		
		self.m_menubar_mainform.Append( self.m_menu_help, u"help" ) 
		
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
		gSizer_toolbox = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_button_Line = wx.Button( self.m_scrolledWindow_box_list, wx.ID_ANY, u"Line", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer_toolbox.Add( self.m_button_Line, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_button2 = wx.Button( self.m_scrolledWindow_box_list, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer_toolbox.Add( self.m_button2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		self.m_scrolledWindow_box_list.SetSizer( gSizer_toolbox )
		self.m_scrolledWindow_box_list.Layout()
		gSizer_toolbox.Fit( self.m_scrolledWindow_box_list )
		self.m_choicebook_box.AddPage( self.m_scrolledWindow_box_list, u"base", False )
		bSizer_b1_2.Add( self.m_choicebook_box, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer_b0.Add( bSizer_b1_2, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer_b0 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_MENU, self.onSelectMenuItemFileNew, id = self.m_menuItem_file_new.GetId() )
		self.Bind( wx.EVT_MENU, self.onSelectMenuItemFileOpen, id = self.m_menuItem_file_open.GetId() )
		self.Bind( wx.EVT_MENU, self.onSelectMenuItemFileSave, id = self.m_menuItem_file_save.GetId() )
		self.Bind( wx.EVT_MENU, self.onSelectMenuItemHelpShowLog, id = self.m_menuItem_help_show_log.GetId() )
		self.m_panel_main.Bind( wx.EVT_LEFT_DOWN, self.onMainPanelLeftDown )
		self.m_panel_main.Bind( wx.EVT_LEFT_UP, self.onMainPanelLeftUp )
		self.m_panel_main.Bind( wx.EVT_MOTION, self.onMainPanelMotion )
		self.m_panel_main.Bind( wx.EVT_PAINT, self.onMainPanelPaint )
		self.m_button_Line.Bind( wx.EVT_BUTTON, self.onButtonLineClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onSelectMenuItemFileNew( self, event ):
		event.Skip()
	
	def onSelectMenuItemFileOpen( self, event ):
		event.Skip()
	
	def onSelectMenuItemFileSave( self, event ):
		event.Skip()
	
	def onSelectMenuItemHelpShowLog( self, event ):
		event.Skip()
	
	def onMainPanelLeftDown( self, event ):
		event.Skip()
	
	def onMainPanelLeftUp( self, event ):
		event.Skip()
	
	def onMainPanelMotion( self, event ):
		event.Skip()
	
	def onMainPanelPaint( self, event ):
		event.Skip()
	
	def onButtonLineClick( self, event ):
		event.Skip()
	

