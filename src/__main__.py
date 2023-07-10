from config.config import CLIENTS, MODULES
from src.models.Dev import Dev


def main():
    device = Dev(CLIENTS[1], MODULES[0])
    default = Dev(CLIENTS[0])
    print(device, "\n")
    print(default)


if __name__ == '__main__':
    main()
