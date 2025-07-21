"""Day 1 Solutions"""

from collections import Counter
from typing import List, Tuple


def get_data(file_name: str) -> List[Tuple[int, ...]]:
    """format input data into a list of tuples"""
    with open(file_name, "r", encoding="utf-8") as file:
        return [tuple(int(n) for n in line.split()) for line in file]


def calc_dist(lt: Tuple[int, ...], rt: Tuple[int, ...]) -> int:
    """Caclculate disatance between two tuples"""
    return sum(abs(a - b) for a, b in zip(sorted(lt), sorted(rt)))


def calc_similarity(lt: Tuple[int, ...], rt: Tuple[int, ...]) -> int:
    """Calculate similarity between two tuples"""
    right_map = Counter(rt)
    return sum(num * right_map[num] for num in lt if num in right_map)


if __name__ == "__main__":
    FILENAME = "input.txt"

    data: List[Tuple[int, ...]] = get_data(FILENAME)
    left, right = zip(*get_data(FILENAME))
    print(f"Solution1: {calc_dist(left, right)}")
    print(f"Solution2: {calc_similarity(left, right)}")
