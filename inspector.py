__author__ = 'veronhu'
"""
    Class displaying flight information
    wraps a widget designed with Qt Designer
    Version integrated in the airport simulator
"""
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QListWidgetItem


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

