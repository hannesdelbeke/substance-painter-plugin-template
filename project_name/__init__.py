import os
import substance_painter.ui
from PySide2 import QtWidgets, QtCore, QtGui


substance_ui_elements = []
widget = None


# hello world widget
class HelloWorld(QtWidgets.QWidget):
    def __init__(self, parent, *args, **kwargs):
        super(HelloWorld, self).__init__(parent, *args, **kwargs)
        # set title
        self.setWindowTitle("Hello World")
        # self.setWindowIcon(QtGui.QIcon(":/SP_ICON_16x16"))  # TODO this does not work
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.Window)
        self.setLayout(QtWidgets.QVBoxLayout())
        self.layout().addWidget(QtWidgets.QLabel("Hello World!"))


def show_widget():
    global widget
    parent = substance_painter.ui.get_main_window()
    print(parent)
    widget = HelloWorld(parent=parent)
    dock_widget = substance_painter.ui.add_dock_widget(widget)
    dock_widget.show()


def start_plugin():
    # Create a text widget for a menu
    Action = QtWidgets.QAction("Hello", triggered=show_widget)
    # Add this widget to the existing Window menu of the application
    substance_painter.ui.add_action(substance_painter.ui.ApplicationMenu.Window, Action)
    # Store the widget for proper cleanup later when stopping the plugin
    substance_ui_elements.append(Action)


def close_plugin():
    # Remove all widgets that have been added to the UI
    for widget in substance_ui_elements:
        substance_painter.ui.delete_ui_element(widget)
    substance_ui_elements.clear()


if __name__ == "__main__":
    start_plugin()
