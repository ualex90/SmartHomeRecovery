from PyQt6.QtWidgets import QMainWindow

from config.config import CONFIG_MODULES, MODULES
from src.modbus.modbus import raed_module_info, read_scenarios
from src.models.Client import Client
from src.models.Dev import Dev
from src.qt.UI.UI_MainWin import Ui_MainWindow
from src.utils import get_config_modules, write_config_module


class MainWin(Ui_MainWindow):
    """
    Main window. Основное окно приложения.
    Объект унаследован от сосзданной формы при помощи QT Designer.
    """
    def __init__(self, clients, modules, MainWindow):
        self.clients = clients
        self.modules = modules
        self.config_modules = None
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

        # Запуск чтения из файла конфигурации модулей
        self.raed_file_button.clicked.connect(self.read_config)

        # Запуск записи в файл конфигурации модулей
        self.write_file_button.clicked.connect(self.write_config)

    def client_changed(self, client):
        # создание объекта класса Client
        self.change_client = Client(self.clients[client])

    def module_changed(self, module):
        """
        Выбор модуля. Создание объекта класса Dev.
        :param module: выбранный модуль
        """
        # создание объекта класса Dev
        self.change_module = Dev(self.modules[module])
        # очистка device_list
        self.device_list.clear()
        # вывод свойств модуля на device_list
        self.device_list.addItem(self.change_module.__str__())

    def read_config(self) -> str:
        """
        Запуск чтения из файла конфигурации модулей
        :return: Результат
        """
        self.config_modules = get_config_modules(CONFIG_MODULES)
        for module in self.config_modules:
            if module.get("name") == self.device_box.currentText():
                self.change_module = Dev(module)
                # очистка device_list
                self.device_list.clear()
                # вывод свойств модуля на device_list
                self.device_list.addItem(self.change_module.__str__())
                # вывод сценариев в device_list если прибор не найден или вывод сообщения что нет сценариев
                for scenario in self.change_module.scenarios:
                    if isinstance(scenario, dict):
                        self.device_list.addItem(list(scenario.keys())[0] + ": " + str(list(scenario.values())[0]))
                    else:
                        self.device_list.addItem("Нет сценариев")
                self.device_list.addItem("----------------------------------------------------------------")
                return "Ok"

        # очистка device_list
        self.device_list.clear()
        # вывод свойств модуля на device_list
        self.device_list.addItem(self.change_module.__str__())
        # Вывод информационного сообщения
        self.device_list.addItem("Отсутствует конфигурация в файле")
        return "Failed"

    def write_config(self):
        """
        Запись изменений в файл конфигурации модулей
        :return: Результат
        """
        # запись изменений в файл конфигурации модулей и вывод результата
        self.device_list.addItem(write_config_module(self.change_module))

    def read_module(self):
        """
        Чтение памяти модуля
        """
        # очистка device_list
        self.device_list.clear()
        # вывод свойств клиента на device_list
        self.device_list.addItem(self.change_client.__str__())
        # вывод свойств модуля на device_list
        self.device_list.addItem(self.change_module.__str__())
        # чтение сценариев из модуля и добавление их в объект
        self.change_module.scenarios = read_scenarios(self.change_module, self.change_client, 8)
        # чтение данных информации о модуле и вывод в device_list
        self.device_list.addItem(raed_module_info(self.change_module, self.change_client))
        # вывод сценариев в device_list если прибор не найден, вывод сообщение об ошибке
        for scenario in self.change_module.scenarios:
            if isinstance(scenario, dict):
                self.device_list.addItem(list(scenario.keys())[0] + ": " + str(list(scenario.values())[0]))
            else:
                self.device_list.addItem(str(scenario))
        self.device_list.addItem("----------------------------------------------------------------")
