from config.config import CLIENTS, MODULES
from src.modbus.modbus import read_scenarios, get_device_info
from src.models.Dev import Dev
from src.utils import write_config_module

# Создание объекта модуля (данные клиента tcp, данные модуля)
device = Dev(CLIENTS[0], MODULES[7])

# Создание объекта со значениями по-умлолчанию(данные клиента tcp)
default = Dev(CLIENTS[0])

# добавление сценариев в объект модуля
device.scenarios = read_scenarios(device, 1)

# Свойства модуля
print(device, "\n")

# Информация из памяти устройства (Объект модуля)
print(get_device_info(device))

# Список сценариев устройства (Объект модуля, количество сценариев)
[print(i) for i in read_scenarios(device, 8)]

# Запись данных модуля в файл JSON
scenarios = read_scenarios(device, 8)
write_config_module(device, scenarios)
