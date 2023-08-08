import time
from datetime import datetime

from pyModbusTCP.client import ModbusClient

from src.models.Client import Client
from src.models.Dev import Dev


def get_mb_set_value(device: Dev) -> list[hex]:
    """
    Генерация значений HR0 (адрес) и HR1 (параметры интерфейса).
    :param device: Объект типа Dev.
    :return: Список значений HR0 и HR1.
    """
    hr0 = hex(device.unit_id)
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

    return [hr0, hr1]


def read_single_holding(device: Dev, client, register) -> hex:
    """
    Чтение значения одного Holding Register
    :param device: Объект типа Dev
    :param client: Объект типа Client
    :param register: Номер регистра
    :return: Значение регистра hex
    """

    try:
        module = ModbusClient(host=client.ip, port=client.port, unit_id=device.unit_id, timeout=3)
        reg = module.read_holding_registers(register)
        time.sleep(0.05)
        module.close()
    except ValueError:
        return ['Connecting Error']
    else:
        if reg:
            return hex(reg[0])


def read_single_input(device: Dev, client, register) -> list[hex]:
    """
    Чтение значения одного Input Register
    :param device: Объект типа Dev
    :param client: Объект типа Client
    :param register: Номер регистра
    :return: Значение регистра hex
    """

    try:
        module = ModbusClient(host=client.ip, port=client.port, unit_id=device.unit_id, timeout=3)
        reg = [hex(i) for i in module.read_input_registers(register) if not None]
        time.sleep(0.05)
        module.close()
    except ValueError and TypeError:
        return [f"Error connecting to {client.ip}:{client.port}"]

    if reg:
        return reg
    return ['unable to read register']


def raed_module_info(device: Dev, client) -> str:
    """"
    Чтение информации о устройстве
    :param device: Объект типа Dev
    :param client: Объект типа Client
    :return: Информация о устройстве
    """

    try:
        module = ModbusClient(host=client.ip, port=client.port, unit_id=device.unit_id, timeout=3)
        info = module.read_input_registers(9000, 25)
        time.sleep(0.05)
        module.close()
    except ValueError and TypeError:
        return f"Error connecting to {client.ip}:{client.port}"

    if info:
        return f"""Тип устройства: {info[3]}
Серийный номер: {info[11]}-{info[12]}-{info[13]}-{info[14]}-{info[15]}-{info[16]} 
Версия ПО: {info[2]}.{info[0]}{info[1]}
Дата: {datetime(info[7], info[6], info[5], info[8], info[9]).strftime('%m.%d.%Y %H:%M')}
Счетчик наработки часов: {info[21]}
Счетчик записей flash: {info[22]}
Количество переключений (~/=): {info[23]}/{info[24]}
--------------------------------------------------------"""
    return 'unable to read registers module_info'


def read_scenarios(device: Dev, client, quantity=10) -> list:
    """"
    Чтение сценариев с устройства
    :param device: Объект типа Dev
    :param client: Объект типа Client
    :param quantity: количество запрашиваемых сценариев
    :return: Список сценариев hex
    """

    scenarios = list()
    try:
        module = ModbusClient(host=client.ip, port=client.port, unit_id=device.unit_id, timeout=3)
        start_register = 100
        for i in range(quantity):
            regs = [hex(i) for i in module.read_holding_registers(start_register, 13) if not None]
            if regs:
                scenarios.append({("Сценарий " + str(i)): regs})
            else:
                scenarios.append({("Сценарий " + str(i)): 'unable to read registers'})
            time.sleep(0.05)
            start_register += 20
        module.close()
    except ValueError and TypeError:
        return [f"Error connecting to {client.ip}:{client.port}"]

    return scenarios


def write_single_holding(device: Dev, client, register, data):
    """
    Запись значения одного Holding Register
    :param device: Объект типа Dev
    :param client: Объект типа Client
    :param register: Номер регистра
    :param data: Значение регистра hex
    :return: True если запись успешно записана или ошибка
    """
    try:
        module = ModbusClient(host=client.ip, port=client.port, unit_id=device.unit_id, timeout=3)
        is_ok = module.write_single_register(register, int(data, 16))
        time.sleep(0.1)
        module.close()
    except ValueError and TypeError:
        return [f"Error connecting to {client.ip}:{client.port}"]

    return "Ok" if is_ok else "Failed"


def write_multiple_holdings(device: Dev, client: Client, start_register, data):
    """
    Запись значения одного Holding Register
    :param device: Объект типа Dev
    :param client: Объект типа Client
    :param start_register: Номер начального регистра
    :param data: Значение регистра hex
    :return: True если запись успешно записана или ошибка
    """

    try:
        module = ModbusClient(host=client.ip, port=client.port, unit_id=device.unit_id, timeout=3)
        is_ok = module.write_multiple_registers(start_register, [int(i, 16) for i in data])
        time.sleep(0.2)
        module.close()
    except ValueError:
        return [f"Error connecting to {client.ip}:{client.port}"]

    return "Ok" if is_ok else "Failed"


def write_module(device: Dev, write_device: Dev, write_client, mb_settings=None, scenarios=None):
    """
    Запись параметров MODBUS и сценариев в память модуля
    :param device: Объект типа Dev. Данные подлежащие записи
    :param write_device: Объект типа Dev. Содержит текущий адрес устройства
    :param write_client: Объект типа Client
    :param mb_settings: Параметры MODBUS
    :param scenarios: Список сценариев
    :return: Результат записи
    """
    if mb_settings is None:
        mb_settings = get_mb_set_value(device)
    if scenarios is None:
        scenarios = device.scenarios

    write_status = list()

    # Запись параметров MODBUS
    write_status.append('Параметры MODBUS: ' + write_multiple_holdings(write_device, write_client, 0, mb_settings))
    # Запись сценариев
    start_register = 100
    for scenario in scenarios:
        number = list(scenario.keys())[0]
        data = list(scenario.values())[0]
        write_status.append(number + ': ' + write_multiple_holdings(write_device, write_client, start_register, data))
        start_register += 20
        print(f'\r{number} - Ok', end='')
    print("\rЗаписано. Ожидание 10 секунд")
    time.sleep(10)
    # Перезагрузка
    write_status.append('Перезагрузка: ' + write_single_holding(write_device, write_client, device.reboot, '0xFF'))
    print('Готово!')
    return write_status
