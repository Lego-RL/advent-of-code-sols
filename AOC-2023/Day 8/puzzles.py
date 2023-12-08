from math import lcm

# with open("AOC-2023/Day 8/testinput.txt", "r") as f:
with open("AOC-2023/Day 8/input.txt", "r") as f:
    data = f.readlines()


data: list[str] = [x.strip("\n") for x in data]

def findCycleLength(nodeMap: dict[str, tuple[str, str]], directions: str, startNode: str) -> int:
    visitedNodes: list[tuple[str, int]] = []
    nodesTraversed: int = 0

    currentNodeLabel = startNode
    while True:
        for directionIndex, turn in enumerate(directions):
            if turn == "L":
                currentNodeLabel = nodeMap[currentNodeLabel][0]

            elif turn == "R":
                currentNodeLabel = nodeMap[currentNodeLabel][1]
            
            nodesTraversed += 1
            alreadyVisited: list[str] = [node for node in visitedNodes if node[0] == currentNodeLabel and node[2] == directionIndex]

            if len(alreadyVisited) == 1:
                return nodesTraversed - alreadyVisited[0][1]

            visitedNodes.append((currentNodeLabel, nodesTraversed, directionIndex))


def puzzle1():

    START_NODE_LABEL: str = "AAA"
    END_NODE_LABEL: str = "ZZZ"

    directions: str = data[0]
    nodeMap: dict[str, tuple[str, str]] = {}

    for line in data[2:]:
        node, connections = line.split("=")
        node = node.strip()

        connections = connections.strip()
        conn1, conn2 = connections[1:4], connections[6:-1]

        nodeMap[node] = (conn1, conn2)

    nodesTraversed: int = 0

    currentNodeLabel = START_NODE_LABEL
    while currentNodeLabel != END_NODE_LABEL:
        for turn in directions:
            if turn == "L":
                currentNodeLabel = nodeMap[currentNodeLabel][0]

            elif turn == "R":
                currentNodeLabel = nodeMap[currentNodeLabel][1]
            
            nodesTraversed += 1
            if currentNodeLabel == END_NODE_LABEL:
                break

    print(nodesTraversed)

        
        
def puzzle2():
    directions: str = data[0]
    nodeMap: dict[str, tuple[str, str]] = {}
    startNodes: set[str] = set()
    endNodes: set[str] = set()

    for line in data[2:]:
        node, connections = line.split("=")
        node = node.strip()

        connections = connections.strip()
        conn1, conn2 = connections[1:4], connections[6:-1]

        nodeMap[node] = (conn1, conn2)

    for node in nodeMap.keys():
        if node[2] == "A":
            startNodes.add(node)
            print(f"{startNodes=}")

        elif node[2] == "Z":
            endNodes.add(node)


    currentNodes: list[str] = list(startNodes)
    cycleLengths: list[int] = []
    for node in currentNodes:
        cycleLengths.append(findCycleLength(nodeMap, directions, node))

    print(lcm(*cycleLengths))



if __name__ == "__main__":
    # puzzle1()
    puzzle2()