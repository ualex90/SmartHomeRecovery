import pytest

from config.test_data import TEST_MODULES
from src.models.Dev import Dev
from src.utils import get_mb_set_value


@pytest.mark.parametrize("module", [i for i in TEST_MODULES])
def test_get_set_value(module):
    device = Dev({}, module)
    assert get_mb_set_value(device) == [module['unit_id'], module['result']]
