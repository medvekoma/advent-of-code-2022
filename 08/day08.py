from typing import List

import numpy as np

from utils import Loader


def part1(matrix) -> int:
    rows = np.shape(matrix)[0]
    cols = np.shape(matrix)[1]
    left = np.full(np.shape(matrix), -1)
    right = np.full(np.shape(matrix), -1)
    top = np.full(np.shape(matrix), -1)
    bottom = np.full(np.shape(matrix), -1)
    for row in range(rows):
        for col in range(1, cols):
            left[row, col] = max(left[row, col - 1], matrix[row, col - 1])
        for col in range(cols - 2, -1, -1):
            right[row, col] = max(right[row, col + 1], matrix[row, col + 1])
    for col in range(cols):
        for row in range(1, rows):
            top[row, col] = max(top[row - 1, col], matrix[row - 1, col])
        for row in range(rows - 2, -1, -1):
            bottom[row, col] = max(bottom[row + 1, col], matrix[row + 1, col])
    trees = 0
    for row in range(rows):
        for col in range(cols):
            if matrix[row, col] > min(left[row, col], right[row, col], top[row, col], bottom[row, col]):
                trees = trees + 1
    return trees


def seen_trees(heights: List[int], my_height: int) -> int:
    return next((index for index, height in enumerate(heights) if height >= my_height), len(heights)-1) + 1


def part2(matrix) -> int:
    rows = np.shape(matrix)[0]
    cols = np.shape(matrix)[1]
    max_value = 0
    for row in range(rows):
        for col in range(cols):
            heights_list = [
                [matrix[row, c] for c in range(col - 1, -1, -1)],
                [matrix[row, c] for c in range(col + 1, cols, +1)],
                [matrix[r, col] for r in range(row - 1, -1, -1)],
                [matrix[r, col] for r in range(row + 1, rows, +1)]
            ]
            value = np.prod([seen_trees(heights, matrix[row, col]) for heights in heights_list])
            max_value = max(max_value, value)
    return max_value


def main() -> None:
    lines = Loader.load()
    array = [[int(ch) for ch in list(line)] for line in lines]
    matrix = np.array(array)
    print(f"part 1: {part1(matrix)}")
    print(f"part 2: {part2(matrix)}")


if __name__ == "__main__":
    main()
