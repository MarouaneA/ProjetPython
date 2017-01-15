__author__ = 'veronhu'


import sys

from PyQt5 import QtWidgets, QtCore
import lect_fichier
import visu
import inspector
import color_form
import configuration


MUSIC_FILE='essai_donnees_2.txt'
act= lect_fichier.load_actions(MUSIC_FILE)[0]

# Initialize Qt
app = QtWidgets.QApplication([])

# create the radar view and the time navigation interface
ui=color_form.Ui_MainWindow(MUSIC_FILE)
FenetreG=QtWidgets.QMainWindow()
ui.setupUi(FenetreG)
color_forme = ui.selec_un
ui2 = configuration.Ui_MainWindow(MUSIC_FILE)
MainWindow = QtWidgets.QMainWindow()
ui2.setupUi(MainWindow)
selec = ui2.selec
selec_join = ui2.selec_join
selec_join2 = ui2.selec_join2
View = visu.View(act,color_forme,selec,selec_join,selec_join2)


# create configuration

MainWindow.show()
FenetreG.show()
# create the QMainWindow and add both widgets
win = QtWidgets.QMainWindow()
win.setWindowTitle("TIMELINE")
win.setCentralWidget(View)
the_inspector_dock3 = QtWidgets.QDockWidget()
the_inspector_window3 = inspector.Inspector3()
the_inspector_dock3.setWidget(the_inspector_window3)
win.addDockWidget(2, the_inspector_dock3)
#win.addDockWidget(QtCore.Qt.DockWidgetArea(1), the_inspector_dock)
win.resize(1280, 720)
win.show()

# enter the main loop
result = app.exec_()

# shut down nicely if main loop has exited, passing the 'result' i.e. the status or error code
sys.exit(result)
