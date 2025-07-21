"""Solutions for day 2"""

from typing import List, Tuple


def get_data(filename: str) -> List[Tuple[int, ...]]:
    """Format and returns data as a list of tuples"""
    with open(filename, "r", encoding="utf-8") as file:
        return [tuple(int(n) for n in line.split()) for line in file]


# def is_safe(level: Tuple[int, ...]) -> bool:
#     """Check if a level is safe"""
#     incr = [level[i] - level[i + 1] for i in range(len(level) - 1)]
#     print(set(incr))
#     return set(incr) <= {1, 2, 3} or set(incr) >= {-1, -2, -3}


def is_safe(level: Tuple[int, ...]) -> bool:
    """Check if a level is safe"""
    direction = level[1] - level[0]
    if direction == 0:
        return False

    return all(
        (next - curr) * direction > 0 and abs(next - curr) <= 3
        for curr, next in zip(level, level[1:])
    )


if __name__ == "__main__":
    FILENAME = "input.txt"
    data = get_data(FILENAME)

    test = data[0]
    print(list(zip(test, test[1:])))

    print(f"Solution 1: {sum( is_safe(level) for level in data)}")
