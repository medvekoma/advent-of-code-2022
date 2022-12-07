from utils import Loader, Collections
from typing import List, Tuple
import re
from enum import Enum


def create_stacks(crates: List[str]) -> List[List[str]]:
    cols = range(0, 9)
    rows = crates[len(crates) - 2::-1]
    stacks: List[List[str]] = [[] for _ in cols]
    for col in cols:
        index = 1 + col * 4
        for row in rows:
            box = row[index]
            if box != ' ':
                stacks[col].append(box)
    return stacks


class CrateMover(Enum):
    CM9000 = 1
    CM9001 = 2


def move(stacks: List[List[str]], count: int, source: int, target: int, crate_mover: CrateMover) -> None:
    boxes = [stacks[source - 1].pop() for _ in range(count)]
    if crate_mover == CrateMover.CM9001:
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


def process(stacks: List[List[str]], instructions: List[str], crate_mover: CrateMover) -> str:
    for instruction in instructions:
        count, source, target = parse_instruction(instruction)
        move(stacks, count, source, target, crate_mover)
    result = [stack.pop() for stack in stacks]
    return ''.join(result)


def main() -> None:
    lines = Loader.load()
    crates, instructions = Collections.split_by(lines, "")
    stacks = create_stacks(crates)
    print(f"part 1: {process(stacks, instructions, CrateMover.CM9000)}")
    stacks = create_stacks(crates)
    print(f"part 2: {process(stacks, instructions, CrateMover.CM9001)}")


if __name__ == "__main__":
    main()
