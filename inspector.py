__author__ = 'veronhu'
"""
    Class displaying flight information
    wraps a widget designed with Qt Designer
    Version integrated in the airport simulator
"""
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QListWidgetItem

from Qt1 import Ui_Form


class Inspector(QWidget):
    """ Widget displaying information about a Flight """

    def __init__(self):
        super(Inspector, self).__init__()

        # sets up instance variables

        self.ui_Inspector = Ui_Form()

        # sets up the widget created with Qt Designer and pyuic
        self.ui_Inspector.setupUi(self)

        # populates the 'filter by type' combobox



        self.show()



