from itertools import groupby

# with open("AOC-2023/Day 12/testinput.txt", "r") as f:
with open("AOC-2023/Day 12/input.txt", "r") as f:
    data = f.readlines()


data: list[str] = [x.strip("\n") for x in data]

# only works for 1 block of question marks
def bruteForceCombos(numQuestionMarks: int, groups: list[int]):
    # print(f"{numQuestionMarks=}, {groups=}")

    if not groups:
        return 0

    total_to_fit = sum(groups) + len(groups) - 1

    if total_to_fit > numQuestionMarks:
        return 0

    # only one group of damaged springs to fit into one block of ?s
    if len(groups) == 1:
        onlyGroupingLength: int = groups[0]

        # group of 1 # can fit in every slot of numQuestionMarks
        if onlyGroupingLength == 1:
            return numQuestionMarks
        
        elif onlyGroupingLength == numQuestionMarks:
            return 1
        
        else:
            return 1 + (numQuestionMarks - onlyGroupingLength)

    return 1 + (numQuestionMarks - total_to_fit) + bruteForceCombos(numQuestionMarks-1, groups)

# check whether can remove set of known damaged springs from either side of line
def tryStripProblem(springs: str, groups: list[int], strBlocks: list[tuple]):
    if not groups:
        return (springs, groups)

    reversedBlocks: list[tuple] = strBlocks[::-1]
    reversedGroups: list[int] = groups[::-1]
    reversedSprings: str = springs[::-1]

    # print(f"{reversedBlocks=}")
    for block in reversedBlocks:
        if block[0] == ".":
            continue

        if block[0] == "?":
            break

        elif block[0] == "#":
            if block[1] == reversedGroups[0]:
                # cut off known grouping
                # print("cuttong off")
                reversedSprings = reversedSprings[reversedSprings.find("#"*block[1])+block[1]+1:]
                reversedGroups = reversedGroups[1:]
    # re-reverse springs w/ simplified input
    return (reversedSprings[::-1], reversedGroups[::-1])

def possibleCombos(springs: str, groups: list[int]) -> int:
    WORK_SPRING: str = "."
    BROKE_SPRING: str = "#"
    UNKNOWN: str = "?"

    strBlocks: list[tuple] = [(label, sum(1 for _ in group)) for label, group in groupby(springs)]

    springs, groups = tryStripProblem(springs, groups, strBlocks)

    #reset strBlocks incase springs & groups changed
    strBlocks: list[tuple] = [(label, sum(1 for _ in group)) for label, group in groupby(springs)]


    # short circuit
    # e.g. case where need to fit 2 groups of 2 damaged springs (so need 5 spaces min)
    # but have less than 5 spaces
    if len(springs) < sum(groups) + len(groups)-1:
        return 0

    # no springs left but still groups to fit, so they don't fit
    elif not springs and len(groups) > 0:
        return 0
    
    # if no more groups left but more damaged springs, not valid combo
    elif springs.find("#") > -1 and len(groups) == 0:
        return 0
    
    # no more groups to fit, so its a valid combo
    elif not springs and len(groups) == 0:
        # print(f"{springs=}, {groups=}, returning 1")
        return 1
    
    elif len(groups) == 0:
        return 0
    
    # when only unknowns left
    if len(strBlocks) == 1 and strBlocks[0][0] == UNKNOWN:
        unknownSpaces: int = strBlocks[0][1]

        return bruteForceCombos(unknownSpaces, groups)
    
    
    # disregard known working spring
    if springs.startswith(WORK_SPRING):
        return possibleCombos(springs[1:], groups)

    # if starting with unknown, test each case where it's working or damaged
    elif springs.startswith(UNKNOWN):
        # double check that groups[0] can't only fit once before continuing
        if len(strBlocks) > 1 and strBlocks[1][0] != BROKE_SPRING:

            #this set of question marks can be counted as only 1 possible way to configure
            # got here with groups being empty list
            if strBlocks[0][1] == groups[0]:
                return possibleCombos(springs[strBlocks[0][1]+1:], groups[1:])


        # print(f"trying both possibilities, {BROKE_SPRING}{springs[1:]} {groups=} & {WORK_SPRING}{springs[1:]}:\n")
        return possibleCombos(f"{BROKE_SPRING}{springs[1:]}", groups) + possibleCombos(f"{WORK_SPRING}{springs[1:]}", groups)
    
    # if first char is broken, check if long enough for first group
    elif springs.startswith(BROKE_SPRING):
        broke_spring_length = strBlocks[0][1]
        # print(f"{springs=}, {broke_spring_length=}")
        if broke_spring_length == groups[0]:

            # print(f"returning {springs[broke_spring_length+1:]=}, {groups[1:]=}")
            # +1 to account for necessary spacing between groups
            return possibleCombos(springs[broke_spring_length+1:], groups[1:])
        
        # broke spring group is too big to fit noted group length of groups[0]
        elif broke_spring_length > groups[0]:
            return 0
        
        # case where broke spring length is less than groups[0]
        # like #?#, groups[0] = 3
        else:
            groups[0] = groups[0] - 1


            return possibleCombos(springs[1:], groups)
        
    # temp
    # print(f"{springs=}, {groups=}, returning 0")
    return 0


def puzzle1():
    
    total: int = 0
    for line in data:
        springs, groups = line.split()

        groups = [int(x) for x in groups.split(',')]

        totalCombos: int = possibleCombos(springs, groups)
        total += totalCombos

    print(total)





def puzzle2():
    pass


if __name__ == "__main__":
    pass
    puzzle1()

    # fails, should be 4
    # print(possibleCombos("????.######..#####.", [1,6,5]))

    # succeeds, should be 1
    # print(possibleCombos("????.#...#...", [4,1,1]))

    # print(tryStripProblem("????.######..#####.", [1,6,5], [("?", 4), (".", 1), ("#", 6), (".", 2), ("#", 5), (".", 1)]))