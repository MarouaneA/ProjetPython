__author__ = 'veronhu'


import sys

from PyQt5 import QtWidgets, QtCore
from Qt1 import Ui_Form
import lect_fichier
import inspector
import visu
import inspector
import configuration


MUSIC_FILE='essai_donnees_2.txt'
act= lect_fichier.load_actions(MUSIC_FILE)

# Initialize Qt
app = QtWidgets.QApplication([])

# create the radar view and the time navigation interface
View = visu.View(act)

# create the inspector
the_inspector_window = inspector.Inspector(View,act)
# create a QDockWidget for the inspector
the_inspector_dock = QtWidgets.QDockWidget()
the_inspector_dock.setWidget(the_inspector_window)
# create the QMainWindow and add both widgets
win = QtWidgets.QMainWindow()
win.setWindowTitle("TIMELINE")
win.setCentralWidget(View)
win.addDockWidget(QtCore.Qt.DockWidgetArea(1), the_inspector_dock)
win.resize(1200, 600)
win.show()

# enter the main loop
result = app.exec_()
# shut down nicely if main loop has exited, passing the 'result' i.e. the status or error code
sys.exit(result)
