from commands.divide import run

try:
    run(10, 0)
except ValueError as e:
    print("Caught ValueError as expected:", e)
