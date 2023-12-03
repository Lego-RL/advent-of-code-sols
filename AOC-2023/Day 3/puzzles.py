# with open("input.txt", "r") as f:
with open("AOC-2023/Day 3/input.txt", "r") as f:
    data = f.readlines()


data: list[str] = [x.strip("\n") for x in data]

def addDot(line: str):
    line = "." + line + "."

    return line


def getIndicesToCheck(row: int, indicesNumberSpans: list[int]):

    indicesToCheck: list[tuple[int, int]] = []
    offsets = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

    for index in indicesNumberSpans:
        for offset in offsets:
            indicesToCheck.append((row+offset[0], index+offset[1]))

    return indicesToCheck


def indexInBounds(i: int, j: int, width: int, height: int) -> bool:
    if i < 0 or j < 0:
        return False
    
    if i > height-1 or j > width-1:
        return False
    return True


def puzzle1():
    i: int = -1
    j: int = -1
    partNums: list[int] = []

    notSymbols: list[str] = [".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    # add dot to start and end of data so always complete building num
    # when finding a non-number char
    paddedData = list(map(addDot, data))

    for line in paddedData:
        i += 1

        buildingNum: bool = False
        
        currentNum: str = ""

        # build each number, check if its a part num, move on
        for char in line:
            j += 1
            if char.isdecimal():
                currentNum += char
                buildingNum = True
            else:
                # it's a symbol
                if(buildingNum):
                    #number just ended so check if it's a part number
                    numIndex: int = j - len(currentNum)
                    indicesNumberSpans: list[int] = list(range(numIndex,numIndex+len(currentNum)))


                    indicesToCheck: list[tuple[int, int]] = getIndicesToCheck(i, indicesNumberSpans)
                    for index in indicesToCheck:
                        if indexInBounds(index[0], index[1], len(paddedData[0]), len(paddedData)):
                            checkChar: str = paddedData[index[0]][index[1]]
                            print(f"{index[0]}, {index[1]}, {checkChar=}")
                            if checkChar not in notSymbols:
                                partNums.append(int(currentNum))
                                break


                    buildingNum = False
                    currentNum = ""
        j = -1

    print(sum(partNums))


def puzzle2():
    i: int = -1
    j: int = -1

    partNums: list[int] = []

    #each key is index of a asterisk symbol that makes part numbers, 
    # value is part numbers adjacent to that asterisk
    possibleGears: dict[tuple[int, int], list[int]] = {}

    notSymbols: list[str] = [".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    # add dot to start and end of data so always complete building num
    # when finding a non-number char
    paddedData = list(map(addDot, data))

    for line in paddedData:
        i += 1

        buildingNum: bool = False
        
        currentNum: str = ""

        # build each number, check if its a part num, move on
        for char in line:
            j += 1
            if char.isdecimal():
                currentNum += char
                buildingNum = True
            else:
                # it's a symbol
                if(buildingNum):
                    #number just ended so check if it's a part number
                    numIndex: int = j - len(currentNum)
                    indicesNumberSpans: list[int] = list(range(numIndex,numIndex+len(currentNum)))

                    indicesToCheck: list[tuple[int, int]] = getIndicesToCheck(i, indicesNumberSpans)
                    for index in indicesToCheck:
                        if indexInBounds(index[0], index[1], len(paddedData[0]), len(paddedData)):
                            checkChar: str = paddedData[index[0]][index[1]]
                            if checkChar not in notSymbols:
                                if checkChar == "*":
                                    indexTuple: tuple[int, int] = (index[0], index[1])
                                    if indexTuple in possibleGears.keys():
                                        possibleGears[indexTuple] = possibleGears[indexTuple] + [int(currentNum)]
                                    else:
                                        possibleGears[indexTuple] = [int(currentNum)]
                                partNums.append(int(currentNum))
                                break


                    buildingNum = False
                    currentNum = ""
        j = -1

    gearRatioSum: int = 0
    for indexTuple, partVals in possibleGears.items():
        if len(partVals) == 2:
            gearRatio = partVals[0] * partVals[1]
            gearRatioSum += gearRatio

    print(gearRatioSum)



if __name__ == "__main__":
    # puzzle1()
    puzzle2()