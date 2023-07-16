from config.config import CLIENTS, CONFIG_MODULES, MODULES
from src.modbus.modbus import read_scenarios, raed_module_info, write_module
from src.models.Client import Client
from src.models.Dev import Dev
from src.utils import write_config_module, get_config_modules

# Создание объекта модуля (данные клиента tcp, данные модуля)
modules = MODULES
# modules = get_config_modules(CONFIG_MODULE)
client = Client(CLIENTS[2])
device = Dev(modules[0])

# Создание объекта со значениями по-умлолчанию(данные клиента tcp)
default_client = Client()
default_dev = Dev()

# # Добавление сценариев в объект модуля
# device.scenarios = read_scenarios(device, client, 1)

# Свойства клиента и модуля
print(client)
print(device)

# # Информация из памяти устройства (Объект модуля)
# print(raed_module_info(device, client))

# Список сценариев устройства (Объект модуля, количество сценариев)
# [print(i) for i in read_scenarios(device, client, 8)]

# # Запись данных модуля в файл YAML
# scenarios = read_scenarios(device, 8)
# write_config_module(device, scenarios)

# # Запись параметров MODBUS и сценариев в память модуля, вывод результата
# mb_settings = ["0x0001", '0x0000']
# [print(i) for i in write_module(device, device, client, mb_settings)]
