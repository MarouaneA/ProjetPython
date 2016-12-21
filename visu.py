__author__ = 'aatefma'
import math
import lect_fichier
import configuration


from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QWheelEvent


COLORS = ['red', 'orange', 'blue', 'green', 'magenta', 'cyan', 'lime', 'purple', 'silver', 'indigo', 'maroon',
          'olive', 'navy', 'goldenrod', 'teal', 'darkorange' 'crimson', 'seagreen', 'steelblue', 'lightcoral',
          'grey', 'black', 'orangered']

n = len(COLORS)

class View(QtWidgets.QWidget):

    def __init__(self, act):
        super(View, self).__init__()
        self.setWindowTitle('Timeline')
        self.act = act
        self.sel = self.select()
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
        add_button ("split view", lambda: self.draw_timeline())
        label_4 = QtWidgets.QLabel()
        label_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        label_4.setObjectName("label_4")

    def draw_timeline(self):
        self.scene.clear()
        timeline_group = QtWidgets.QGraphicsItemGroup()
        self.scene.addItem(timeline_group)
        timeline_group.setZValue(0)
        pen = QtGui.QPen(QtCore.Qt.transparent)
        line_pen = QtGui.QPen(QtGui.QColor("black"))
        width = 30
        i = 720
        t_0 = self.act[0].time
        t_f = self.act[-1].time
        inter= (t_f - t_0)/2000
        dict = {}
        for point in self.act:
            if self.sel[point.action]== 'Y':
                if point.action not in dict:
                    dict[point.action] = i
                    brush = QtGui.QBrush(QtGui.QColor(COLORS[i % n]))
                    xys = ((point.time - t_0) / inter), dict[point.action]
                    item = QtWidgets.QGraphicsRectItem(xy_coords(xys, width), timeline_group)
                    i -= 60
                else:
                    brush = QtGui.QBrush(QtGui.QColor(COLORS[dict[point.action] % n]))
                    xys = ((point.time - t_0) / inter), dict[point.action]
                    item = QtWidgets.QGraphicsRectItem(xy_coords(xys, width), timeline_group)
                item.setPen(pen)
                item.setBrush(brush)
                item.setToolTip(point.action+' '+ point.arg)

    def select(self):
        sel = {}
        for point in self.act:
            if point.action not in sel:
                sel[point.action] = input(point.action +'?'+ 'Y = Yes'+ ' '+'N = No'+' ')
        return(sel)








def xy_coords(xy, width):
    dw = width / 2.
    return QtCore.QRectF(xy[0] - dw, xy[1] - dw, width/15, width)