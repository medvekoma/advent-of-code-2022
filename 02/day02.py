from utils import Loader


def bet_value(bet: str) -> int:
    match bet:
        case 'A' | 'X': return 1
        case 'B' | 'Y': return 2
        case 'C' | 'Z': return 3


def part1_win_points(difference: int) -> int:
    match difference:
        case -2 | 1: return 6
        case -1 | 2: return 0
        case 0: return 3


def part1(content: list[str]) -> None:
    bets = [(bet_value(line[0]), bet_value(line[2])) for line in content]
    points = [bet[1] + part1_win_points(bet[1] - bet[0]) for bet in bets]
    print(f"part 1: {sum(points)}")


def my_choice(his: int, result: int) -> int:
    match result:
        case 2: return his
        case 1: return 1 + (his - 1 + 2) % 3
        case 3: return 1 + (his - 1 + 1) % 3


def part2_win_points(choice: int) -> int:
    match choice:
        case 1: return 0
        case 2: return 3
        case 3: return 6


def part2(content: list[str]) -> None:
    bets = [(bet_value(line[0]), bet_value(line[2])) for line in content]
    choices = [(part2_win_points(bet[1]) + my_choice(bet[0], bet[1])) for bet in bets]
    print(f"part 2: {sum(choices)}")


def main() -> None:
    content = Loader.load()
    part1(content)
    part2(content)


if __name__ == "__main__":
    main()
