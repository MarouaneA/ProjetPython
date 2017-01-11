from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import lect_fichier

FICHIER = "essai_donnees.txt"

class Ui_MainWindow(object):

    def __init__(self, fichier):
        #self.action = lect_fichierbiss.load_actions(fichier)[0]
        self.list_chkbx = []   # liste des Checkbox créées qui contiennent les différentes actions
        self.list_action = lect_fichier.load_actions(fichier)[1]  # liste des actions differentes sous forme de str
        self.selec=initialisation(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(703, 686)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(150, 50, 581, 481))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        for evnt in self.list_action:
            chkbx = QtWidgets.QCheckBox(self.verticalLayoutWidget)
            chkbx.setObjectName(evnt)
            chkbx.toggle()  # initialise l'état de la Checkbox à 'sélectionnée'
            # state (1er argument) : argument obligatoire de la méthode stateChanged + nécessité de mettre chkbx=chkbx
            # sinon la fonction n'évalue que le dernier de la boucle 'for' ( il faut définir des variables indépendantes)
            chkbx.stateChanged.connect(lambda state=0, chkbx=chkbx : dict_evnt(self,state,chkbx))
            self.list_chkbx.append(chkbx)
            self.verticalLayout.addWidget(chkbx)


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 703, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Select Configuration"))
        for k in range(len(self.list_action)):
            self.list_chkbx[k].setText(_translate("MainWindow", self.list_action[k]))



def initialisation(Ui_MainWindow):
    selec={}
    for point in Ui_MainWindow.list_action:
        selec[point]="selected"
    return selec

def dict_evnt(ui, state, evnt):
    if state == 0 :
        #print(evnt.text() + " is deselected")
        ui.selec[evnt.text()] = "deselected"
    else :
        #print(evnt.text() + " is selected")
        ui.selec[evnt.text()] = "selected"




if __name__ == "__main__":
    fichier = FICHIER
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui2 = Ui_MainWindow(fichier)
    ui2.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

