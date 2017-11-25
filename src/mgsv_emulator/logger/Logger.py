import logging
from .. import settings

def create_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler(settings.LOG_FILE_PATH)
    fh.setLevel(logging.DEBUG)
    formatter = logging.Formatter('[%(asctime)s][%(module)s][%(levelname)s] %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger
