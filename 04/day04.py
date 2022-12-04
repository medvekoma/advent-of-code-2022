from utils import Loader
import re
from typing import Tuple, List

R = re.compile(r'(\d+)-(\d+),(\d+)-(\d+)')


def parse_line(line: str) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    match = re.match(R, line)
    if match:
        a, b, c, d = match.groups()
        return (int(a), int(b)), (int(c), int(d))
    else:
        raise RuntimeError(f"No match in {line}")


def range_set(r: Tuple[int, int]) -> set[int]:
    return set(range(r[0], r[1] + 1))


def part1(content: List[Tuple[Tuple[int, int], Tuple[int, int]]]) -> int:
    ranges = [(range_set(r1), range_set(r2)) for r1, r2 in content]
    inclusions = [r1
                  for r1, r2 in ranges
                  if r1.intersection(r2) in [r1, r2]]
    return len(inclusions)


def part2(content: List[Tuple[Tuple[int, int], Tuple[int, int]]]) -> int:
    ranges = [(range_set(r1), range_set(r2)) for r1, r2 in content]
    inclusions = [r1
                  for r1, r2 in ranges
                  if r1.intersection(r2)]
    return len(inclusions)


def main() -> None:
    lines = Loader.load()
    result = [parse_line(line) for line in lines]

    print(f"part 1: {part1(result)}")
    print(f"part 2: {part2(result)}")


if __name__ == "__main__":
    main()
