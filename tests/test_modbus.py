import pytest

from config.test_data import TEST_MODULES
from src.modbus.modbus import get_set_value
from src.models.Dev import Dev


@pytest.mark.parametrize("module", [i for i in TEST_MODULES])
def test_get_set_value(module):
    device = Dev({}, module)
    assert get_set_value(device) == [module['unit_id'], module['result']]
