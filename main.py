import sys # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets, QtCore, QtGui
from des import *
from check_db import *




class Interface(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)  # Это нужно для инициализации нашего дизайна

        self.ui.pushButton.clicked.connect(self.register)
        self.base_line_Edit = [self.ui.lineEdit, self.ui.lineEdit_2, self.ui.lineEdit_3, self.ui.lineEdit_4]

        self.check_db = CheckThread()
        self.check_db.mysignal.connect(self.signal_handler)
    






    def check_input(funct):
         def wrapper(self):
            for line_edit in self.base_line_edit:
                if len(line_edit.text()) == 0:
                  return
            funct(self)
         return wrapper         
    

    def signal_handler(self, value):
        QtWidgets.QMessageBox.about(self,'Notification', value)

      


    def register(self):
        name = self.ui.lineEdit.text()
        lastname = self.ui.lineEdit_2.text()
        mail = self.ui.lineEdit_3.text()
        time = self.ui.lineEdit_4.text()
        self.check_db.thr_register(name, lastname, mail, time)




def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = Interface()  # Создаём объект класса ExampleApp
    window.setWindowFlags(window.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint) # Так мы убираем возможность нажать кнопку развернуть окно
    window.setFixedSize(window.size()) # а так устанавливаем фиксированный размер окна, без возможности изменить размер мышкой 
    window.show()  # Показываем окнa
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()

