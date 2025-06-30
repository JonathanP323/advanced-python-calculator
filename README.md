#Advanced Python Calculator

The present project is a complex command-line calculator. It is built to support arithmetic operations, flexibility to load new plugins on demand, history of previous calculations based on Pandas, and adoption of best software engineering practices, including logging, configuration flanked by the environment, unit tests, and different design patterns.
Key Features
•	Arithmetic Operations: Addition, Subtraction, Multiplication, Division
•	REPL Interface
•	Dynamic Plugin System
•	History Management: Powered by Pandas
•	Logging System
•	Environment-based Configuration
•	Multiple Design Patterns
•	Unit Testing with Pytest 

Design Patterns, Configuration, and Logging
1. Design Patterns Utilized
Facade Pattern: This pattern is used to simplify interactions with the history manager, which is built using Pandas.
•	Implementation: commands/calculator/history_manager.py 
Command Pattern: This pattern structures the different calculator commands (like add, subtract) into reusable and modular units.
•	Implementation: commands/command.py and specific command files such as commands/add.py 
Factory Pattern: The factory pattern generates command instances dynamically in the REPL environment.
•	Implementation: commands/calculator/repl.py 
Singleton Pattern: This ensures that the history manager has only one instance throughout the program, managing the application's state.
•	Implementation: commands/calculator/history_manager.py 
Strategy Pattern: This pattern promotes interchangeable command behaviors, each encapsulated in separate modules.
•	Implementation: commands/
2. Environment Variables
Environment variables are utilized to configure aspects of the logging system dynamically.
•	File: config.py 
Example:
export LOG_LEVEL=DEBUG
export LOG_FILE=calculator_debug.log
3. Logging
The calculator maintains logs for user actions, errors, and inputs to ensure transparency and assist with debugging.
•	Logging Configuration: config.py 
•	Log Usage: Found within commands/calculator/repl.py 
Log levels supported: INFO, WARNING, ERROR—all of which can be configured via environment variables.
4. Exception Handling (LBYL and EAFP)
The calculator integrates two exception-handling approaches: LBYL (Look Before You Leap) and EAFP (Easier to Ask for Forgiveness than Permission):
•	LBYL Example: Validating input types before executing operations.
•	EAFP Example: Using try/except blocks to handle division by zero errors.
Relevant Files:
•	Commands/divide.py 
•	Commands/calculator/repl.py 
Running the Application
To launch the application, use the following command:
python3 main.py
Running Tests
To run the test suite, use:
Pytest    
 
Watch the video demo here: [View on Google Drive](https://drive.google.com/file/d/1zRC75KJ7NBqJB9GkORGRu1yQiVV12ZmF/view?usp=drive_link)


