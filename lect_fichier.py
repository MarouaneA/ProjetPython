__author__ = 'aatefma'




class Point(object):

    def __init__(self,time,action,arg):
        self.time=time
        self.action=action
        self.arg=arg
    def __repr__(self):
        return "<action.Point {0}>".format(self.name)


def load_actions(fichier):
    liste=[]
    with open(fichier,'r') as f:
        for line in f:
            l=str.split(line)
            L= l[0].split(',')
            liste.append(Point(int(L[0]),L[2]," , ".join(L[3:])))
    return liste



