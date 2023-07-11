import time
from datetime import datetime

from pyModbusTCP.client import ModbusClient

from src.models.Dev import Dev


def get_single_holding(device: Dev, register) -> list:
    """
    Получение значения одного Holding Register
    :param device: Объект типа Dev
    :param register: Номер регистра
    :return: Значение регистра hex
    """
    try:
        client = ModbusClient(host=device.ip, port=device.port, unit_id=device.unit_id, timeout=5)
        reg = [hex(i) for i in client.read_holding_registers(register)]
        time.sleep(0.05)
        client.close()
        if reg:
            return reg
        else:
            return ['unable to read register']
    except ValueError:
        print(f"Error connecting to {device.ip}:{device.port}")


def get_single_input(device: Dev, register) -> list:
    """
    Получение значения одного Input Register
    :param device: Объект типа Dev
    :param register: Номер регистра
    :return: Значение регистра hex
    """

    try:
        client = ModbusClient(host=device.ip, port=device.port, unit_id=device.unit_id, timeout=5)
        reg = [hex(i) for i in client.read_input_registers(register)]
        time.sleep(0.05)
        client.close()
        if reg:
            return reg
        else:
            return ['unable to read register']
    except ValueError:
        print(f"Error connecting to {device.ip}:{device.port}")


def get_device_info(device: Dev) -> str:
    """"
    Получение информации о устройстве
    :param device: Объект типа Dev
    :return: Информация о устройстве
    """

    info = list()
    try:
        client = ModbusClient(host=device.ip, port=device.port, unit_id=device.unit_id, timeout=5)
        info = client.read_input_registers(9000, 25)
        time.sleep(0.05)
        client.close()
        if not info:
            return 'unable to read register'
    except ValueError:
        print(f"Error connecting to {device.ip}:{device.port}")

    return f"""Тип устройства: {info[3]}
             \rСерийный номер: {info[11]}-{info[12]}-{info[13]}-{info[14]}-{info[15]}-{info[16]} 
             \rВерсия ПО: {info[2]}.{info[0]}{info[1]}
             \rДата: {datetime(info[7], info[6], info[5], info[8], info[9]).strftime('%m.%d.%Y %H:%M')}
             \rСчетчик наработки часов: {info[21]}
             \rСчетчик записей flash: {info[22]}
             \rКоличество переключений (~/=): {info[23]}/{info[24]}"""


def read_scenarios(device: Dev, quantity=10) -> list:
    """"
    Чтение сценариев с устройства
    :param device: Объект типа Dev
    :param quantity: количество запрашиваемых сценариев
    :return: Список сценариев hex
    """

    scenarios = list()
    try:
        client = ModbusClient(host=device.ip, port=device.port, unit_id=device.unit_id, timeout=5)
        n = 100
        for i in range(quantity):
            regs = [hex(i) for i in client.read_holding_registers(n, 13)]
            if regs:
                scenarios.append({("Сценарий " + str(i)): regs})
            else:
                scenarios.append({("Сценарий " + str(i)): 'unable to read registers'})
            time.sleep(0.05)
            n += 20
        client.close()
    except ValueError:
        print(f"Error connecting to {device.ip}:{device.port}")
    return scenarios

