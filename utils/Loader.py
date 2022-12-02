import os
import inspect


def load(filename: str = None) -> list[str]:
    filename = filename or os.path.dirname((inspect.stack()[1])[1]) + "/input.txt"
    with open(filename) as file:
        return [line.rstrip() for line in file]


