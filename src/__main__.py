from config.config import CLIENTS, MODULES
from src.modbus.modbus import read_scenarios, get_device_info
from src.models.Dev import Dev


def main():
    device = Dev(CLIENTS[0], MODULES[7])
    default = Dev(CLIENTS[0])

    print(device, "\n")
    print(get_device_info(device))

    [print(i) for i in read_scenarios(device, 1)]


if __name__ == '__main__':
    main()
