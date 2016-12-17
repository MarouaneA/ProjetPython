__author__ = 'aatefma'
import math
import lect_fichier


from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QWheelEvent

RUN_COLOR = 'red'
STRATLOG_COLOR = 'blue'
ASSIGNMENT_COLOR = 'green'
SUPERVISED_RECORD_START_COLOR = 'black'
MODEL_NUM_COLOR = 'brown'
TRAIN_START_COLOR = 'orange'
TRAIN_STOP_COLOR = 'purple'


class View(QtWidgets.QWidget):

    def __init__(self, act):
        super(View, self).__init__()
        self.setWindowTitle('Timeline')
        self.action = act
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
        add_button("one view", lambda : self.draw_one_timeline())
        add_button ("split view", lambda: self.draw_timeline())
        label_4 = QtWidgets.QLabel()
        label_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        label_4.setObjectName("label_4")
    def draw_one_timeline(self):
        self.scene.clear()
        timeline_group = QtWidgets.QGraphicsItemGroup()
        self.scene.addItem(timeline_group)
        timeline_group.setZValue(0)
        pen = QtGui.QPen(QtCore.Qt.transparent)
        width = 50
        i = 0
        t_0 = self.action[0].time
        t_f = self.action[-1].time
        inter= (t_f - t_0)/3000
        for point in self.action:
            if point.action == 'START_RUN':
                brush = QtGui.QBrush(QtGui.QColor(RUN_COLOR))
                xys = ((point.time-t_0)/inter), 0
                item = QtWidgets.QGraphicsEllipseItem(xy_coords(xys, width), timeline_group)
            elif point.action == 'ASSIGNMENT_STARTED':
                brush = QtGui.QBrush(QtGui.QColor(ASSIGNMENT_COLOR))
                xys =(point.time-t_0)/inter, 0
                item = QtWidgets.QGraphicsEllipseItem(xy_coords(xys, width), timeline_group)
            elif point.action == 'SUPERVISED_RECORD_START':
                brush = QtGui.QBrush(QtGui.QColor(SUPERVISED_RECORD_START_COLOR))
                xys = (point.time-t_0)/inter,0
                item = QtWidgets.QGraphicsEllipseItem(xy_coords(xys, width), timeline_group)
            elif point.action == 'MODEL_NUM=0':
                brush = QtGui.QBrush(QtGui.QColor(MODEL_NUM_COLOR))
                xys = (point.time-t_0)/inter, 0
                item = QtWidgets.QGraphicsEllipseItem(xy_coords(xys, width), timeline_group)
            elif point.action == 'TRAIN_START':
                brush = QtGui.QBrush(QtGui.QColor(TRAIN_START_COLOR))
                xys = (point.time-t_0)/inter, 0
                item = QtWidgets.QGraphicsEllipseItem(xy_coords(xys, width), timeline_group)
            elif point.action == 'TRAIN_FINISHED':
                brush = QtGui.QBrush(QtGui.QColor(TRAIN_STOP_COLOR))
                xys = (point.time-t_0)/inter, 0
                item = QtWidgets.QGraphicsEllipseItem(xy_coords(xys, width), timeline_group)
            else:
                brush = QtGui.QBrush(QtGui.QColor('BLUE'))
                xys = (point.time-t_0)/inter, 0
                item = QtWidgets.QGraphicsEllipseItem(xy_coords(xys, width), timeline_group)
            i += 1
            item.setPen(pen)
            item.setBrush(brush)
            item.setToolTip(point.action+' '+ point.arg)


    def draw_timeline(self):
        self.scene.clear()
        timeline_group = QtWidgets.QGraphicsItemGroup()
        self.scene.addItem(timeline_group)
        timeline_group.setZValue(0)
        pen = QtGui.QPen(QtCore.Qt.transparent)
        width = 20
        i = 0
        t_0 = self.action[0].time
        t_f = self.action[-1].time
        inter= (t_f - t_0)/900
        for point in self.action:
            if point.action == 'START_RUN':
                brush = QtGui.QBrush(QtGui.QColor(RUN_COLOR))
                xys = ((point.time-t_0)/inter), 540
                item = QtWidgets.QGraphicsRectItem(xy_coords(xys, width), timeline_group)
            elif point.action == 'ASSIGNMENT_STARTED':
                brush = QtGui.QBrush(QtGui.QColor(ASSIGNMENT_COLOR))
                xys =(point.time-t_0)/inter, 720
                item = QtWidgets.QGraphicsRectItem(xy_coords(xys, width), timeline_group)
            elif point.action == 'SUPERVISED_RECORD_START':
                brush = QtGui.QBrush(QtGui.QColor(SUPERVISED_RECORD_START_COLOR))
                xys = (point.time-t_0)/inter, 360
                item = QtWidgets.QGraphicsRectItem(xy_coords(xys, width), timeline_group)
            elif point.action == 'MODEL_NUM=0':
                brush = QtGui.QBrush(QtGui.QColor(MODEL_NUM_COLOR))
                xys = (point.time-t_0)/inter, 180
                item = QtWidgets.QGraphicsRectItem(xy_coords(xys, width), timeline_group)
            elif point.action == 'TRAIN_START':
                brush = QtGui.QBrush(QtGui.QColor(TRAIN_START_COLOR))
                xys = (point.time-t_0)/inter, 0
                item = QtWidgets.QGraphicsRectItem(xy_coords(xys, width), timeline_group)
            elif point.action == 'TRAIN_FINISHED':
                brush = QtGui.QBrush(QtGui.QColor(TRAIN_STOP_COLOR))
                xys = (point.time-t_0)/inter, -180
                item = QtWidgets.QGraphicsRectItem(xy_coords(xys, width), timeline_group)
            else:
                brush = QtGui.QBrush(QtGui.QColor('BLUE'))
                xys = (point.time-t_0)/inter, -360
                item = QtWidgets.QGraphicsRectItem(xy_coords(xys, width), timeline_group)
            i += 1
            item.setPen(pen)
            item.setBrush(brush)
            item.setToolTip(point.action+' '+ point.arg)



def xy_coords(xy, width):
    dw = width / 2.
    return QtCore.QRectF(xy[0] - dw, xy[1] - dw, width/15, width)