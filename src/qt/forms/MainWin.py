import time

from PyQt6.QtWidgets import QMainWindow

from config.config import CLIENTS, MODULES, CONFIG_MODULES, UNIT_ID, BAUD_RATE, DATA_BITS, PARITY, STOP_BITS
from src.modbus.modbus import raed_module_info, read_scenarios, read_single_holding, write_module, \
    write_multiple_holdings, write_single_holding
from src.models.Client import Client
from src.models.Dev import Dev
from src.qt.UI.UI_MainWin import Ui_MainWindow
from src.utils import get_config_modules, write_config_module, get_mb_set_value


class MainWin(Ui_MainWindow):
    """
    Main window. Основное окно приложения.
    Объект унаследован от сосзданной формы при помощи QT Designer.
    """
    def __init__(self, MainWindow: QMainWindow) -> None:
        self.module = None
        self.write_module = None
        self.read_client = None
        self.write_client = None
        self.unit_id = None
        self.new_unit_id = None
        self.new_baud_rate = None
        self.new_data_bits = None
        self.new_parity = None
        self.new_stop_bits = None
        self.MainWindow = MainWindow

    def setupUi(self, window: QMainWindow) -> None:
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
        self._new_baud_rate_set(0)
        for index in BAUD_RATE:
            self.new_baud_rate_box.addItem(str(index))
        self.new_baud_rate_box.setCurrentIndex(0)
        self.new_baud_rate_box.currentIndexChanged.connect(self._new_baud_rate_set)

        # DATA BITS НОВЫЙ. Заполнение data_bits_box списком  клиентов и запуск функции выбора
        self._new_data_bits_set(0)
        for index in DATA_BITS:
            self.new_data_bits_box.addItem(str(index))
        self.new_data_bits_box.setCurrentIndex(0)
        self.new_data_bits_box.currentIndexChanged.connect(self._new_data_bits_set)

        # PARITY НОВЫЙ. Заполнение parity_box списком  клиентов и запуск функции выбора
        self._new_parity_set(0)
        for index in PARITY:
            self.new_parity_box.addItem(str(index))
        self.new_parity_box.setCurrentIndex(0)
        self.new_parity_box.currentIndexChanged.connect(self._new_parity_set)

        # STOP BITS НОВЫЙ. Заполнение stop_bits_box списком  клиентов и запуск функции выбора
        self._new_stop_bits_set(1)
        for index in STOP_BITS:
            self.new_stop_bits_box.addItem(str(index))
        self.new_stop_bits_box.setCurrentIndex(1)
        self.new_stop_bits_box.currentIndexChanged.connect(self._new_stop_bits_set)

        # Запуск чтения памяти модуля
        self.raed_device_button.clicked.connect(self._read_module)

        # Запуск чтения из файла конфигурации модулей
        self.raed_file_button.clicked.connect(self._read_config)

        # Запуск записи в файл конфигурации модулей
        self.write_file_button.clicked.connect(self._write_config)

        # Запуск проверки связи с модулем
        self.check_connection_button.clicked.connect(self._check_connection)

        # Запись параметров считанного устройства в новое
        self.write_device_button.clicked.connect(self._write_device)

        # Перезагрузка модуля
        self.reboot_device_button.clicked.connect(self._reboot_device)

        # запись новых параметров modbus
        self.write_mb_set_button.clicked.connect(self._write_mb_set)

    def _module_changed(self, index: int) -> None:
        """
        Выбор модуля. Создание объекта класса Dev.
        :param index: индекс выбранного модуля из списка
        """
        # создание объекта класса Dev
        self.module = Dev(MODULES[index])
        # очистка device_list
        self.device_list.clear()
        # вывод свойств модуля на device_list
        self.device_list.addItem(self.module.__str__())

    def _read_client_set(self, index: int) -> None:
        # создание объекта класса Client
        self.read_client = Client(CLIENTS[index])

    def _write_client_set(self, index: int) -> None:
        # создание объекта класса Client
        self.write_client = Client(CLIENTS[index])

    def _unit_id_set(self, index: int) -> None:
        self.unit_id = UNIT_ID[index]

    def _new_unit_id_set(self, index: int) -> None:
        self.new_unit_id = UNIT_ID[index]

    def _new_baud_rate_set(self, index: int) -> None:
        self.new_baud_rate = BAUD_RATE[index]

    def _new_data_bits_set(self, index: int) -> None:
        self.new_data_bits = DATA_BITS[index]

    def _new_parity_set(self, index: int) -> None:
        self.new_parity = PARITY[index]

    def _new_stop_bits_set(self, index: int) -> None:
        self.new_stop_bits = STOP_BITS[index]

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

    def _write_config(self) -> None:
        """
        Запись изменений в файл конфигурации модулей
        """
        # запись изменений в файл конфигурации модулей и вывод результата
        self.device_list.addItem(write_config_module(self.module))
        self.search_status_label.setStyleSheet("background-color: rgb(46, 194, 126);")

    def _read_module(self) -> None:
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

    def _check_connection(self) -> None:
        """
        Проверка связи с модулем
        """
        self.write_module = Dev({'unit_id': self.unit_id})
        unit_id = read_single_holding(self.write_module, self.write_client, 0)
        if unit_id == hex(self.unit_id):
            self.search_status_label.setStyleSheet("background-color: rgb(46, 194, 126);")
            self.search_status_label.setText("Успешно")
        else:
            self.search_status_label.setStyleSheet("background-color: rgb(237, 0, 0);")
            self.search_status_label.setText("Ошибка")

    def _write_device(self) -> None:
        """
        Запись параметров в модуль
        """
        write_module(self.module, self.write_module, self.write_client)

    def _reboot_device(self) -> None:
        write_single_holding(self.write_module, self.write_client, self.write_module.reboot, '0xFF')

    def _write_mb_set(self) -> None:
        """
        Запись новых настроек MODBUS в модуль
        """
        set_dev = Dev()
        set_dev.unit_id = self.new_unit_id
        set_dev.baud_rate = self.new_baud_rate
        set_dev.data_bits = self.new_data_bits
        set_dev.parity = self.new_parity
        set_dev.stop_bits = self.new_stop_bits
        mb_settings = list(map(hex, get_mb_set_value(set_dev)))
        write_multiple_holdings(self.write_module, self.write_client, 0, mb_settings)
