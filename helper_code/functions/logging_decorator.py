import logging
import pathlib
from functools import wraps


def config_logger():
    """Create project-wide logger, define settings and return logger"""
    # General settings. Change for individual projects.
    log_file = pathlib.Path.cwd() / 'log.txt'
    logging_format = '%(levelname)s:%(asctime)s:%(module)s:%(message)s'
    logging.basicConfig(level=logging.ERROR,
                        filename=log_file,
                        format=logging_format,
                        datefmt='%d-%m-%Y')
    logger = logging.getLogger(__name__)
    return logger


LOGGER = config_logger()


# TODO Doesn't log exceptions handled in passed func. Is there a work around?

def log_error(logger=LOGGER, *, silence_err=False):
    """Decorator function: Log any errors caught in wrapper func.
       Args:
            logger: Project logger object. Defaults to pre-set logger.
            silence_err: True = Log error and continue.
                         False = Log error then re-raise error.
    """
    def inner(func):
        @wraps(func)  # Keep passed function meta-data
        def wrapper(*args, **kwargs):
            try:
                ret_val = func(*args, **kwargs)
                return ret_val
            except Exception as exc:
                msg = f'{func.__name__}:{exc}'
                logger.error(msg)
                if not silence_err:
                    raise  # re-raise error
        return wrapper
    return inner
