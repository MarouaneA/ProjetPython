import math



from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QWheelEvent


class View(QtWidgets.QWidget):

    def __init__(self, act,color_form,selec,selec_join,selec_join2):
        super(View, self).__init__()
        self.setWindowTitle('Timeline')
        self.action = act
        self.color_form = color_form
        self.selec= selec
        self.selec_join = selec_join
        self.selec_join2 = selec_join2
        self.grview = None
        self.scene = None
        self.entry = None
        self.build_interface()
        self.draw_timeline()
        self.dep_time = act[0].time
        self.valeur = 0
        self.premier=0
        self.inter = self.action[-1].time-self.action[0].time

class Timeline_item(QtWidgets.QVBoxLayout):
    def __init__(self,name,points):
        self.label = QtWidgets.QLabel(name)
        self.list_points = points


    def create_one_timeline(self):
        self.horizontalLayoutWidget = QtWidgets.QWidget()
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.addWidget(self.label)

        for point in self.list_points:
            xys = ((point.time - t_0) / inter), y



def xy_coords(xy, width):
    dw = width / 3
    return QtCore.QRectF(xy[0] - dw, xy[1] - dw / 3, width / 3, width / 3)

def xy_line(xy, inter):
    return QtCore.QRectF(-50, xy[1], (inter * 8) + 50, 1)