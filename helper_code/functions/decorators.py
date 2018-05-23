"""Helper decorator functions.

   Functions:
        timer: Calculate time taken to run given function and print to terminal.
        ntimes: Run given function n number of times.
        make_html: Create html element from inner func text.

   Decorator order important for combined use e.g:
        Run function twice and print total time taken for both function calls:
        @timer
        @ntimes(2)

        Run function twice and print time taken for each individual function call:
        @ntimes(2)
        @timer

"""
from time import time
from functools import wraps


def timer(func):
    """Decorator function: Calculate time taken to run given function and print to terminal."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'Timing {func.__name__}........')
        start = time()
        ret_value = func(*args, **kwargs)
        time_elapsed = time() - start
        print(f'Time elapsed: {time_elapsed:10.3}\n')
        return ret_value
    return wrapper


def ntimes(n):
    """Decorator function: Run given function n number of times."""
    def inner(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                ret_value = func(*args, **kwargs)
            return ret_value
        return wrapper
    return inner


def make_html(element):
    """Decorator function: Create html element from inner func text."""
    def inner(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            text = func(*args, **kwargs)
            return f'<{element}>{text}</{element}>'
        return wrapper
    return inner