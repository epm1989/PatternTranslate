import logging
from functools import wraps


def create_log():
    logging.basicConfig(format='%(levelname)s %(levelno)s %(asctime)s %(message)s')
    logger = logging.getLogger('AlertLogic')
    return logger


logger = create_log()


def trace(skip: bool = False, quiet: bool = False):
    def catch_log(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            response = func(*args, **kwargs)
            if not skip:
                if quiet:
                    logger.warning(f'- Module:{func.__module__} - '
                                   f'Class:{args[0].__class__.__name__} - '
                                   f'FuncName:{func.__name__} ')
                else:
                    logger.warning(f'- Module:{func.__module__} - '
                                   f'Class:{args[0].__class__.__name__} - '
                                   f'FuncName:{func.__name__} - '
                                   f'Arguments:{kwargs} - Return:{response}')

            return response

        return wrapper

    return catch_log
