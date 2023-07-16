import sys
from PyQt6 import QtWidgets

from config.config import CONFIG_MODULES, CLIENTS, MODULES
from src.qt.forms.MainWin import MainWin
from src.utils import get_config_modules


def main():
    # Чтение конфигурации из файла
    modules = MODULES

    # Запуск приложения
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    main_win = MainWin(CLIENTS, modules, MainWindow)
    main_win.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
