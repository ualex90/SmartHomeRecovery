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
        self.device_box.setGeometry(QtCore.QRect(10, 30, 251, 25))
        self.device_box.setObjectName("device_box")
        self.device_list = QtWidgets.QListWidget(parent=self.centralwidget)
        self.device_list.setGeometry(QtCore.QRect(10, 110, 631, 651))
        self.device_list.setObjectName("device_list")
        self.raed_device_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.raed_device_button.setGeometry(QtCore.QRect(280, 30, 171, 25))
        self.raed_device_button.setObjectName("raed_device_button")
        self.read_client_box = QtWidgets.QComboBox(parent=self.centralwidget)
        self.read_client_box.setGeometry(QtCore.QRect(10, 70, 251, 25))
        self.read_client_box.setObjectName("read_client_box")
        self.baud_rate_box = QtWidgets.QComboBox(parent=self.centralwidget)
        self.baud_rate_box.setGeometry(QtCore.QRect(720, 70, 101, 25))
        self.baud_rate_box.setObjectName("baud_rate_box")
        self.data_bit_box = QtWidgets.QComboBox(parent=self.centralwidget)
        self.data_bit_box.setGeometry(QtCore.QRect(830, 70, 41, 25))
        self.data_bit_box.setObjectName("data_bit_box")
        self.parity_box = QtWidgets.QComboBox(parent=self.centralwidget)
        self.parity_box.setGeometry(QtCore.QRect(880, 70, 41, 25))
        self.parity_box.setObjectName("parity_box")
        self.stop_bit_box = QtWidgets.QComboBox(parent=self.centralwidget)
        self.stop_bit_box.setGeometry(QtCore.QRect(930, 70, 41, 25))
        self.stop_bit_box.setObjectName("stop_bit_box")
        self.search_module_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.search_module_button.setGeometry(QtCore.QRect(990, 30, 171, 25))
        self.search_module_button.setObjectName("search_module_button")
        self.write_client_box = QtWidgets.QComboBox(parent=self.centralwidget)
        self.write_client_box.setGeometry(QtCore.QRect(720, 30, 251, 25))
        self.write_client_box.setObjectName("write_client_box")
        self.raed_file_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.raed_file_button.setGeometry(QtCore.QRect(470, 30, 171, 25))
        self.raed_file_button.setObjectName("raed_file_button")
        self.write_file_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.write_file_button.setGeometry(QtCore.QRect(470, 70, 171, 25))
        self.write_file_button.setObjectName("write_file_button")
        self.write_device_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.write_device_button.setGeometry(QtCore.QRect(720, 110, 251, 25))
        self.write_device_button.setObjectName("write_device_button")
        self.default_device_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.default_device_button.setGeometry(QtCore.QRect(720, 150, 251, 25))
        self.default_device_button.setObjectName("default_device_button")
        self.reboot_device_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.reboot_device_button.setGeometry(QtCore.QRect(720, 190, 251, 25))
        self.reboot_device_button.setObjectName("reboot_device_button")
        self.search_status_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.search_status_label.setGeometry(QtCore.QRect(990, 70, 171, 21))
        self.search_status_label.setStyleSheet("background-color: rgb(204, 0, 0);")
        self.search_status_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.search_status_label.setObjectName("search_status_label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.raed_device_button.setText(_translate("MainWindow", "Прочитать модуль"))
        self.search_module_button.setText(_translate("MainWindow", "Найти модуль"))
        self.raed_file_button.setText(_translate("MainWindow", "Прочитать из файла"))
        self.write_file_button.setText(_translate("MainWindow", "Записать в файл"))
        self.write_device_button.setText(_translate("MainWindow", "Записть прочитанное"))
        self.default_device_button.setText(_translate("MainWindow", "Записть по умолчанию"))
        self.reboot_device_button.setText(_translate("MainWindow", "Перезагрузить модуль"))
        self.search_status_label.setText(_translate("MainWindow", "None"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
