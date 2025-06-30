import logging
import os

def get_logger(name):
    log_level = os.environ.get("LOG_LEVEL", "INFO").upper()
    log_file = os.environ.get("LOG_FILE", "calculator.log")

    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(getattr(logging, log_level, logging.INFO))

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

    return logger
