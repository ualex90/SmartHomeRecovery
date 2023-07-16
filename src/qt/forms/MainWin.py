from PyQt6.QtWidgets import QMainWindow

from config.config import CLIENTS, MODULES, CONFIG_MODULES, UNIT_ID, BAUD_RATE, DATA_BITS, PARITY, STOP_BITS
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
    def __init__(self, MainWindow):
        self.module = None
        self.read_client = None
        self.write_client = None
        self.unit_id = None
        self.new_unit_id = None
        self.baud_rate = None
        self.data_bits = None
        self.parity = None
        self.stop_bits = None
        self.MainWindow = MainWindow

    def setupUi(self, window: QMainWindow):
        """
        Вызывается при создании объекта формы.
        Здесь подключаются сигналы от виджетов
        и вызываются методы для их обработки
        :param window: объект окна
        """
        super().setupUi(self.MainWindow)

        # МОДУЛЬ. Заполнение device_box списком модулей и запуск функции выбора
        self._module_changed(0)
        for index in range(len(MODULES)):
            self.device_box.addItem(MODULES[index].get("name"))
        self.device_box.setCurrentIndex(0)
        self.device_box.currentIndexChanged.connect(self._module_changed)

        # КЛИЕНТ ЧТЕНИЯ. Заполнение read_client_box списком клиентов и запуск функции выбора
        self._read_client_set(0)
        for index in range(len(CLIENTS)):
            self.read_client_box.addItem(CLIENTS[index].get("name"))
        self.read_client_box.setCurrentIndex(0)
        self.read_client_box.currentIndexChanged.connect(self._read_client_set)

        # КЛИЕНТ ЗАПИСИ. Заполнение write_client_box списком клиентов и запуск функции выбора
        self._write_client_set(1)
        for index in range(len(CLIENTS)):
            self.write_client_box.addItem(CLIENTS[index].get("name"))
        self.write_client_box.setCurrentIndex(1)
        self.write_client_box.currentIndexChanged.connect(self._write_client_set)

        # UNIT ID ТЕКУЩИЙ. Заполнение unit_id_box списком  клиентов и запуск функции выбора
        self._unit_id_set(0)
        for index in UNIT_ID:
            self.unit_id_box.addItem(str(index))
        self.unit_id_box.setCurrentIndex(0)
        self.unit_id_box.currentIndexChanged.connect(self._unit_id_set)

        # UNIT ID НОВЫЙ. Заполнение new_unit_id_box списком  клиентов и запуск функции выбора
        self._new_unit_id_set(0)
        for index in UNIT_ID:
            self.new_unit_id_box.addItem(str(index))
        self.new_unit_id_box.setCurrentIndex(0)
        self.new_unit_id_box.currentIndexChanged.connect(self._new_unit_id_set)

        # BAUD RATE НОВЫЙ. Заполнение baud_rate_box списком  клиентов и запуск функции выбора
        self._baud_rate_set(0)
        for index in BAUD_RATE:
            self.baud_rate_box.addItem(str(index))
        self.baud_rate_box.setCurrentIndex(0)
        self.baud_rate_box.currentIndexChanged.connect(self._baud_rate_set)

        # DATA BITS НОВЫЙ. Заполнение data_bits_box списком  клиентов и запуск функции выбора
        self._data_bits_set(0)
        for index in DATA_BITS:
            self.data_bits_box.addItem(str(index))
        self.data_bits_box.setCurrentIndex(0)
        self.data_bits_box.currentIndexChanged.connect(self._data_bits_set)

        # PARITY НОВЫЙ. Заполнение parity_box списком  клиентов и запуск функции выбора
        self._parity_set(0)
        for index in PARITY:
            self.parity_box.addItem(str(index))
        self.parity_box.setCurrentIndex(0)
        self.parity_box.currentIndexChanged.connect(self._parity_set)

        # STOP BITS НОВЫЙ. Заполнение stop_bits_box списком  клиентов и запуск функции выбора
        self._stop_bits_set(1)
        for index in STOP_BITS:
            self.stop_bits_box.addItem(str(index))
        self.stop_bits_box.setCurrentIndex(1)
        self.stop_bits_box.currentIndexChanged.connect(self._stop_bits_set)

        # Запуск чтения памяти модуля
        self.raed_device_button.clicked.connect(self._read_module)

        # Запуск чтения из файла конфигурации модулей
        self.raed_file_button.clicked.connect(self._read_config)

        # Запуск записи в файл конфигурации модулей
        self.write_file_button.clicked.connect(self._write_config)

    def _module_changed(self, module):
        """
        Выбор модуля. Создание объекта класса Dev.
        :param module: выбранный модуль
        """
        # создание объекта класса Dev
        self.module = Dev(MODULES[module])
        # очистка device_list
        self.device_list.clear()
        # вывод свойств модуля на device_list
        self.device_list.addItem(self.module.__str__())

    def _read_client_set(self, index):
        # создание объекта класса Client
        self.read_client = Client(CLIENTS[index])

    def _write_client_set(self, index):
        # создание объекта класса Client
        self.write_client = Client(CLIENTS[index])

    def _unit_id_set(self, index):
        self.unit_id = UNIT_ID[index]

    def _new_unit_id_set(self, index):
        self.new_unit_id = UNIT_ID[index]

    def _baud_rate_set(self, index):
        self.baud_rate = BAUD_RATE[index]

    def _data_bits_set(self, index):
        self.data_bits = DATA_BITS[index]

    def _parity_set(self, index):
        self.parity = PARITY[index]

    def _stop_bits_set(self, index):
        self.stop_bits = STOP_BITS[index]

    def _read_config(self) -> str:
        """
        Запуск чтения из файла конфигурации модулей
        :return: Результат
        """
        self.config_modules = get_config_modules(CONFIG_MODULES)
        for module in self.config_modules:
            if module.get("name") == self.device_box.currentText():
                self.module = Dev(module)
                # очистка device_list
                self.device_list.clear()
                # вывод свойств модуля на device_list
                self.device_list.addItem(self.module.__str__())
                # вывод сценариев в device_list если прибор не найден или вывод сообщения что нет сценариев
                for scenario in self.module.scenarios:
                    if isinstance(scenario, dict):
                        self.device_list.addItem(list(scenario.keys())[0] + ": " + str(list(scenario.values())[0]))
                    else:
                        self.device_list.addItem("Нет сценариев")
                self.device_list.addItem("----------------------------------------------------------------")
                return "Ok"

        # очистка device_list
        self.device_list.clear()
        # вывод свойств модуля на device_list
        self.device_list.addItem(self.module.__str__())
        # Вывод информационного сообщения
        self.device_list.addItem("Отсутствует конфигурация в файле")
        return "Failed"

    def _write_config(self):
        """
        Запись изменений в файл конфигурации модулей
        """
        # запись изменений в файл конфигурации модулей и вывод результата
        self.device_list.addItem(write_config_module(self.module))

    def _read_module(self):
        """
        Чтение памяти модуля
        """
        # очистка device_list
        self.device_list.clear()
        # вывод свойств клиента на device_list
        self.device_list.addItem(self.read_client.__str__())
        # вывод свойств модуля на device_list
        self.device_list.addItem(self.module.__str__())
        # чтение сценариев из модуля и добавление их в объект
        self.module.scenarios = read_scenarios(self.module, self.read_client, 8)
        # чтение данных информации о модуле и вывод в device_list
        self.device_list.addItem(raed_module_info(self.module, self.read_client))
        # вывод сценариев в device_list если прибор не найден, вывод сообщение об ошибке
        for scenario in self.module.scenarios:
            if isinstance(scenario, dict):
                self.device_list.addItem(list(scenario.keys())[0] + ": " + str(list(scenario.values())[0]))
            else:
                self.device_list.addItem(str(scenario))
        self.device_list.addItem("----------------------------------------------------------------")
