# Form implementation generated from reading ui file 'UI_MainWin.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1168, 769)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.device_box = QtWidgets.QComboBox(parent=self.centralwidget)
        self.device_box.setGeometry(QtCore.QRect(10, 30, 411, 25))
        self.device_box.setObjectName("device_box")
        self.device_list = QtWidgets.QListWidget(parent=self.centralwidget)
        self.device_list.setGeometry(QtCore.QRect(10, 80, 411, 681))
        self.device_list.setObjectName("device_list")
        self.raed_device_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.raed_device_button.setGeometry(QtCore.QRect(440, 30, 171, 25))
        self.raed_device_button.setObjectName("raed_device_button")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.raed_device_button.setText(_translate("MainWindow", "Прочитать модуль"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())