from enum import Enum
from pprint import pprint
import functools

# with open("AOC-2023/Day 14/testinput.txt", "r") as f:
with open("AOC-2023/Day 14/input.txt", "r") as f:
    data = f.readlines()

data: list[str] = tuple([x.strip("\n") for x in data])

class Direction(Enum):
    NORTH = 0
    WEST = 1
    SOUTH = 2
    EAST = 3
    
    
class Space(Enum):
    EMPTY = "."
    ROUND_ROCK = "O"
    CUBE_ROCK = "#"



# loop thru every row - if rounded rock, find furthest empty space and
# put rock there
@functools.cache
def tiltPlatform(platform: tuple[str], direction: Direction) -> tuple[str]:
    # return platform with rocks moved by tilt
    platform = list(platform)

    if direction == Direction.NORTH:
        for i in range(1, len(platform)):
            for j in range(len(platform[0])):
                char: str = platform[i][j]


                if char == Space.ROUND_ROCK.value:
                    rowOffset: int = 0

                    while platform[i-rowOffset-1][j] not in [Space.ROUND_ROCK.value, Space.CUBE_ROCK.value]:
                        if i-rowOffset-1 < 0:
                            break

                        rowOffset += 1

                    
                    platform[i] = platform[i][:j] + Space.EMPTY.value + platform[i][j+1:]
                    platform[i-rowOffset] = platform[i-rowOffset][:j] + Space.ROUND_ROCK.value + platform[i-rowOffset][j+1:]


    elif direction == Direction.EAST:
        for i in range(0, len(platform)):
            # loop from right to left so rocks properly tilt
            for j in range(len(platform[0])-2, -1, -1):
                char: str = platform[i][j]


                if char == Space.ROUND_ROCK.value:
                    colOffset: int = 0

                    while platform[i][j+colOffset+1] not in [Space.ROUND_ROCK.value, Space.CUBE_ROCK.value]:

                        colOffset += 1
                        if j+colOffset+1 >= len(platform[0]):
                            break

                    
                    platform[i] = platform[i][:j] + Space.EMPTY.value + platform[i][j+1:]
                    platform[i] = platform[i][:j+colOffset] + Space.ROUND_ROCK.value + platform[i][j+colOffset+1:]


    elif direction == Direction.SOUTH:
        # loop from bottom to top
        for i in range(len(platform)-2, -1, -1):
            for j in range(len(platform[0])):
                char: str = platform[i][j]


                if char == Space.ROUND_ROCK.value:
                    rowOffset: int = 0

                    while i+rowOffset+1 < len(platform) and platform[i+rowOffset+1][j] not in [Space.ROUND_ROCK.value, Space.CUBE_ROCK.value]:

                        rowOffset += 1
                        
                    
                    platform[i] = platform[i][:j] + Space.EMPTY.value + platform[i][j+1:]
                    platform[i+rowOffset] = platform[i+rowOffset][:j] + Space.ROUND_ROCK.value + platform[i+rowOffset][j+1:]

    elif direction == Direction.WEST:
        for i in range(0, len(platform)):
            # loop from left to right so rocks properly tilt
            for j in range(1, len(platform[0])):
                char: str = platform[i][j]


                if char == Space.ROUND_ROCK.value:
                    colOffset: int = 0

                    while platform[i][j-colOffset-1] not in [Space.ROUND_ROCK.value, Space.CUBE_ROCK.value]:
                        colOffset += 1
                        if j-colOffset-1 < 0:
                            break

                    
                    platform[i] = platform[i][:j] + Space.EMPTY.value + platform[i][j+1:]
                    platform[i] = platform[i][:j-colOffset] + Space.ROUND_ROCK.value + platform[i][j-colOffset+1:]
    return tuple(platform)
                


def calcLoad(platform: list[str]) -> int:
    totalValue: int = 0
    loadValue: int = len(platform)

    for row in platform:
        for char in row:
            if char == Space.ROUND_ROCK.value:
                totalValue += loadValue

        loadValue -= 1

    return totalValue


def puzzle1():
    tiltedPlatform = tiltPlatform(data, Direction.NORTH)
    pprint(tiltedPlatform)

    print(calcLoad(tiltedPlatform))



def puzzle2():
    platform = data[::]
    for i in range(1000000000):
        if i % 100000 == 0:
            print(f"on cycle {i}")

        for direction in Direction:
            platform = tiltPlatform(platform, direction)

    print(calcLoad(platform))

if __name__ == "__main__":
    # puzzle1()
    puzzle2()