import functools


def requests_session(**optional_kwargs):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            kwargs.update(optional_kwargs)
            return func(*args, **kwargs)
        return wrapper
    return decorator


@requests_session(hello='hello')
def test(*args, **kwargs):
    print('Kwargs:')
    print(kwargs)
    print()


test(haha='haha')
