from collections import Counter


def get_data(fileName):
    with open(fileName, "r") as file:
        return [[int(n) for n in line.split()] for line in file]


def calc_dist(left, right):
    return sum(abs(a - b) for a, b in zip(sorted(left), sorted(right)))


def calc_similarity(left, right):
    right_counts = Counter(right)
    return sum(num * right_counts[num] for num in left if num in right_counts)


if __name__ == "__main__":
    filename = "input.txt"

    left, right = zip(*get_data(filename))
    print(f"Solution1: {calc_dist(left, right)}")
    print(f"Solution2: {calc_similarity(left, right)}")
