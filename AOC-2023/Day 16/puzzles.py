from enum import Enum
from pprint import pprint
import functools

# with open("AOC-2023/Day 16/testinput.txt", "r") as f:
with open("AOC-2023/Day 16/input.txt", "r") as f:
    data = f.readlines()


data: list[str] = [x.strip("\n") for x in data]

class Direction(Enum):
    NORTH = (-1, 0)
    SOUTH = (1, 0)
    EAST = (0, 1)
    WEST = (0, -1)


class Tile(Enum):
    EMPTY = "."
    RIGHTDIAG = "/"
    LEFTDIAG = "\\"
    VERTSPLITTER = "|"
    HORSPLITTER = "-"


class Point():
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        
    def __hash__(self):
        return hash(repr(self))

# if currently heading north 
northDirMap: dict[Tile, Direction | tuple[Direction]] = {
    "/": Direction.EAST,
    "\\": Direction.WEST,
    "|": Direction.NORTH,
    "-": (Direction.WEST, Direction.EAST),
}
southDirMap: dict[Tile, Direction | tuple[Direction]] = {
    "/": Direction.WEST,
    "\\": Direction.EAST,
    "|": Direction.SOUTH,
    "-": (Direction.WEST, Direction.EAST),
}
eastDirMap: dict[Tile, Direction | tuple[Direction]] = {
    "/": Direction.NORTH,
    "\\": Direction.SOUTH,
    "|": (Direction.NORTH, Direction.SOUTH),
    "-": Direction.EAST,
}
westDirMap: dict[Tile, Direction | tuple[Direction]] = {
    "/": Direction.SOUTH,
    "\\": Direction.NORTH,
    "|": (Direction.NORTH, Direction.SOUTH),
    "-": Direction.WEST,
}

# @functools.cache
def getNewDirection(tile: Tile, direction: Direction) -> Direction:
    match direction:
        case Direction.NORTH:
            return northDirMap[tile]
        case Direction.SOUTH:
            return southDirMap[tile]
        case Direction.EAST:
            return eastDirMap[tile]
        case Direction.WEST:
            return westDirMap[tile]



visitedLocs: set[Point] = set()
visitedSplitters: set[Point] = set()

# @functools.cache
def travel(grid: tuple[str], location: Point | None, travelDir: Direction, isStart: bool = False):

    if isStart:
        targetLoc: Point = location

    else:
        targetLoc: Point = Point(location.x + travelDir.value[0], location.y + travelDir.value[1])

    # if target grid location is off grid, done travelling
    if targetLoc.x < 0 or targetLoc.y < 0:
        return None
    
    elif targetLoc.x >= len(grid) or targetLoc.y >= len(grid[0]):
        return None
    
    # consider target tile now travelled
    visitedLocs.add(targetLoc)
    print(f"adding {targetLoc=}")

    match (targetTile := grid[targetLoc.x][targetLoc.y]):
    
        case Tile.EMPTY.value:
            return (targetLoc, travelDir)
        
        case Tile.RIGHTDIAG.value | Tile.LEFTDIAG.value:
            newTravelDir: Direction = getNewDirection(targetTile, travelDir)
            return (targetLoc, newTravelDir)
        
        case Tile.VERTSPLITTER.value | Tile.HORSPLITTER.value:
            
            newTravelDir: Direction | tuple[Direction] = getNewDirection(targetTile, travelDir)
            if isinstance(newTravelDir, tuple):
                if targetLoc in visitedSplitters:
                    return None
                
                visitedSplitters.add(targetLoc)
                
                return (targetLoc, *newTravelDir)
            
            else:
                return (targetLoc, newTravelDir)


def puzzle1():
    
    grid: tuple[str] = tuple(data)
    pathsToProgress: set[tuple[Point, Direction]] = set()
    pathsToProgress.add((Point(0, 0), Direction.EAST)) #just to have something to pop when beginning

    isStart: bool = True
    while pathsToProgress:
        currentPoint, currentDir = pathsToProgress.pop()
        newPath: tuple[Point, Direction] = travel(grid, currentPoint, currentDir, isStart)
        isStart = False
        if newPath:
            pathsToProgress.add((newPath[0], newPath[1]))
            # hit splitter and gave 2 new paths to follow
            if len(newPath) == 3:
                pathsToProgress.add((newPath[0], newPath[2]))
    print(f"{len(visitedLocs)=}")


def puzzle2():
    grid: tuple[str] = tuple(data)
    pathStartPoints: list[tuple[Point, Direction]] = []

    maxRow: int = len(grid)-1
    # TOP -> DOWN && BOTTOM -> UP
    for i in range(len(grid[0])):
        pathStartPoints.append((Point(0, i), Direction.SOUTH))
        pathStartPoints.append((Point(maxRow, i), Direction.NORTH))

    maxCol: int = len(grid[0])-1
    # LEFT -> RIGHT && RIGHT -> LEFT
    for i in range(len(grid)):
        pathStartPoints.append((Point(i, 0), Direction.EAST))
        pathStartPoints.append((Point(i, maxCol), Direction.WEST))

    # pprint(pathStartPoints)
    print(f"{len(pathStartPoints)=}")

    maxVisited: int = 0
    pathsStarted: int = 0
    for pathStart in pathStartPoints:
        pathsStarted += 1
        print(f"starting new path {pathStart=}, {pathsStarted=}")
        
        pathsToProgress: set[tuple[Point, Direction]] = set()
        pathsToProgress.add(pathStart)

        while pathsToProgress:
            currentPoint, currentDir = pathsToProgress.pop()
            newPath: tuple[Point, Direction] = travel(grid, currentPoint, currentDir)
            if newPath:
                pathsToProgress.add((newPath[0], newPath[1]))
                # hit splitter and gave 2 new paths to follow
                if len(newPath) == 3:
                    pathsToProgress.add((newPath[0], newPath[2]))

        if (tilesVisited := len(visitedLocs)) > maxVisited:
            maxVisited = tilesVisited

            ## TO VISUALIZE
            # energizedSpots: list[str] = [["." for x in range(len(grid))] for y in range(len(grid[0]))]

            # for point in visitedLocs:
            #     print(len(visitedLocs))
            #     energizedSpots[point.x][point.y] = "#"

            # pprint([''.join(x) for x in energizedSpots])

        visitedLocs.clear()
        visitedSplitters.clear()
    
    print(maxVisited)


if __name__ == "__main__":
    # puzzle1()
    puzzle2()