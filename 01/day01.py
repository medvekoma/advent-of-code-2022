from utils import Loader, Collections


def main() -> None:
    lines = Loader.load()
    items = Collections.split_by(lines, "")
    calories = [sum([int(elem) for elem in item]) for item in items]
    print(f"part 1: {max(calories)}")
    print(f"part 2: {sum(sorted(calories, reverse=True)[0:3])}")


if __name__ == "__main__":
    main()
