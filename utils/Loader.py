def load(filename: str = "input.txt") -> list[str]:
    with open(filename) as file:
        return [line.rstrip() for line in file]


