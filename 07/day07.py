from utils import Loader
from typing import Dict, List, Optional
import re
from functools import reduce


class Folder:
    def __init__(self, parent=None) -> None:
        self.parent: Optional["Folder"] = parent
        self.files: Dict[str, int] = {}
        self.folders: Dict[str, "Folder"] = {}
        self.total_size: int = 0

    def calculate_sizes(self) -> None:
        for _, folder in self.folders.items():
            folder.calculate_sizes()
        self.total_size = sum(size for _, size in self.files.items()) + sum(
            folder.total_size for _, folder in self.folders.items()
        )

    def flatten(self) -> List["Folder"]:
        flattened_folders: List["Folder"] = reduce(
            lambda a, b: a + b,
            [folder.flatten() for _, folder in self.folders.items()],
            [],
        )
        return [self, *flattened_folders]


def get_root(lines: List[str]) -> Folder:
    root = Folder()
    pwd: Folder = root
    regex = re.compile(r"(\d+) (.+)")

    for line in lines:
        if line == "$ cd /":
            pwd = root
        elif line == "$ cd ..":
            pwd = pwd.parent or root
        elif line.startswith("$ cd "):
            dir = line[5:]
            pwd = pwd.folders[dir]
        elif line.startswith("dir "):
            name = line[4:]
            if not pwd.folders.get(name):
                pwd.folders[name] = Folder(parent=pwd)
        elif match := re.match(regex, line):
            size_str, file_name = match.groups()
            pwd.files[file_name] = int(size_str)
    return root


def main() -> None:
    lines = Loader.load()
    root = get_root(lines)
    root.calculate_sizes()
    folders = root.flatten()

    part1 = sum(folder.total_size for folder in folders if folder.total_size <= 100000)
    print(f"part 1: {part1}")

    max_space = 70000000 - 30000000
    to_free = root.total_size - max_space
    part2 = min(folder.total_size for folder in folders if folder.total_size >= to_free)
    print(f"part 2: {part2}")


if __name__ == "__main__":
    main()
