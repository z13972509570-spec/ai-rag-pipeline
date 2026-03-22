import logging

def get_logger():
    logger = logging.getLogger(__name__)
    logger.basic_config(level=logging.INFO)
    return logger
