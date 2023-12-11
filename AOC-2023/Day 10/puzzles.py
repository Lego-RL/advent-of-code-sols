
# with open("AOC-2023/Day 10/testinput.txt", "r") as f:
with open("AOC-2023/Day 10/input.txt", "r") as f:
    data = f.readlines()


data: list[str] = [x.strip("\n") for x in data]


class Node():

    def __init__(self, coord: tuple[int], symbol: str, distance: int):
        self.coord = coord
        self.symbol = symbol
        self.distance = distance

    def __hash__(self):
        return self.coord[0] * 1000000 + self.coord[1]

    def __eq__(self, other):
        if isinstance(other, tuple):
            return self.coord == other
        else:
            return self.coord == other.coord
    
    def __repr__(self):
        return f"{self.symbol}: {self.coord}, {self.distance=}"

# tuples of (row, col)
NORTH: tuple[int, int] = (-1, 0)
SOUTH: tuple[int, int] = (1, 0)
EAST: tuple[int, int] = (0, 1)
WEST: tuple[int, int] = (0, -1) 

tileMap: dict[str, tuple[tuple[int]]] = {
    "|": (NORTH, SOUTH),
    "-": (EAST, WEST),
    "L": (NORTH, EAST),
    "J": (NORTH, WEST),
    "7": (SOUTH, WEST),
    "F": (SOUTH, EAST),
    ".": (),
    # animal location
    "S": (NORTH, SOUTH, EAST, WEST) 
}

global furthestNode
furthestNode: Node | None = None

def findValidNeighbors(tiles: list[tuple[str]], nodeCoord: tuple[int]) -> list[tuple[int]]:
    validNeighbors: list[tuple[int]] = []

    for offset in tileMap[tiles[nodeCoord[0]][nodeCoord[1]]]:
        tryIndex: tuple[int] = (nodeCoord[0] + offset[0], nodeCoord[1] + offset[1])

        if tryIndex[0] > -1 and tryIndex[1] > -1:
            if tryIndex[0] < len(tiles) and tryIndex[1] < len(tiles[0]):
                indexSymbol: str = tiles[tryIndex[0]][tryIndex[1]]
                indexOffsets: tuple[tuple[int]] = tileMap[indexSymbol]

                # see if paths connect
                # i.e, if current offset (say it's | and checking NORTH direction)
                # then indexOffsets should contain SOUTH direction if they connect
                # SOUTH + NORTH (or 1 + -1) should equal 0 when they connect 
                for indexOffset in indexOffsets:
                    if (offset[0]+indexOffset[0] == 0) and (offset[1]+indexOffset[1] == 0):
                        # paths connect so neighbor is reachable/valid
                        # print(f"adding {tryIndex=}")
                        validNeighbors.append(tryIndex)

    return validNeighbors


def findInvalidNeighbors(tiles: list[tuple[str]], nodeCoord: tuple[int]) -> list[tuple[int]]:
    invalidNeighbors: list[tuple[int]] = []

    for offset in tileMap[tiles[nodeCoord[0]][nodeCoord[1]]]:
        tryIndex: tuple[int] = (nodeCoord[0] + offset[0], nodeCoord[1] + offset[1])

        if tryIndex[0] > -1 and tryIndex[1] > -1:
            if tryIndex[0] < len(tiles) and tryIndex[1] < len(tiles[0]):
                indexSymbol: str = tiles[tryIndex[0]][tryIndex[1]]
                indexOffsets: tuple[tuple[int]] = tileMap[indexSymbol]

                # see if paths don't connect
                for indexOffset in indexOffsets:
                    if (offset[0]+indexOffset[0] != 0) or (offset[1]+indexOffset[1] != 0):
                        # paths connect so neighbor is reachable/valid
                        # print(f"adding {tryIndex=}")
                        invalidNeighbors.append(tryIndex)

    return invalidNeighbors

def addNeighbor(adjacents: dict[tuple[int], list[tuple[int]]], coord: tuple[int], neighborCoord: tuple[int]):

    if coord not in adjacents:
        adjacents[coord] = []

    adjacents[coord].append(neighborCoord)

    return adjacents


# tiles = map
# visited = list of visited nodes
# adjacents = map of coords to other valid coords adjacent to them
visited = set()
def bfs(tiles: list[str], node: tuple[int]):
    global visited
    visited = set()
    queue = set()
    
    visited.add(node)
    queue.add(node)

    distance: int = -1

    while queue:
        distance += 1
        # print(f'{distance=}, {len(queue)=}')
        newQueue: set = set()

        for visitingNode in queue:
            visited.add(visitingNode)
            validNeighbors: list[tuple[int]] = findValidNeighbors(tiles, visitingNode)
            validNeighbors = [x for x in validNeighbors if x not in visited]
            for neighbor in validNeighbors:
                newQueue.add(neighbor)

        queue = newQueue

    return distance

 
