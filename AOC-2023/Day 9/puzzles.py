# with open("AOC-2023/Day 9/testinput.txt", "r") as f:
with open("AOC-2023/Day 9/input.txt", "r") as f:
    data = f.readlines()


data: list[str] = [x.strip("\n") for x in data]

def predictNextVal(vals: list[int]):

    if len(set(vals)) == 1 and vals[0] == 0:
        return 0
    else:
        differences: list[int] = []

        for i in range(1, len(vals)):
            differences.append(vals[i] - vals[i-1])

        return vals[-1]+predictNextVal(differences)
    

def predictPreviousVal(vals):
    assert len(vals) > 0

    if len(set(vals)) == 1 and vals[0] == 0:
        return 0
    else:
        differences: list[int] = []
        for i in range(1, len(vals)):
            differences.append(vals[i] - vals[i-1])

        return vals[0]-predictPreviousVal(differences)


def puzzle1():
    sum: int = 0
    for line in data:
        sum += predictNextVal([int(x) for x in line.split()])

    print(sum)


def puzzle2():
    sum: int = 0
    for line in data:
        sum += predictPreviousVal([int(x) for x in line.split()])

    print(sum)


if __name__ == "__main__":
    # puzzle1()
    puzzle2()