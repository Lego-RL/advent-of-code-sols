from collections import deque

# with open("AOC-2023/Day 5/testinput.txt", "r") as f:
with open("AOC-2023/Day 5/input.txt", "r") as f:
    data = f.readlines()


data: list[str] = [x.strip("\n") for x in data]

#add one empty line on end of data to signify end of last map
data.append("")

class SeedRange():
    def __init__(self, lower_bound: int, upper_bound: int):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

    
    def __repr__(self):
        return f"{self.lower_bound} - {self.upper_bound}"


class Mapping():
    def __init__(self, dest_range: int, source_range: int, range_length: int):
        self.dest_range = dest_range
        self.source_range = source_range
        self.range_length = range_length

    def withinSourceRange(self, num: int) -> bool:
        return num >= self.source_range and num < self.source_range+self.range_length
    
    
    def getDestination(self, num: int) -> int:
        return self.dest_range + (num - self.source_range)
    
    # methods for part 2
    def seedRangeWithinSourceRange(self, seedRange: SeedRange) -> SeedRange | None:
        lower_bound: int = max(self.source_range, seedRange.lower_bound)
        upper_bound: int = min(self.source_range+self.range_length-1, seedRange.upper_bound)

        if lower_bound >= upper_bound:
            return None
        
        intersectingSeedRange: SeedRange = SeedRange(lower_bound, upper_bound)
        return intersectingSeedRange
            

    def getDestinationMapping(self, seedRange: SeedRange):
        newLowerBound: int = self.dest_range + (seedRange.lower_bound - self.source_range)
        newUpperBound: int = self.dest_range + (seedRange.upper_bound - self.source_range)
        return SeedRange(newLowerBound, newUpperBound)
    

    def getRangeDifferences(self, seedRange: SeedRange) -> list[SeedRange] | None:
        returnRanges: list[SeedRange] = []
        
        # if self.source_range < seedRange.lower_bound:
        if seedRange.lower_bound < self.source_range:
            print("First case")
            returnRanges.append(SeedRange(seedRange.lower_bound, self.source_range-1))

        if self.source_range+self.range_length < seedRange.upper_bound:
            print("second case")
            # returnRanges.append(SeedRange(self.source_range+self.range_length-1, seedRange.upper_bound-1))
            returnRanges.append(SeedRange(self.source_range+self.range_length, seedRange.upper_bound))

        return returnRanges



def puzzle1():
    seeds: list[str] = data[0].split(":")[1].strip()
    seeds = list(map(lambda x: int(x.strip()), seeds.split()))

    constructingMap: bool = False

    currentMappings: list[Mapping] = []
    for line in data[1:]:
        if "map" in line:
            constructingMap = True

        elif constructingMap:
            if line != "":
                mappingData = list(map(lambda x: int(x.strip()), line.split()))
                currentMappings.append(Mapping(mappingData[0], mappingData[1], mappingData[2]))

            if line == "":
                constructingMap = False

                # we just finished constructing a map so process mappings

                for i, seed in enumerate(seeds):
                    for mapping in currentMappings:
                        if mapping.withinSourceRange(seed):
                            seeds[i] = mapping.getDestination(seed)

                # reset currentMappings for next set of maps to be constructed n used
                currentMappings.clear()

    print(min(seeds))



def puzzle2():
    seeds: list[str] = data[0].split(":")[1].strip()
    seeds = list(map(lambda x: int(x.strip()), seeds.split()))

    seedRanges: [list[SeedRange]] = []

    for i in range(0, len(seeds), 2):
        #subtract one in upper bound to maintain inclusive nature of upper bound
        seedRanges.append(SeedRange(seeds[i], seeds[i]+seeds[i+1]-1))
        

    constructingMap: bool = False

    currentMappings: list[Mapping] = []
    for line in data[1:]:
        if "map" in line:
            constructingMap = True

        elif constructingMap:
            if line != "":
                mappingData = list(map(lambda x: int(x.strip()), line.split()))
                currentMappings.append(Mapping(mappingData[0], mappingData[1], mappingData[2]))

            if line == "":
                constructingMap = False

                # we just finished constructing a map so process mappings
                rangesToMap: deque[SeedRange] = deque()

                # initialize deque with initial seedranges
                rangesToMap.extend(seedRanges)
                seedRanges.clear()

                while len(rangesToMap) > 0:
                    rangeToMap: SeedRange = rangesToMap.pop()

                    isMapped: bool = False
                    for mapping in currentMappings:
                        intersection: SeedRange | None = mapping.seedRangeWithinSourceRange(rangeToMap)
                        if intersection is not None:
                            isMapped = True
                            newRange = mapping.getDestinationMapping(intersection)
                            seedRanges.append(newRange)

                            rangeDifferences: list[SeedRange] = mapping.getRangeDifferences(rangeToMap)
                            if rangeDifferences is not None:
                                rangesToMap.extendleft(rangeDifferences)

                                break
                    
                    if not isMapped:
                        seedRanges.append(rangeToMap)

                # reset currentMappings for next set of maps to be constructed n used
                currentMappings.clear()


    print(min(list(map(lambda x: x.lower_bound, seedRanges))))


if __name__ == "__main__":
    puzzle2()