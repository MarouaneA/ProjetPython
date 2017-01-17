__author__ = 'veronhu'


import sys

from PyQt5 import QtWidgets, QtCore
import lect_fichier
import visu
import inspector
import color_form
import configuration
from PyQt5.QtWidgets import QFileDialog

app = QtWidgets.QApplication([])
win = QtWidgets.QMainWindow()
win.setWindowTitle("TIMELINE")
win.setCentralWidget(QtWidgets.QWidget())

fname = QFileDialog.getOpenFileName(win.centralWidget(), 'Open file', '/home')
if fname[0]:
    MUSIC_FILE = fname[0].split('/')[-1]

act= lect_fichier.load_actions(MUSIC_FILE)[0]

# Initialize Qt
the_inspector_dock = QtWidgets.QDockWidget()
the_inspector_window = inspector.Inspector(MUSIC_FILE)
the_inspector_dock.setWidget(the_inspector_window)


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
View = visu.View(act,color_forme,selec,selec_join,selec_join2)

ui2.setView(View)
the_inspector_window.setView(View)

# create configuration

MainWindow.show()
# FenetreG.show()
# create the QMainWindow and add both widgets

win.setCentralWidget(View)
win.addDockWidget(1, the_inspector_dock)
#win.addDockWidget(QtCore.Qt.DockWidgetArea(1), the_inspector_dock)
win.adjustSize()
win.show()
# ui2.list_chkbx[1].keyPressEvent(print(25))
# enter the main loop
result = app.exec_()

# shut down nicely if main loop has exited, passing the 'result' i.e. the status or error code
sys.exit(result)
