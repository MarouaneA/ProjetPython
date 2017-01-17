__author__ = 'veronhu'
"""
    Class displaying flight information
    wraps a widget designed with Qt Designer
    Version integrated in the airport simulator
"""
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QListWidgetItem
from ui_colonnedroite import Ui_MainWindow3
from color_form import Ui_MainWindow

class Inspector(QWidget):
    """ Widget displaying information about a Flight """

    def __init__(self,fichier):
        super(Inspector, self).__init__()


        self.selec_un=0
        # sets up instance variables
        self.ui_Inspector = Ui_MainWindow(fichier)
        self.selec_un = self.ui_Inspector.selec_un
        self.list_comboBox_form = self.ui_Inspector.list_comboBox_form
        self.list_comboBox_colour = self.ui_Inspector.list_comboBox_colour
        # sets up the widget created with Qt Designer and pyuic
        self.ui_Inspector.setupUi(self)
        self.show()
        for k in range (len(self.list_comboBox_colour)):
            self.list_comboBox_colour[k].currentTextChanged.connect(lambda : self.view.draw_timeline())
            self.list_comboBox_form[k].currentTextChanged.connect(lambda : self.view.draw_timeline())
    def setView1(self, view):
        self.view=view




class Inspector3(QWidget):
    """ Widget displaying information about a Flight """

    def __init__(self):
        super(Inspector3, self).__init__()

        # sets up instance variables

        self.ui_Inspector = Ui_MainWindow3()

        # sets up the widget created with Qt Designer and pyuic
        self.ui_Inspector.setupUi(self)

        self.show()
