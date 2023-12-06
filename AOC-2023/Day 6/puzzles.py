from functools import reduce


# with open("AOC-2023/Day 6/testinput.txt", "r") as f:
with open("AOC-2023/Day 6/input.txt", "r") as f:
    data = f.readlines()


data: list[str] = [x.strip("\n") for x in data]

def puzzle1():

    numValidTimesPerRace: list[int] = []

    times: list[int] = list(map(lambda x: int(x), data[0].split("Time:")[1].split()))
    distances: list[int] = list(map(lambda x: int(x), data[1].split("Distance:")[1].split()))
    print(f"{times=}, {distances=}")

    for i, allowedTime in enumerate(times):
        numValidTimes: int = 0
        for j in range(1, int(allowedTime)):
            timeHeld: int = (allowedTime - j)
            distance: int =  timeHeld * j
            if distance > distances[i]:
                numValidTimes += 1

        
        numValidTimesPerRace.append(numValidTimes)

    print(reduce(lambda x, y: x*y, numValidTimesPerRace))


def puzzle2():
    time: int = int(reduce(lambda x, y: x+y, data[0].split("Time:")[1].split()).strip())
    distance: int = int(reduce(lambda x, y: x+y, data[1].split("Distance:")[1].split()).strip())

    numValidTimes: int = 0
    for j in range(1, int(time)):
        timeHeld: int = (time - j)
        distanceTravelled: int =  timeHeld * j
        if distanceTravelled > distance:
            numValidTimes += 1
    print(numValidTimes)


if __name__ == "__main__":
    puzzle2()