import functools

# with open("AOC-2023/Day 15/testinput.txt", "r") as f:
with open("AOC-2023/Day 15/input.txt", "r") as f:
    data = f.readlines()


data: list[str] = [x.strip("\n") for x in data]

class Mirror():
    def __init__(self, string: str, focalLen: int):
        self.string = string
        self.focalLen = focalLen

    def __eq__(self, other):
        if isinstance(other, Mirror):
            return self.string == other.string
        
        return False
    
    def __repr__(self):
        return f"{self.string} w/ focal len {self.focalLen}"

@functools.cache
def hashStr(instruction: str) -> int:
    currentValue: int = 0
    for char in instruction:
        asciiCode = ord(char)
        currentValue += asciiCode

        currentValue *= 17
        currentValue %= 256
    return currentValue


def puzzle1():
    
    instructions = "".join(data).split(",")

    sum: int = 0
    for instruction in instructions:
        currentValue: int = 0
        for char in instruction:
            asciiCode = ord(char)
            currentValue += asciiCode

            currentValue *= 17
            currentValue %= 256
        
        sum += currentValue

    print(sum)


def puzzle2():
    instructions = "".join(data).split(",")

    boxes: dict[int, list[Mirror]] = {}

    for i in range(256):
        boxes[i] = []

    for instruction in instructions:

        if instruction[-1] == "-":
            string: str = instruction[:-1]
            hashVal: int = hashStr(string)

            for i in range(len(boxes[hashVal])):
                mirrorToCheck: Mirror = boxes[hashVal][i]
                if mirrorToCheck.string == string:
                    del boxes[hashVal][i]
                    break

        # instruction has "=" followed by focal length
        else:
            string: str = instruction[:-2]
            focalLen: int = int(instruction[-1])
            # don't include "=#" in hash val
            hashVal: int = hashStr(string)

            newMirror: Mirror = Mirror(string, focalLen)

            if newMirror in boxes[hashVal]:
                for i in range(len(boxes[hashVal])):
                    mirrorToCheck: Mirror = boxes[hashVal][i]
                    if mirrorToCheck.string == string:
                        # replace old mirror with new
                        boxes[hashVal][i] = newMirror

            else:
                boxes[hashVal].append(newMirror)


    sum: int = 0
    for i in range(256):
        for slotNum, mirror in enumerate(boxes[i]):
            sum += (1+i) * (slotNum+1) * mirror.focalLen


    print(sum)



if __name__ == "__main__":
    puzzle1()
    # puzzle2()