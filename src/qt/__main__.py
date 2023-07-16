import sys
from PyQt6 import QtWidgets


from src.qt.forms.MainWin import MainWin


def main():

    # Запуск приложения
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    main_win = MainWin(MainWindow)
    main_win.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
