import gc

import pytest


@pytest.fixture(autouse=True)
def switch():
    yield gc.disable()
    gc.enable()
