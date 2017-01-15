__author__ = 'veronhu'
"""
    Class displaying flight information
    wraps a widget designed with Qt Designer
    Version integrated in the airport simulator
"""
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QListWidgetItem
from ui_colonnedroite import Ui_MainWindow3

class Inspector(QWidget):
    """ Widget displaying information about a Flight """

    def __init__(self,View,act):
        super(Inspector, self).__init__()

        # sets up instance variables
        self.view = View
        self.action = act
        self.ui_Inspector = zero.Ui_FenetreG(act)

        # sets up the widget created with Qt Designer and pyuic
        self.ui_Inspector.setupUi(self)
        self.show()
class Inspector3(QWidget):
    """ Widget displaying information about a Flight """

    def __init__(self):
        super(Inspector3, self).__init__()

        # sets up instance variables

        self.ui_Inspector = Ui_MainWindow3()

        # sets up the widget created with Qt Designer and pyuic
        self.ui_Inspector.setupUi(self)

        # populates the 'filter by type' combobox



        self.show()
