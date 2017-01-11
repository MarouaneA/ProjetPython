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
        MainWindow.resize(500, 650)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 50, 400, 550))
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

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_save = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_save.setObjectName("Save Configuration")
        self.pushButton_save.clicked.connect(lambda : self.save())
        self.horizontalLayout.addWidget(self.pushButton_save)
        self.pushButton_load = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_load.setObjectName("Load Configuration")
        self.pushButton_load.clicked.connect(lambda : self.load())
        self.horizontalLayout.addWidget(self.pushButton_load)
        self.verticalLayout.addWidget(self.horizontalLayoutWidget)


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
        self.pushButton_save.setText(_translate("MainWindow", "Save Configuration"))
        self.pushButton_load.setText(_translate("MainWindow", "Load Configuration"))

    def save(self):
        nom_fichier = input('Nom de la configuration que vous voulez sauvergarder ?')
        fic = open(str(nom_fichier), 'w')
        for evnt in self.list_action:
            fic.write(str(evnt)+'    '+self.selec[evnt]+'\n')
        return ()

    def load(self):
        nom_fichier = input('Nom du fichier de la configuration que vous voulez charger ?')
        dic = {}
        k = 0
        with open(nom_fichier, 'r') as f:
            for line in f:
                list = line.split()
                dic[list[0]] = list[1]
                self.list_chkbx[k].toggle()
                if list[1] == 'selected':
                    self.list_chkbx[k].setChecked(True)
                else:
                    self.list_chkbx[k].setChecked(False)
                k += 1
        self.selec = dic
        return ()



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

