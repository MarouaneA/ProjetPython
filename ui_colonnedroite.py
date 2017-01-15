# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'collonnedroite.ui'
#
# Created: Wed Dec 21 17:43:15 2016
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow3(object):
    def setupUi(self, MainWindow3):
        MainWindow3.setObjectName("MainWindow3")
        MainWindow3.resize(313, 857)
        self.verticalLayout = QtWidgets.QVBoxLayout(MainWindow3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(MainWindow3)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame_2")
        self.verticalLayout2 = QtWidgets.QHBoxLayout(self.frame)
        self.verticalLayout2.setContentsMargins(8, 8, 8, 5)
        self.verticalLayout2.setObjectName("horizontalLayout")
        self.comboBox_type = QtWidgets.QComboBox(self.frame)
        self.comboBox_type.setObjectName("comboBox_type")
        self.verticalLayout2.addWidget(self.comboBox_type)
        self.comboBox_type2 = QtWidgets.QComboBox(self.frame)
        self.comboBox_type2.setObjectName("comboBox_type")
        self.verticalLayout2.addWidget(self.comboBox_type2)
        self.comboBox_type3 = QtWidgets.QComboBox(self.frame)
        self.comboBox_type3.setObjectName("comboBox_type")
        self.verticalLayout2.addWidget(self.comboBox_type3)
        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(MainWindow3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow3)
    def retranslateUi(self, MainWindow3):
        _translate = QtCore.QCoreApplication.translate
        MainWindow3.setWindowTitle(_translate("Mainwindow3", "Mainwindow3"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow3 = QtWidgets.QWidget()
    ui = Ui_MainWindow3()
    ui.setupUi(MainWindow3)
    MainWindow3.show()
    sys.exit(app.exec_())