def puzzle1():
    # global visited
    start_index: tuple[int] = ()

    tiles: list = data[::]

    for i, line in enumerate(data):
        if (start:= line.find("S")) > -1:
            start_index = (i, start)
            break

    startNode: Node = Node(start_index, tiles[start_index[0]][start_index[1]], 0)
    visited = []
    maxDistance: int = bfs(data, startNode.coord)

    print(f"{maxDistance=}")



#  add new char * between 7F and JL
#  flood .'s and *'s 
# number of .'s left over is answer

def puzzle2():
    global visited
    tiles: list[str] = []
    
    replacements: dict[list[list[str]]] = {
        "7": ["...", "-7.", ".|."],
        "F": ["...", ".F-", ".|."],
        "J": [".|.", "-J.", "..."],
        "L": [".|.", ".L-", "..."],
        "|": [".|.", ".|.", ".|."],
        "-": ["...", "---", "..."],
        "S": [".|.", "-S-", ".|."],
        ".": ["...", ".^.", "..."],
    }

    # for line in data:
    #     tiles.append(line)

    

    for i, line in enumerate(data):
        lineInProg: str = ""
        

        for j, char in enumerate(line):

            if (i, j) not in visited:
                lineInProg += "."
            
            else:
                lineInProg += char

        tiles.append(lineInProg)

    # [print(x) for x in tiles]



    

    
    # expand each char into 3x3
    # flood outside starting from top left, changing adjacent .s to *s
    # any leftover .s are inside
        
    expandedGrid: list[str] = []
    # construct expanded grid
    for row in tiles:
        firstRow: str = ""
        secondRow: str = ""
        thirdRow: str = ""

        for char in row:
            replaceWith: list[str] = replacements[char]
            firstRow += replaceWith[0]
            secondRow += replaceWith[1]
            thirdRow += replaceWith[2]

        expandedGrid.append(firstRow)
        expandedGrid.append(secondRow)
        expandedGrid.append(thirdRow)

    # [print(x) for x in expandedGrid]
    
    # replace top left element with & to initiate flood fill operation
    expandedGrid[0] = "&" + expandedGrid[0][1:]

    # for every . or ^ char, if it's next to a & sign flip it to an &
    # initialized to 1 so while loop begins
    numFlipped: int = 1

    # if numflipped is 0 on any iteration, no more work to be done
    while numFlipped != 0:
        numFlipped = 0
        for i, row in enumerate(expandedGrid[::]):
            for j, char in enumerate(row):
                if char in [".", "^"]:
                    # if bordering &, change it

                    for dir in (NORTH, SOUTH, EAST, WEST):
                        coordToCheck: tuple[int, int] = (i+dir[0],j+dir[1])

                        if (coordToCheck[0] < 0 or coordToCheck[1] < 0) or (coordToCheck[0] >= len(expandedGrid) or coordToCheck[1] >= len(expandedGrid[0])):
                            continue

                        # print(f"{coordToCheck[0]=}, {len(expandedGrid)=}, {coordToCheck[1]}, {len(expandedGrid[coordToCheck[0]])}, ", flush=True)
                        try:
                            if expandedGrid[coordToCheck[0]][coordToCheck[1]] == "&":
                                numFlipped += 1
                                # expandedGrid[i][j] = "&"
                                oldRow: int = expandedGrid[i]
                                if j+1 >= len(expandedGrid[i]):
                                    expandedGrid[i] = expandedGrid[i][:j] + "&"
                                    # print('246')
                                else:
                                    expandedGrid[i] = expandedGrid[i][:j] + "&" + expandedGrid[i][j+1:]
                                    # print('249')

                                assert len(expandedGrid[i]) == len(oldRow)
                                break

                        except AssertionError:
                            pass
                            # print(f"{oldRow=}, {expandedGrid[i]}")

                        except Exception as x:
                            # print(f"{coordToCheck[0]=}, {len(expandedGrid)=}, {coordToCheck[1]}, {len(expandedGrid[coordToCheck[0]])}, ", flush=True)
                            # [print(x) for x in expandedGrid]
                            raise x
    


    # print(expandedGrid)
    # [print(x) for x in expandedGrid]


    carrotCount: int = 0

    for i, row in enumerate(expandedGrid):
        print(f"{carrotCount=}")
        for j, char in enumerate(row):
            if char == "^":
                print(f"{i=}, {j=}")
                carrotCount += 1

    print(carrotCount)
    # [print(x) for x in expandedGrid]


        


if __name__ == "__main__":
    puzzle1()
    puzzle2()