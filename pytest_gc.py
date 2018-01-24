import gc

import pytest


def pytest_addoption(parser):
    parser.addoption('--gc-disable', action='store_true',
                     help='Disable automatic garbage collection')


@pytest.fixture(autouse=True)
def switch(request):
    if request.config.getoption('--gc-disable'):
        request.addfinalizer(gc.enable)
        gc.disable()
