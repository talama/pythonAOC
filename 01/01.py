def get_data(fileName):
    with open(fileName, "r") as file:
        return [[int(n) for n in line.split()] for line in file]


def calc_dist(data):
    left, right = zip(*data)
    return sum(abs(a - b) for a, b in zip(sorted(left), sorted(right)))


if __name__ == "__main__":
    filename = "input.txt"

    data = get_data(filename)
    print(f"Solution1: {calc_dist(data)}")
