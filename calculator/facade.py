from commands import add, subtract, multiply, divide

class CalculatorFacade:
    def __init__(self):
        self.commands = {
            'add': add.run,
            'subtract': subtract.run,
            'multiply': multiply.run,
            'divide': divide.run,
        }

    def execute(self, command, a, b):
        if command in self.commands:
            return self.commands[command](a, b)
        else:
            raise ValueError(f"Unknown command: {command}")
