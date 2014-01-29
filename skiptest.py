def skiptest(reason=None):
    def decorator(func):
        from nose.plugins.skip import SkipTest
        def _(*args, **kwargs):
            outputMessage = "Skip %s"
            if reason is not None:
                outputMessage += ": " + reason
            raise SkipTest( outputMessage % func.__name__ )
        _.__name__ = func.__name__
        return _
    return decorator
