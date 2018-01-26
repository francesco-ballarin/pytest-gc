import functools
import gc

import pytest


@pytest.fixture(autouse=True)
def switch(request):
    if request.config.getoption('gc_disable'):
        request.addfinalizer(gc.enable)
        gc.disable()


@pytest.fixture(autouse=True)
def change_threshold(request):
    threshold = request.config.getoption('gc_threshold')
    if threshold:
        request.addfinalizer(
            functools.partial(gc.set_threshold, *gc.get_threshold())
        )
        gc.set_threshold(*threshold)
