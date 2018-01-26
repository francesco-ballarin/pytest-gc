class PluginLoader:
    @staticmethod
    def pytest_addoption(parser):
        parser.addoption('--gc-disable', action='store_true',
                         help='Disable automatic garbage collection')
        parser.addoption('--gc-threshold', nargs='+', type=int,
                         help='Set the garbage collection thresholds')

    @staticmethod
    def pytest_configure(config):
        options = 'gc_disable', 'gc_threshold'
        if any(map(config.getoption, options)):
            from pytest_gc import plugin
            config.pluginmanager.register(plugin)
