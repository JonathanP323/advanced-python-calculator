import os

# Environment variable for log level (default is INFO)
LOG_LEVEL = os.getenv("CALCULATOR_LOG_LEVEL", "INFO")

# Environment variable for the history file name (default is history.csv)
HISTORY_FILE = os.getenv("CALCULATOR_HISTORY_FILE", "history.csv")
