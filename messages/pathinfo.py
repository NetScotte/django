import logging


def pathinfo(func):
    def wrapper(*args, **kw):
        logging.info("call function:{} with {}".format(func.__name__, args))
        return func(*args, **kw)
    return wrapper