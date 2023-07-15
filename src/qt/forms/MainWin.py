from PyQt6.QtWidgets import QMainWindow

from config.config import CLIENTS
from src.modbus.modbus import raed_module_info, read_scenarios
from src.models.Dev import Dev
from src.qt.UI.UI_MainWin import Ui_MainWindow


class MainWin(Ui_MainWindow):
    """
    Main window. Основное окно приложения.
    Объект унаследован от сосзданной формы при помощи QT Designer.
    """
    def __init__(self, modules, MainWindow):
        self.modules = modules
        self.change_module = None
        self.MainWindow = MainWindow

    def setupUi(self, window: QMainWindow):
        """
        Вызывается при создании объекта формы.
        Здесь подключаются сигналы от виджетов
        и вызываются методы для их обработки
        :param window: объект окна
        """
        super().setupUi(self.MainWindow)

        self.add_module_in_device_box(self.modules)
        self.raed_device_button.clicked.connect(self.read_module)

    def add_module_in_device_box(self, modules):
        """
        Заполнения device_box для выбора модуля
        :param modules: список конфигураций модулей
        """
        self.module_changed(0)
        for module in range(len(modules)):
            self.device_box.addItem(modules[module].get("name"))
        self.device_box.currentIndexChanged.connect(self.module_changed)

    def module_changed(self, module, client=CLIENTS[0]):
        """
        Выбора модуля. Создание объекта класса Dev.
        :param module: выбранный модуль
        :param client: клиент
        """
        self.change_module = Dev(client, self.modules[module])
        self.device_list.clear()
        self.device_list.addItem(self.change_module.__str__())
        print(self.change_module)

    def read_module(self):
        self.device_list.clear()
        self.change_module.scenarios = read_scenarios(self.change_module, 8)
        self.device_list.addItem(self.change_module.__str__())
        self.device_list.addItem(raed_module_info(self.change_module))
