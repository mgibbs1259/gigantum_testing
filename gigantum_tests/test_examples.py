

def test_simple_success(*args, **kwargs):
    """ Asserts trivially true as a demonstration. """
    assert True, 'This will never fail'


def test_simple_failure(*args, **kwargs):
    """ Asserts false as demonstration of failure. """
    assert False, 'This test always fails'


def test_simple_error(*args, **kwargs):
    """ Raises an exception to demo difference between
    success (pass), fail, and error conditions """
    raise ValueError('Example test error')
