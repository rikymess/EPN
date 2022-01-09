from PyQt5 import QtCore, QtGui, QtWidgets
from db_handler import * 


class CheckThread(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(str)

    def thr_register(self, name, lastname, mail, time):
        register(name, lastname, mail, time, self.mysignal)