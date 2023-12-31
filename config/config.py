from pathlib import Path

# Пути дирректорий
ROOT = Path(__file__).resolve().parent.parent
CONFIG = Path(ROOT, "config")

# Пути файлов
CONFIG_MODULES = Path(CONFIG, "config_modules.yaml")

UNIT_ID = [i for i in range(1, 13)]
BAUD_RATE = [9600, 19200, 38400, 57600, 115200, 230400]
DATA_BITS = [8]
PARITY = ["N", "E", "O"]
STOP_BITS = [1, 2]

# Настройка устройств
CLIENTS = [{"name": "USR-DR302", "ip": "192.168.3.4", "port": 502},
           {"name": "USR-DR302_Test", "ip": "192.168.3.8", "port": 502},
           {"name": "Test_Eth_Card", "ip": "192.168.3.9", "port": 502}]
MODULES = [{"name": "Module_A3", "model": "Razumdom_DRM88R", "description": "Управление оборудованием 230V",
            "unit_id": 3, "baud_rate": BAUD_RATE[4], "data_bits": DATA_BITS[0], "parity": PARITY[0],
            "stop_bits": STOP_BITS[0], "scenarios": []},

           {"name": "Module_A4", "model": "Razumdom_DRM21R", "description": "Питание кондиционера в прихожей",
            "unit_id": 4, "baud_rate": BAUD_RATE[4], "data_bits": 8, "parity": "N", "stop_bits": 1,
            "scenarios": []},

           {"name": "Module_A5", "model": "Razumdom_DRM21R", "description": "Питание кондиционера в гостиной",
            "unit_id": 5, "baud_rate": BAUD_RATE[4], "data_bits": DATA_BITS[0], "parity": PARITY[0],
            "stop_bits": STOP_BITS[0], "scenarios": []},

           {"name": "Module_A6", "model": "Razumdom_DRM21R", "description": "Питание бойлера",
            "unit_id": 6, "baud_rate": BAUD_RATE[4], "data_bits": DATA_BITS[0], "parity": PARITY[0],
            "stop_bits": STOP_BITS[0], "scenarios": []},

           {"name": "Module_A8", "model": "Razumdom_DRM88R", "description": "Управление оборудованием 24V",
            "unit_id": 8, "baud_rate": BAUD_RATE[4], "data_bits": DATA_BITS[0], "parity": PARITY[0],
            "stop_bits": STOP_BITS[0], "scenarios": []},

           {"name": "Module_A9", "model": "Razumdom_DDL88R", "description": "Диммер подсветки прихожей и предбанника",
            "unit_id": 9, "baud_rate": BAUD_RATE[4], "data_bits": DATA_BITS[0], "parity": PARITY[0],
            "stop_bits": STOP_BITS[0], "scenarios": []},

           {"name": "Module_A10", "model": "Razumdom_DDL88R", "description": "Диммер подсветки кухонного гарнитура",
            "unit_id": 10, "baud_rate": BAUD_RATE[4], "data_bits": DATA_BITS[0], "parity": PARITY[0],
            "stop_bits": STOP_BITS[0], "scenarios": []},

           {"name": "Module_A11", "model": "Razumdom_DDL88R", "description": "Диммер подсветки детской",
            "unit_id": 11, "baud_rate": BAUD_RATE[4], "data_bits": DATA_BITS[0], "parity": PARITY[0],
            "stop_bits": STOP_BITS[0], "scenarios": []},
           ]