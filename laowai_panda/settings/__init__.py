try:
    from .local import *
except ImportError:
    try:
        from .production import *
    except ImportError as e:
        e.args = tuple(
            ['%s (did you create a copy settings/production-example.py?)' % e.args[0]])
        raise e
