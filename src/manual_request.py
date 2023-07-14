from config.config import CLIENTS, CONFIG_MODULE
from src.modbus.modbus import read_scenarios, raed_device_info, write_module
from src.models.Dev import Dev
from src.utils import write_config_module, get_config_modules

# Создание объекта модуля (данные клиента tcp, данные модуля)
modules = get_config_modules(CONFIG_MODULE)
device = Dev(CLIENTS[1], modules[0])

# Создание объекта со значениями по-умлолчанию(данные клиента tcp)
default = Dev(CLIENTS[0])

# добавление сценариев в объект модуля
# device.scenarios = read_scenarios(device, 1)

# Свойства модуля
print(device, "\n")

# Информация из памяти устройства (Объект модуля)
# print(raed_device_info(device))

# Список сценариев устройства (Объект модуля, количество сценариев)
# [print(i) for i in read_scenarios(device, 8)]

# Запись данных модуля в файл JSON
# scenarios = read_scenarios(device, 8)
# write_config_module(device, scenarios)

# Запись параметров MODBUS и сценариев в память модуля, вывод результата
[print(i) for i in write_module(device)]
