import functools
import gc

import pytest


def pytest_addoption(parser):
    parser.addoption('--gc-disable', action='store_true',
                     help='Disable automatic garbage collection')
    parser.addoption('--gc-threshold', nargs='+', type=int,
                     help='Set the garbage collection thresholds')


@pytest.fixture(autouse=True)
def switch(request):
    if request.config.getoption('--gc-disable'):
        request.addfinalizer(gc.enable)
        gc.disable()


@pytest.fixture(autouse=True)
def change_threshold(request):
    threshold = request.config.getoption('--gc-threshold')
    if threshold:
        request.addfinalizer(
            functools.partial(gc.set_threshold, *gc.get_threshold())
        )
        gc.set_threshold(*threshold)
