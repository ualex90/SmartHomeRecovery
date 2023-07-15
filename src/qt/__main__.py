import sys
from PyQt6 import QtWidgets

from config.config import CONFIG_MODULE
from src.qt.forms.MainWin import MainWin
from src.utils import get_config_modules


def main():
    # Чтение конфигурации из файла
    modules = get_config_modules(CONFIG_MODULE)

    # Запуск приложения
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    main_win = MainWin(modules, MainWindow)
    main_win.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
