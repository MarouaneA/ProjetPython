__author__ = 'veronhu'


import sys

from PyQt5 import QtWidgets, QtCore
import lect_fichier
import visu
import inspector
import zero
import configuration


MUSIC_FILE='essai_donnees_2.txt'
act= lect_fichier.load_actions(MUSIC_FILE)

# Initialize Qt
app = QtWidgets.QApplication([])

# create the radar view and the time navigation interface
ui=zero.Ui_FenetreG(act)
FenetreG=QtWidgets.QMainWindow()
ui.setupUi(FenetreG)
ui2 = configuration.Ui_MainWindow(act)
MainWindow = QtWidgets.QMainWindow()
ui2.setupUi(MainWindow)
selec = ui2.selec
View = visu.View(act,ui,selec)


# create configuration

MainWindow.show()
FenetreG.show()
# create the QMainWindow and add both widgets
win = QtWidgets.QMainWindow()
win.setWindowTitle("TIMELINE")
win.setCentralWidget(View)
#win.addDockWidget(QtCore.Qt.DockWidgetArea(1), the_inspector_dock)
win.resize(1280, 720)
win.show()

# enter the main loop
result = app.exec_()

# shut down nicely if main loop has exited, passing the 'result' i.e. the status or error code
sys.exit(result)
