from utils import Loader


def process(message: str, size: int) -> int:
    return next(i + size
                for i in range(len(message) - size + 1)
                if len(set(message[i:i + size])) == size)


def main() -> None:
    message = Loader.load()[0]
    print(f"part 1: {process(message, 4)}")
    print(f"part 2: {process(message, 14)}")


if __name__ == "__main__":
    main()
