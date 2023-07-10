from config.config import CLIENTS, MODULES
from src.modbus.modbus import read_scenarios
from src.models.Dev import Dev


def main():
    device = Dev(CLIENTS[1], MODULES[0])
    default = Dev(CLIENTS[0])
    print(device, "\n")
    [print(i) for i in read_scenarios(device, 10)]


if __name__ == '__main__':
    main()
