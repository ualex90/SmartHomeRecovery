import yaml

from config.config import CONFIG_MODULE
from src.models.Dev import Dev


def get_mb_set_value(device: Dev) -> list:
    """
    Генерация значений HR0 (адрес) и HR1 (параметры интерфейса).
    :param device: Объект типа Dev.
    :return: Список значений HR0 и HR1.
    """
    hr0 = device.unit_id
    hr1 = str()
    match device.parity:
        case "N":
            hr1 = "0x00"
        case "E":
            hr1 = "0x02"
        case "O":
            hr1 = "0x04"

    match device.stop_bits:
        case 1:
            hr1 = "0x0" + str(int(hr1, 16) + 1)

    match device.baud_rate:
        case 9600:
            hr1 += "00"
        case 19200:
            hr1 += "01"
        case 38400:
            hr1 += "02"
        case 57600:
            hr1 += "03"
        case 115200:
            hr1 += "04"
        case 230400:
            hr1 += "05"

    return [hr0, int(hr1, 16)]


def get_config_modules(file) -> list:
    """
    Получение конфигурации модулей из файла.
    :param file: Путь к файлу конфигурации модуля.
    :return: Конфигурация модулей.
    """
    with open(file, "r", encoding="UTF-8") as file_in:
        data = yaml.safe_load(file_in)

    config_modules = list()
    for name, data in data.items():
        config_module = dict()
        config_module["name"] = name
        config_module["model"] = data["model"]
        config_module["description"] = data["description"]
        config_module["unit_id"] = data["unit_id"]
        config_module["baud_rate"] = data["baud_rate"]
        config_module["parity"] = data["parity"]
        config_module["stop_bits"] = data["stop_bits"]
        config_module["scenarios"] = data["scenarios"]
        config_modules.append(config_module)

    return config_modules


def write_config_module(device: Dev, scenarios=None):
    """
    Запись конфигурации модуля в файл.
    Если файл не существует, он будет создан.
    Если данные модуля уже ранее были записаны, то они будут обновлены.
    Если данных о модуле ранее небыло в файле, то они добавятся в конец файла
    :param device: Объект типа Dev.
    :param scenarios: Список сценариев либо список сценариев будет взят со свойств объекта
    :return: Результат записи в файл.
    """
    if scenarios is None:
        scenarios = device.scenarios

    try:
        with open(CONFIG_MODULE, "r", encoding="UTF-8") as file_in:
            config_module = yaml.safe_load(file_in)
    except FileNotFoundError:
        file = open(CONFIG_MODULE, "w")
        file.close()
        config_module = dict()

    config_module[device.name] = {"model": device.model,
                                  "description": device.description,
                                  "unit_id": device.unit_id,
                                  "baud_rate": device.baud_rate,
                                  "parity": device.parity,
                                  "stop_bits": device.stop_bits,
                                  "scenarios": scenarios,
                                  }

    with open(CONFIG_MODULE, "w", encoding="UTF-8") as file_out:
        yaml.safe_dump(config_module, file_out, sort_keys=False, allow_unicode=True)
