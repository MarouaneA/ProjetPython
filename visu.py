__author__ = 'aatefma'
import math



from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QWheelEvent
import zero
import configuration

COLORS = ['red', 'orange', 'blue', 'green', 'magenta', 'cyan', 'lime', 'purple', 'silver', 'indigo', 'maroon',
          'olive', 'navy', 'goldenrod', 'teal', 'darkorange' 'crimson', 'seagreen', 'steelblue', 'lightcoral',
          'grey', 'black', 'orangered']
FORME = ['R','E','C']
n = len(COLORS)

class View(QtWidgets.QWidget):

    def __init__(self, act):
        super(View, self).__init__()
        self.setWindowTitle('Timeline')
        self.action =act
        self.sel = self.select()


        FenetreG = QtWidgets.QMainWindow()
        ui = zero.Ui_FenetreG(act)
        ui.setupUi(FenetreG)
        self.color = zero.colour(ui)
        self.form = zero.form(ui)

        config = QtWidgets.QMainWindow()
        ui2 = configuration.Ui_MainWindow(act)
        ui2.setupUi(config)
        self.selec=ui2.selec

        self.grview = None
        self.scene = None
        self.entry = None
        self.build_interface()
        self.draw_timeline()
        self.dep_time = act[0].time


    @QtCore.pyqtSlot(int)
    def zoom_view(self, value):
        self.grview.scale(value, 1)

    @QtCore.pyqtSlot(QWheelEvent)
    def zoom_view_mouse(self, event):
        self.grview.setTransformationAnchor(self.grview.AnchorUnderMouse)
        factor = math.pow(1.001, event.angleDelta().y())
        self.grview.scale(factor, 1)


    def zoom_time(self,value):
        self.draw_timeline(self,value)



    def build_interface(self):
        vbox = QtWidgets.QVBoxLayout(self)
        self.grview = QtWidgets.QGraphicsView()
        self.scene = QtWidgets.QGraphicsScene()
        self.grview.setScene(self.scene)
        self.grview.setDragMode(QtWidgets.QGraphicsView.ScrollHandDrag)
        self.grview.setRenderHint(QtGui.QPainter.Antialiasing)
        self.grview.wheelEvent = lambda event: self.zoom_view_mouse(event)
        self.grview.scale(1, -1)
        vbox.addWidget(self.grview)
        self.draw_timeline()
        self.grview.fitInView(self.grview.sceneRect(), QtCore.Qt.KeepAspectRatio)
        def add_button(text, slot):
            """adds a button to the hbox and connects the slot"""
            button = QtWidgets.QPushButton(text)
            button.clicked.connect(slot)
            vbox.addWidget(button)
        add_button ("split view", change)
        label_4 = QtWidgets.QLabel()
        label_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        label_4.setObjectName("label_4")

    def draw_timeline(self):
        self.scene.clear()
        timeline_group = QtWidgets.QGraphicsItemGroup()
        self.scene.addItem(timeline_group)
        timeline_group.setZValue(0)
        pen = QtGui.QPen(QtCore.Qt.transparent)
        width = 30
        i = 0
        t_0 = self.action[0].time
        t_f = self.action[-1].time
        inter= (t_f - t_0)/2000
        dict={}
        for point in self.action:
            if self.selec[point.action] == 'selected':
                if point.action not in dict:
                    dict[point.action] = i
                    brush = QtGui.QBrush(QtGui.QColor(self.color[point.action]))
                    xys = ((point.time - t_0) / inter), 720 - 60 * dict[point.action]
                    item = QtWidgets.QGraphicsRectItem(xy_coords(xys, width), timeline_group)
                    i += 1
                else:
                    brush = QtGui.QBrush(QtGui.QColor(self.color[point.action]))
                    xys = ((point.time - t_0) / inter), 720 - 60 * dict[point.action]
                    item = QtWidgets.QGraphicsRectItem(xy_coords(xys, width), timeline_group)
                item = QtWidgets.QGraphicsRectItem(xy_coords(xys, width), timeline_group)
                item.setPen(pen)
                item.setBrush(brush)
                item.setToolTip(point.action+' '+ point.arg)


    """def select(self):
        sel = {}
        for point in self.action:
            if point.action not in sel:
                sel[point.action] = input(point.action +' ?'+ ' = Yes'+ ' '+'N = No'+' ')
        return(sel)"""

def change():


def xy_coords(xy, width):
    dw = width / 2.
    return QtCore.QRectF(xy[0] - dw, xy[1] - dw, width/15, width)