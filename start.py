import wx
from MainForm import MainForm

App = wx.App()

#Main Frame.
MainForm = MainForm(None)

# Show it.
MainForm.Show()

# Start the event loop.
App.MainLoop()
