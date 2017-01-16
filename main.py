__author__ = 'veronhu'


import sys

from PyQt5 import QtWidgets, QtCore
import lect_fichier
import visu1
import inspector1
import color_form
import configuration


MUSIC_FILE='essai_donnees_2.txt'
act= lect_fichier.load_actions(MUSIC_FILE)[0]

# Initialize Qt
app = QtWidgets.QApplication([])
the_inspector_dock = QtWidgets.QDockWidget()
the_inspector_window = inspector1.Inspector(MUSIC_FILE)
the_inspector_dock.setWidget(the_inspector_window)
print(1)

# create the radar view and the time navigation interface
# ui=color_form.Ui_MainWindow(MUSIC_FILE)
# FenetreG=QtWidgets.QMainWindow()
# ui.setupUi(FenetreG)
color_forme = the_inspector_window.selec_un
ui2 = configuration.Ui_MainWindow(MUSIC_FILE)
MainWindow = QtWidgets.QMainWindow()

ui2.setupUi(MainWindow)
selec = ui2.selec
selec_join = ui2.selec_join
selec_join2 = ui2.selec_join2
View = visu1.View(act,color_forme,selec,selec_join,selec_join2)


# create configuration

MainWindow.show()
# FenetreG.show()
# create the QMainWindow and add both widgets
win = QtWidgets.QMainWindow()
win.setWindowTitle("TIMELINE")
win.setCentralWidget(View)
the_inspector_dock3 = QtWidgets.QDockWidget()
the_inspector_window3 = inspector1.Inspector3()
the_inspector_dock3.setWidget(the_inspector_window3)
win.addDockWidget(2, the_inspector_dock3)
win.addDockWidget(1, the_inspector_dock)
#win.addDockWidget(QtCore.Qt.DockWidgetArea(1), the_inspector_dock)
win.adjustSize()
win.show()
# ui2.list_chkbx[1].keyPressEvent(print(25))
# enter the main loop
result = app.exec_()

# shut down nicely if main loop has exited, passing the 'result' i.e. the status or error code
sys.exit(result)
