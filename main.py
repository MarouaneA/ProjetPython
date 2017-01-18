__author__ = 'veronhu'


import sys

from PyQt5 import QtWidgets, QtCore
import lect_fichier
import visu
import inspector
import color_form
import configuration
from PyQt5.QtWidgets import QFileDialog


#initialises Qt
app = QtWidgets.QApplication([])
win = QtWidgets.QMainWindow()
win.setWindowTitle("TIMELINE")
win.setCentralWidget(QtWidgets.QWidget())

#permet de choisir le fichier de travail à ouvrir
fname = QFileDialog.getOpenFileName(win.centralWidget(), 'Open file','SamplesLog/')
if fname[0]:
    MUSIC_FILE = fname[0]

#variable globale
# act= lect_fichier.load_actions(MUSIC_FILE)[0]

#créer le color_form par le biais de l'inspecteur
the_inspector_dock = QtWidgets.QDockWidget()
the_inspector_window = inspector.Inspector(MUSIC_FILE)
the_inspector_dock.setWidget(the_inspector_window)

#récupère la liste des couleurs et des formes pour créer la vue(variable globale)
# color_form = the_inspector_window.selec_un



config_mainWindow= configuration.Ui_MainWindow(MUSIC_FILE)
MainWindow = QtWidgets.QMainWindow()
# met en place le widget créé avec Qt Designer et pyuic
config_mainWindow.setupUi(MainWindow)

#récupère les listes des checkbox pour créer la vue(varialbe globale)
# dict_state_chekbx = config_mainWindow.selec
# dict_state_joinchkbx1 = config_mainWindow.selec_join
# dict_state_joinchkbx2 = config_mainWindow.selec_join2

#créé la vue
View = visu.View(lect_fichier.load_actions(MUSIC_FILE)[0],the_inspector_window.selec_un,config_mainWindow.selec,config_mainWindow.selec_join,config_mainWindow.selec_join2)


config_mainWindow.setView(View)
the_inspector_window.setView(View)



# met en place fenetre principale
win.setCentralWidget(View)

#ajoute color_form par le biais d'inspector à la fenetre principale
win.addDockWidget(1, the_inspector_dock)

#affiche la fenetre principale
win.resize(1920,1080)
win.show()

#affiche la fenetre configuration
MainWindow.show()

# enter the main loop
result = app.exec_()

# shut down nicely if main loop has exited, passing the 'result' i.e. the status or error code
sys.exit(result)
