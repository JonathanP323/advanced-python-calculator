import logging
from config import LOG_LEVEL

def setup_logging():
    logging.basicConfig(
        level=getattr(logging, LOG_LEVEL.upper(), logging.INFO),
        format="%(asctime)s - %(levelname)s - %(message)s",
        filename="calculator.log",
        filemode="a"
    )
