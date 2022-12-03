from utils import Loader, Collections


def priority(item: str) -> int:
    if item.islower():
        return ord(item) - ord('a') + 1
    elif item.isupper():
        return ord(item) - ord('A') + 27
    else:
        raise RuntimeError(f"Incorrect item: {item}")


def part1(rucksacks: list[str]) -> int:
    pairs = [(s[:len(s)//2], s[len(s)//2:]) for s in rucksacks]
    items = [set(a).intersection(set(b)) for (a, b) in pairs]
    result = [priority(item.pop()) for item in items]
    return sum(result)


def part2(rucksacks: list[str]) -> int:
    groups = Collections.split_into(rucksacks, 3)
    badges = [get_badge(group) for group in groups]
    priorities = [priority(badge) for badge in badges]
    return sum(priorities)


def get_badge(group: list[str]) -> str:
    sets = [set(rucksack) for rucksack in group]
    return set.intersection(*sets).pop()


def main() -> None:
    rucksacks = Loader.load()
    print(f"part 1: {part1(rucksacks)}")
    print(f"part 2: {part2(rucksacks)}")


if __name__ == "__main__":
    main()
