from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import lect_fichier
import configuration


class Ui_MainWindow2(object):

    def __init__(self, act):
        self.action = act
        self.list_chkbx = []   # liste des Checkbox créées qui contiennent les différentes actions
        self.list_action = list_action(self.action)  # liste des actions sous forme de str

    def setupUi(self, MainWindow2):
        MainWindow2.setObjectName("MainWindow2")
        MainWindow2.resize(703, 686)
        self.centralwidget = QtWidgets.QWidget(MainWindow2)
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
            chkbx.stateChanged.connect(lambda state=0,chkbx=chkbx : self.dict_evnt(state,chkbx))
            self.list_chkbx.append(chkbx)
            self.verticalLayout.addWidget(chkbx)


        MainWindow2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 703, 25))
        self.menubar.setObjectName("menubar")
        MainWindow2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow2)
        self.statusbar.setObjectName("statusbar")
        MainWindow2.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow2)

    def retranslateUi(self, MainWindow2):
        _translate = QtCore.QCoreApplication.translate
        MainWindow2.setWindowTitle(_translate("MainWindow2", "Select Configuration"))
        for k in range(len(self.list_action)):
            self.list_chkbx[k].setText(_translate("MainWindow2", self.list_action[k]))

    def affichage(self, state, evnt):
        #print(state)
        if state == 0 :
            print(evnt.text()+" is deselected")
        else :
            # state = 2
            print(evnt.text()+" is selected")

    def dict_evnt(self, state, evnt):
        dict = {}
        if state == 0 :
            dict[evnt.text()] = "deselected"
        else :
            dict[evnt.text()] = "selected"
        print(dict)



def list_action(act):
    L = []
    for point in act:
        if point.action not in L :
            L.append(point.action)
    return(L)

#['STARTLOG', 'ASSIGNMENT_STARTED', 'NEW_PROJECT_STARTED', 'INPUT_GROUP_UPDATE', 'OUTPUT_GROUP_UPDATE', 'SUPERVISED_LEARNING_START', 'MODEL_BUILDER_UPDATED', 'SUPERVISED_DELETE_ALL_EXAMPLES', 'SUPERVISED_RECORD_START', 'TRAIN_START', 'TRAIN_FINISHED', 'MODEL_NUM=0', 'SUPERVISED_RECORD_STOP', 'START_RUN', 'RUN_STOP', 'DELETE_LAST_ROUND', 'PATH_EDITED', 'MODEL_EDITED_OLD', 'MODEL_EDITED_NEW', 'MODEL_TO_CONSOLE', 'STOPLOG']


if __name__ == "__main__":
    act = lect_fichier.load_actions("essai_donnees.txt")
    app = QtWidgets.QApplication(sys.argv)
    MainWindow2 = QtWidgets.QMainWindow()
    ui = Ui_MainWindow2(act)
    ui.setupUi(MainWindow2)
    MainWindow2.show()
    sys.exit(app.exec_())

