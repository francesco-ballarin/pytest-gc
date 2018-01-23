pytest_plugins = "pytester",


def test_disable(testdir):
    testdir.makepyfile("""
    import gc

    def test_disable():
        assert not gc.isenabled()
    """)
    testdir.runpytest('--gc-disable').assert_outcomes(passed=1)
