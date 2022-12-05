from utils import Loader, Collections
from typing import List, Tuple, Callable
import re


def create_stacks(init: List[str]) -> List[List[str]]:
    cols = range(0, 9)
    rows = init[len(init) - 2::-1]
    stacks: List[List[str]] = [[] for _ in cols]
    for col in cols:
        index = 1 + col * 4
        for row in rows:
            box = row[index]
            if box != ' ':
                stacks[col].append(box)
    return stacks


MoveFunc = Callable[[List[List[str]], int, int, int], None]


def move1(stacks: List[List[str]], count: int, source: int, target: int) -> None:
    for step in range(count):
        value = stacks[source - 1].pop()
        stacks[target - 1].append(value)


def move2(stacks: List[List[str]], count: int, source: int, target: int) -> None:
    boxes = [stacks[source - 1].pop() for step in range(count)]
    boxes.reverse()
    for box in boxes:
        stacks[target - 1].append(box)


R = re.compile(r'move (\d+) from (\d+) to (\d+)')


def parse_instruction(instruction: str) -> Tuple[int, int, int]:
    match = re.match(R, instruction)
    if match:
        a, b, c = match.groups()
        return int(a), int(b), int(c)
    else:
        raise RuntimeError(f"Incorrect match for '{instruction}'")


def part(stacks: List[List[str]], instructions: List[str], move: MoveFunc) -> str:
    for instruction in instructions:
        count, source, target = parse_instruction(instruction)
        move(stacks, count, source, target)
    result = [stack.pop() for stack in stacks]
    return ''.join(result)


def main() -> None:
    lines = Loader.load()
    init, instructions = Collections.split_by(lines, "")
    stacks = create_stacks(init)
    print(f"part 1: {part(stacks, instructions, move1)}")
    stacks = create_stacks(init)
    print(f"part 2: {part(stacks, instructions, move2)}")


if __name__ == "__main__":
    main()
