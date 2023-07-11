import time
from datetime import datetime

from pyModbusTCP.client import ModbusClient

from src.models.Dev import Dev


def get_set_value(device: Dev) -> list:
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


def get_single_holding(device: Dev, register) -> list:
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


def get_info(device: Dev):
    """"
    Get information about the devices
    :param device: object of the Dev
    :return: info of devices
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
    Read scenarios from the device
    :param device: object of the Dev
    :param quantity: quantity of scenarios
    :return: list of scenarios
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

