from PyQt6.QtWidgets import QMainWindow

from src.modbus.modbus import raed_module_info, read_scenarios
from src.models.Dev import Dev
from src.qt.UI.UI_MainWin import Ui_MainWindow


class MainWin(Ui_MainWindow):
    """
    Main window. Основное окно приложения.
    Объект унаследован от сосзданной формы при помощи QT Designer.
    """
    def __init__(self, clients, modules, config_modules, MainWindow):
        self.clients = clients
        self.modules = modules
        self.config_modules = config_modules
        self.change_client = None
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

        # Заполнение client_box списком  клиентов и запуск функции выбора модуля
        self.client_changed(0)
        for client in range(len(self.clients)):
            self.read_client_box.addItem(self.clients[client].get("name"))
        self.read_client_box.currentIndexChanged.connect(self.client_changed)

        # Заполнение device_box списком модулей и запуск функции выбора модуля
        self.module_changed(0)
        for module in range(len(self.modules)):
            self.device_box.addItem(self.modules[module].get("name"))
        self.device_box.currentIndexChanged.connect(self.module_changed)

        # Запуск чтения памяти модуля
        self.raed_device_button.clicked.connect(self.read_module)

    def client_changed(self, client):
        self.change_client = self.clients[client]

    def module_changed(self, module):
        """
        Выбор модуля. Создание объекта класса Dev.
        :param module: выбранный модуль
        """
        # создание объекта класса Dev
        self.change_module = Dev(self.change_client, self.modules[module])
        # очистка device_list
        self.device_list.clear()
        # вывод свойств модуля на device_list
        self.device_list.addItem(self.change_module.__str__())

    def read_module(self):
        """
        Чтение памяти модуля
        """
        # очистка device_list
        self.device_list.clear()
        # обновление параметров клиента
        self.change_module.client = self.change_client.get('name')
        self.change_module.ip = self.change_client.get('ip')
        self.change_module.port = self.change_client.get('port')
        # чтение сценариев из модуля и добавление их в объект
        self.change_module.scenarios = read_scenarios(self.change_module, 8)
        # вывод свойств модуля на device_list
        self.device_list.addItem(self.change_module.__str__())
        # чтение данных информации о модуле и вывод в device_list
        self.device_list.addItem(raed_module_info(self.change_module))
        # вывод сценариев в device_list если прибор не найден, вывод сообщение об ошибке
        for scenario in self.change_module.scenarios:
            if isinstance(scenario, dict):
                self.device_list.addItem(list(scenario.keys())[0] + ": " + str(list(scenario.values())[0]))
            else:
                self.device_list.addItem(str(scenario))
