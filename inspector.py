__author__ = 'veronhu'
"""
    Class displaying flight information
    wraps a widget designed with Qt Designer
    Version integrated in the airport simulator
"""
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QListWidgetItem
from color_form import Ui_MainWindow

class Inspector(QWidget):
    """ Widget  affichant les actions et permettant de choisir la couleur et la forme """

    def __init__(self,fichier):
        super(Inspector, self).__init__()
        #permet de récupérer les couleurs et les formes dans main
        self.selec_un=0

        #crée le widget
        self.ui_Inspector = Ui_MainWindow(fichier)

        #récupère les couleurs et les formes de color_form
        self.selec_un = self.ui_Inspector.selec_un

        #permet de modifier directement le window principal lorsqu'on change la couleur ou la forme dans une combobox
        self.list_comboBox_form = self.ui_Inspector.list_comboBox_form
        self.list_comboBox_colour = self.ui_Inspector.list_comboBox_colour
        # met en place le widget créé avec Qt Designer et pyuic
        self.ui_Inspector.setupUi(self)
        self.show()
        for k in range (len(self.list_comboBox_colour)):
            self.list_comboBox_colour[k].currentTextChanged.connect(lambda : self.view.draw_timeline())
            self.list_comboBox_form[k].currentTextChanged.connect(lambda : self.view.draw_timeline())



    #récupère la vue créer dans main pour pouvoir actualiser le window principal avec les combo box
    def setView(self, view):
        self.view=view


