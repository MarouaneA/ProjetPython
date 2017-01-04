__author__ = 'veronhu'
"""
    Class displaying flight information
    wraps a widget designed with Qt Designer
    Version integrated in the airport simulator
"""
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QListWidgetItem
import zero

class Inspector(QWidget):
    """ Widget displaying information about a Flight """

    def __init__(self,View,act,ui):
        super(Inspector, self).__init__()

        # sets up instance variables
        self.view = View
        self.action = act
        self.color = zero.colour(ui)
        self.ui_Inspector = zero.Ui_FenetreG(act)

        # sets up the widget created with Qt Designer and pyuic
        self.ui_Inspector.setupUi(self)
        self.show()

    """def color(self):
        k = 0
        for point in self.action:
            self.color[point.action] = self.list_cbbxC[k].currentText()
            k += 1

    def form(self):
        form = {}
        k = 0
        for point in self.action:
            if point.action not in form:
                form[point.action] = self.list_cbbxF[k].currentText()
                k += 1
        return (form)"""
