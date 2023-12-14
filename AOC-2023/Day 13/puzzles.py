import numpy as np
from pprint import pprint

# with open("AOC-2023/Day 13/testinput.txt", "r") as f:
with open("AOC-2023/Day 13/input.txt", "r") as f:
    data = f.readlines()


data: list[str] = [x.strip("\n") for x in data]
data.append("") # necessary for for loop to catch last mapping

class Puzzle:
    def __init__(self, grid: list[str]):
        self.grid = grid

    def __repr__(self):
        return f"grid:{self.grid}\n"
    
def countCharDifferences(str1: str, str2: str) -> int:
    # returns -1 if strings are different by more than 1 char
    numDifferences: int = 0

    for (c1, c2) in zip(str1, str2):
        if c1 != c2:
            numDifferences += 1

    return numDifferences

def reflectsHorizontallyWSmudge(puzzle: Puzzle) -> int:
    # return number of rows above reflection *iff*
    # there is a horizontal reflection w/ smudge
    
    for i in range(1, len(puzzle.grid)):
        upperRows: list[str] = list(reversed(puzzle.grid[:i]))
        lowerRows: list[str] = puzzle.grid[i:]

        totalDifferences: int = 0
        for (upperRow, lowerRow) in zip(upperRows, lowerRows):
            totalDifferences += countCharDifferences(upperRow, lowerRow)

        if totalDifferences == 1:
            return i
        
    return 0


def reflectsVerticallyWSmudge(puzzle: Puzzle) -> int:
    grid: list[list[str]] = [list(x) for x in puzzle.grid]
    gridTranspose: list[str] = np.transpose(grid).tolist()
    newGrid = [''.join(item) for item in gridTranspose]
    
    return reflectsHorizontallyWSmudge(Puzzle(newGrid))


def reflectsHorizontally(puzzle: Puzzle) -> tuple:
    previousLine: str = ""
    matchingIndices: list[int] = []

    for row, line in enumerate(puzzle.grid):
        if line == previousLine:
            matchingIndices.append((row-1, row))

        previousLine = line

    toRtn = ()
    for match in matchingIndices:
        lowerIndex: int = match[0]
        upperIndex: int = match[1]

        lowerStr: str = ""
        upperStr: str = ""
        for i in range(lowerIndex, -1, -1):
            lowerStr += puzzle.grid[i]

        for i in range(upperIndex, len(puzzle.grid)):
            upperStr += puzzle.grid[i]

        if len(lowerStr) > len(upperStr):
            lowerStr = lowerStr[:len(upperStr)]

        elif len(upperStr) > len(lowerStr):
            upperStr = upperStr[:len(lowerStr)]

        if lowerStr == upperStr:
            toRtn = (lowerIndex, upperIndex)
        
        # if (smudgePos := equalWithOneCharDifference(lowerStr, upperStr)) > -1:
        #     toRtn = (lowerIndex, upperIndex)
            # puzzle.smudgePos = smudgePos
        
    return toRtn


def reflectsVertically(puzzle: Puzzle) -> tuple:
    grid: list[list[str]] = [list(x) for x in puzzle.grid]
    gridTranspose: list[str] = np.transpose(grid).tolist()
    newGrid = [''.join(item) for item in gridTranspose]
    
    return reflectsHorizontally(Puzzle(newGrid))


def findNewReflecValue(puzzle: Puzzle):
    for i, row in enumerate(puzzle.grid):
        for j, col in enumerate(row):
            newGrid = puzzle.grid[::]
            currentChar: str = newGrid[i][j]

            if currentChar == ".":
                replaceChar: str = "#"
                
            else:
                replaceChar: str = "."

            oldRow: str = newGrid[i]
            newGrid[i] = oldRow[:j] + replaceChar + oldRow[j+1:]

            newPuzzle: Puzzle = Puzzle(newGrid)
            newHorizontal = reflectsHorizontally(newPuzzle)
            newVertical = reflectsVertically(newPuzzle)

            if newHorizontal:
                rowsAbove: int = newHorizontal[0] + 1
                print(f"adding {100 * rowsAbove}")
                # total += 100 * rowsAbove
                return 100 * rowsAbove

            elif newVertical:
                colsToLeft: int = newVertical[0] + 1
                print(f"adding {colsToLeft}")
                # total += colsToLeft
                return colsToLeft


def puzzle1():
    puzzles: list[list[str]] = []

    tempPuzzle: list[str] = [] 
    for line in data:
        
        if line:
            tempPuzzle.append(line)
        else:
            puzzles.append(Puzzle(tempPuzzle))
            tempPuzzle = []

    total: int = 0
    for puzzle in puzzles:
        horizontal: tuple = reflectsHorizontally(puzzle)
        if horizontal:
            rowsAbove: int = horizontal[0] + 1
            total += 100 * rowsAbove

        else:
            vertical: tuple = reflectsVertically(puzzle)
            colsToLeft: int = vertical[0] + 1
            total += colsToLeft

    print(total)


def puzzle2():
    puzzles: list[Puzzle] = []

    tempPuzzle: list[str] = [] 
    for line in data:
        
        if line:
            tempPuzzle.append(line)
        else:
            puzzles.append(Puzzle(tempPuzzle))
            tempPuzzle = []

    total: int = 0
    for puzzle in puzzles:

        value: int = reflectsHorizontallyWSmudge(puzzle)*100 + reflectsVerticallyWSmudge(puzzle)

        if not value:

            horizontal: tuple = reflectsHorizontally(puzzle)
            if horizontal:
                rowsAbove: int = horizontal[0] + 1
                total += 100 * rowsAbove

            else:
                vertical: tuple = reflectsVertically(puzzle)
                colsToLeft: int = vertical[0] + 1
                total += colsToLeft

        else:
            total += value
        




    print(total)


if __name__ == "__main__":
    # puzzle1()
    puzzle2()