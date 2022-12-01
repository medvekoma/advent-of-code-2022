from typing import TypeVar, Generator

T = TypeVar('T')


def split_by(the_list: list[T], element: T) -> Generator[list[T], None, None]:
    start_idx = 0
    for idx, line in enumerate(the_list):
        if line == element:
            yield the_list[start_idx:idx]
            start_idx = idx + 1
    yield the_list[start_idx:]