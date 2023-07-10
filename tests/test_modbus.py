from config.config import CLIENTS, MODULES
from src.modbus.modbus import get_set_value
from src.models.Dev import Dev


def test_get_set_value():
    device = Dev(CLIENTS[1], MODULES[0])
    assert get_set_value(device) == [3, 260]
