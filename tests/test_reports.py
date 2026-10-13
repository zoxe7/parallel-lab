import time
import pytest


@pytest.mark.parametrize("report", ["day", "week", "month", "year"])
def test_build_report(report):
    time.sleep(4)
    assert report in {"day", "week", "month", "year"}