import time
import pytest


@pytest.mark.parametrize("order_id", range(10))
def test_order_status(order_id):
    time.sleep(1)
    assert order_id < 10