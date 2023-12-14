import functools
from enum import Enum

# with open("AOC-2023/Day 12/testinput.txt", "r") as f:
with open("AOC-2023/Day 12/input.txt", "r") as f:
    data = f.readlines()


data: list[str] = [x.strip("\n") for x in data]


class Spring(Enum):
    WORKING = "."
    DAMAGED = "#"
    UNKNOWN = "?"

@functools.cache
def possibleCombos(springs: str, groups: tuple[int]) -> int:

    if not groups:
        if "#" not in springs:
            return 1
        
        else:
            return 0

    if not springs:
        return 0
    
    nextGroup = groups[0]        
    if springs.startswith(Spring.DAMAGED.value):
        springGroup: str = springs[:nextGroup]
        springGroup = springGroup.replace("?", "#")

        # damaged spring group isn't long enough to match known group length
        if springGroup != "#" * nextGroup:
            return 0 
        
        if len(springs) == nextGroup:
            if len(groups) == 1:
                return 1
            
            else:
                return 0
            
        # ensure group is separated by a valid separator
        if springs[nextGroup] in ".?":
            return possibleCombos(springs[nextGroup+1:], groups[1:])
        
        return 0
    
    elif springs.startswith(Spring.WORKING.value):
        return possibleCombos(springs[1:], groups)
    
    elif springs.startswith(Spring.UNKNOWN.value):
        return possibleCombos(f"#{springs[1:]}", groups) + possibleCombos(f".{springs[1:]}", groups)


def puzzle1():
    total: int = 0
    for line in data:
        springs, groups = line.split()

        groups = tuple([int(x) for x in groups.split(',')])

        totalCombos: int = possibleCombos(springs, groups)
        total += totalCombos

    print(total)


def puzzle2():
    total: int = 0
    for line in data:
        springs, groups = line.split()

        originalSprings: str = springs

        for _ in range(4):
            springs += f"?{originalSprings}"

        groups = [int(x) for x in groups.split(',')] * 5
        groups = tuple(groups)

        total += possibleCombos(springs, groups)

    print(total)


if __name__ == "__main__":
    # puzzle1()
    puzzle2()