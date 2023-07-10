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


def read_scenarios(device: Dev, quantity=10) -> list:
    """"
    Read scenarios from the device
    :param device: object of the Dev
    :param quantity: quantity of scenarios
    :return: list of scenarios
    """

    scenarios = list()
    try:
        client = ModbusClient(host=device.ip, port=device.port, unit_id=device.unit_id)

        n = 100
        for i in range(quantity):
            scenarios.append({("Сценарий " + str(i)): [hex(i) for i in client.read_holding_registers(n, 13)]})
            n += 20

        client.close()
    except ValueError:
        print(f"Error connecting to {device.ip}:{device.port}")
    return scenarios
