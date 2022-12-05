from utils import Loader
import re
from typing import Tuple, List, Callable, Set

R = re.compile(r'(\d+)-(\d+),(\d+)-(\d+)')


def parse_line(line: str) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    match = re.match(R, line)
    if match:
        a, b, c, d = match.groups()
        return (int(a), int(b)), (int(c), int(d))
    else:
        raise RuntimeError(f"No match in {line}")


def range_set(r: Tuple[int, int]) -> Set[int]:
    return set(range(r[0], r[1] + 1))


ConditionFunc = Callable[[set[int], set[int]], bool]


def condition1(r1: Set[int], r2: Set[int]) -> bool:
    return r1.intersection(r2) in [r1, r2]


def condition2(r1: set[int], r2: Set[int]) -> bool:
    return r1.intersection(r2) != set()


def part(content: List[Tuple[Tuple[int, int], Tuple[int, int]]], condition: ConditionFunc) -> int:
    ranges = [(range_set(r1), range_set(r2)) for r1, r2 in content]
    inclusions = [1 for r1, r2 in ranges if condition(r1, r2)]
    return len(inclusions)


def main() -> None:
    lines = Loader.load()
    result = [parse_line(line) for line in lines]

    print(f"part 1: {part(result, condition1)}")
    print(f"part 2: {part(result, condition2)}")


if __name__ == "__main__":
    main()
