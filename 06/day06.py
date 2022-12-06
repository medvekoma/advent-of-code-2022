from utils import Loader


def process(message: str, size: int) -> int:
    for i in range(len(message) - size + 1):
        marker = message[i:i+size]
        if len(set(marker)) == size:
            return i + size
    raise RuntimeError(f'No correct marker was found')


def main() -> None:
    content = Loader.load()
    if len(content) != 1:
        raise RuntimeError(f"There must be exactly one message. You received {len(content)} messages!")
    message = content[0]
    print(f"part 1: {process(message, 4)}")
    print(f"part 2: {process(message, 14)}")


if __name__ == "__main__":
    main()
