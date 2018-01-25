pytest_plugins = 'pytester',


def test_disable(testdir):
    testdir.makepyfile("""
    import gc

    def test_disable():
        assert not gc.isenabled()
    """)
    testdir.runpytest('--gc-disable').assert_outcomes(passed=1)


def test_threshold(testdir):
    threshold = 1, 2, 3
    testdir.makepyfile("""
    import gc

    def test_threshold():
        assert gc.get_threshold() == {}
    """.format(threshold))
    testdir.runpytest('--gc-threshold', *threshold).assert_outcomes(passed=1)
