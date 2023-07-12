import json

from coverage import data

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


def write_config_module(device: Dev, scenarios):
    """
    Запись конфигурации модуля в файл.
    :param device:
    :param scenarios:
    :return:
    """

    config_module = {device.name: {"model": device.model,
                                   "description": device.description,
                                   "unit_id": device.unit_id,
                                   "baud_rate": device.baud_rate,
                                   "parity": device.parity,
                                   "stop_bits": device.stop_bits,
                                   "scenarios": scenarios,
                                   }
                     }

    with open(CONFIG_MODULE, "w", encoding="utf-8") as file_out:
        json.dump(config_module, file_out, ensure_ascii=False, indent=2)
