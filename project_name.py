import os 
import substance_painter.ui 
from PySide2 import QtWidgets 
 
 
plugin_widgets = [] 
 
 
def hello() : 
 print("hello)
 
 
def start_plugin(): 
 # Create a text widget for a menu 
 Action = QtWidgets.QAction("Hello", triggered=hello) 
 # Add this widget to the existing File menu of the application 
 substance_painter.ui.add_action(substance_painter.ui.ApplicationMenu.File, Action ) 
 # Store the widget for proper cleanup later when stopping the plugin 
 plugin_widgets.append(Action) 
 
 
def close_plugin(): 
 # Remove all widgets that have been added to the UI 
 for widget in plugin_widgets: 
  substance_painter.ui.delete_ui_element(widget) 
 plugin_widgets.clear() 
 
 
if __name__ == "__main__": 
 start_plugin()