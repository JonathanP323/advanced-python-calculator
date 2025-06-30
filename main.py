import os
import logging
from calculator.repl import run_repl
from logging_config import setup_logging

def main():
    setup_logging()
    logging.info("Starting the calculator application.")
    print("Welcome to the Advanced Python Calculator (REPL)")
    run_repl()
    logging.info("Calculator application terminated.")

if __name__ == "__main__":
    main()

