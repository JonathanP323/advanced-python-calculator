import importlib
import logging
import pandas as pd
from datetime import datetime
import os

VALID_COMMANDS = ["add", "subtract", "multiply", "divide", "history", "help", "exit"]

# Setup logging
logging.basicConfig(
    filename="calculator.log",
    level=logging.INFO,
    format="%(asctime)s - REPL - %(levelname)s - %(message)s",
)

HISTORY_FILE = "history.csv"

def log_history(command, a, b, result):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = {"timestamp": timestamp, "command": command, "a": a, "b": b, "result": result}

    if not os.path.exists(HISTORY_FILE):
        df = pd.DataFrame(columns=["timestamp", "command", "a", "b", "result"])
    else:
        df = pd.read_csv(HISTORY_FILE)

    df = pd.concat([df, pd.DataFrame([entry])], ignore_index=True)
    df.to_csv(HISTORY_FILE, index=False)

def run_repl():
    print("Welcome to the Advanced Python Calculator (REPL)")
    print("Available commands: add, subtract, multiply, divide, history, help, exit")

    while True:
        command = input("Enter command: ").strip().lower()
        logging.info(f"User entered command: {command}")

        if command not in VALID_COMMANDS:
            print("Invalid command. Try again.")
            logging.warning(f"Invalid command: {command}")
            continue

        if command == "exit":
            print("Goodbye!")
            logging.info("Exiting REPL")
            break

        if command == "history":
            if os.path.exists(HISTORY_FILE):
                df = pd.read_csv(HISTORY_FILE)
                print(df.to_string(index=False))
            else:
                print("No history available.")
            continue

        if command == "help":
            try:
                help_module = importlib.import_module("commands.help")
                help_module.run()
            except Exception as e:
                print(f"Error running help: {e}")
            continue

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            logging.info(f"Received inputs: a={a}, b={b}")
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        try:
            module = importlib.import_module(f"commands.{command}")
            result = module.run(a, b)
            print(f"Result: {result}")
            log_history(command, a, b, result)
            logging.info(f"{command}({a}, {b}) = {result}")
        except Exception as e:
            print(f"Error during calculation: {e}")
            logging.error(f"Calculation error: {e}")

