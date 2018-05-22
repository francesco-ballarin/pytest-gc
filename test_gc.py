pytest_plugins = ("pytester",)


def test_disable(testdir):
    test_file = """
    import gc

    def test_disable():
        assert not gc.isenabled()
    """
    testdir.makepyfile(test_file)
    testdir.runpytest("--gc-disable").assert_outcomes(passed=1)


def test_threshold(testdir):
    threshold = 1, 2, 3
    test_file = """
    import gc

    def test_threshold():
        assert gc.get_threshold() == {}
    """
    testdir.makepyfile(test_file.format(threshold))
    testdir.runpytest("--gc-threshold", *threshold).assert_outcomes(passed=1)
