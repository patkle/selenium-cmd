def exception_printer(func):
    def decorator(*a, **kw):
        try:
            return func(*a, **kw)
        except Exception as e:
            print(e)
    return decorator

def decorate_do_methods(decorator):
    """apply decorator to all methods starting with do_"""
    def decorate(cls):
        for attr in cls.__dict__:
            if not attr.startswith('do_'):
                continue
            if callable(getattr(cls, attr)):
                setattr(cls, attr, decorator(getattr(cls, attr)))
        return cls
    return decorate
