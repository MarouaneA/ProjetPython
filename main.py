__author__ = 'veronhu'


import sys

from PyQt5 import QtWidgets
import load_file
import visu
import inspector
import configuration



#initialises Qt
app = QtWidgets.QApplication([])
win = QtWidgets.QMainWindow()
win.setWindowTitle("TIMELINE")
win.setCentralWidget(QtWidgets.QWidget())

#permet de choisir le fichier de travail à ouvrir
"""fname = QFileDialog.getOpenFileName(win.centralWidget(), 'Open file','SamplesLog/')
if fname[0]:
    MUSIC_FILE = fname[0]"""

MUSIC_FILE = 'SamplesLog/essai_donnees_2.txt'


#variable globale
list_point = load_file.load_actions(MUSIC_FILE)[0]

#créer le color_form par le biais de l'inspecteur
the_inspector_dock = QtWidgets.QDockWidget()
the_inspector_window = inspector.Inspector(MUSIC_FILE)
the_inspector_dock.setWidget(the_inspector_window)

#récupère le dictionnaire qui renseigne les couleurs et fes formes des points pour créer la vue(variable temporaire)
color_form = the_inspector_window.selec_un


#récupère le dictionnaire qui détermine l'état (selec ou not selec) des points pour créer la vue(variable temporaire)
config_mainWindow = configuration.Config(MUSIC_FILE)

MainWindow = QtWidgets.QMainWindow()
# met en place le widget créé avec Qt Designer et pyuic
config_mainWindow.setupUi(MainWindow)

#récupère les listes des checkbox pour créer la vue(varialbe temporaire)
dict_state_chekbx = config_mainWindow.selec
dict_state_joinchkbx1 = config_mainWindow.selec_join
dict_state_joinchkbx2 = config_mainWindow.selec_join2

#créé la vue
view = visu.View(list_point, color_form, dict_state_chekbx, dict_state_joinchkbx1, dict_state_joinchkbx2)


config_mainWindow.setView(view)
the_inspector_window.setView(view)



# met en place fenetre principale
win.setCentralWidget(view)

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
