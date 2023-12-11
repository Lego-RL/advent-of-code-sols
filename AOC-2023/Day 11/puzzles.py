import math

# with open("AOC-2023/Day 11/testinput.txt", "r") as f:
with open("AOC-2023/Day 11/input.txt", "r") as f:
    data = f.readlines()


data: list[str] = [x.strip("\n") for x in data]

class Location():
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.pair = (self.x, self.y)

    def __eq__(self, other):
        if isinstance(other, Location):
            return self.x == other.x and self.y == other.y
        
        return False

    def __repr__(self):
        return f"({self.x}, {self.y})"

class Galaxy():
    def __init__(self, id: int, location: Location):
        self.id = id
        self.location = location

    def updateLocation(self, newLocation: Location):
        self.location = newLocation

    def __eq__(self, other):
        if isinstance(other, Galaxy):
            return self.id == other.id
        
        else:
            return False
        
    def __repr__(self):
        return f"#{self.id} @ {self.location}"

def puzzle1():
    
    expandedRows: set = set(range(len(data)))
    expandedCols: set = set(range(len(data[0])))

    galaxies: list[Galaxy] = []
    pathsFound: dict[int, int] = {}
    for i, row in enumerate(data):
        for j, char in enumerate(row):
            if char == "#":
                expandedRows = expandedRows.difference({i})
                expandedCols = expandedCols.difference({j})
                galaxies.append(Galaxy(len(galaxies), Location(i, j)))

    for galaxy in galaxies:
        x: int = galaxy.location.x
        y: int = galaxy.location.y

        x += len([num for num in expandedRows if x > num])
        y += len([num for num in expandedCols if y > num])

        galaxy.updateLocation(Location(x, y))

    sum: int = 0
    for galaxy in galaxies:
        if galaxy.id not in pathsFound:
            pathsFound[galaxy.id] = []
        
        for otherGalaxy in galaxies:
            if otherGalaxy.id not in pathsFound:
                pathsFound[otherGalaxy.id] = []

            if galaxy.id in pathsFound[otherGalaxy.id] or otherGalaxy.id in pathsFound[galaxy.id]:
                continue

            if galaxy != otherGalaxy:
                # manhattan distance
                distance = abs(galaxy.location.y-otherGalaxy.location.y) + abs(galaxy.location.x-otherGalaxy.location.x)
                sum += distance

                
                pathsFound[galaxy.id].append(otherGalaxy.id)

    print(sum)
    



def puzzle2():
    expandedRows: set = set(range(len(data)))
    expandedCols: set = set(range(len(data[0])))

    galaxies: list[Galaxy] = []
    pathsFound: dict[int, int] = {}
    for i, row in enumerate(data):
        for j, char in enumerate(row):
            if char == "#":
                expandedRows = expandedRows.difference({i})
                expandedCols = expandedCols.difference({j})
                galaxies.append(Galaxy(len(galaxies), Location(i, j)))

    for galaxy in galaxies:
        x: int = galaxy.location.x
        y: int = galaxy.location.y

        x += len([num for num in expandedRows if x > num]) * (1000000-1)
        y += len([num for num in expandedCols if y > num]) * (1000000-1)

        galaxy.updateLocation(Location(x, y))

    sum: int = 0
    for galaxy in galaxies:
        if galaxy.id not in pathsFound:
            pathsFound[galaxy.id] = []
        
        for otherGalaxy in galaxies:
            if otherGalaxy.id not in pathsFound:
                pathsFound[otherGalaxy.id] = []

            if galaxy.id in pathsFound[otherGalaxy.id] or otherGalaxy.id in pathsFound[galaxy.id]:
                continue

            if galaxy != otherGalaxy:
                # manhattan distance
                distance = abs(galaxy.location.y-otherGalaxy.location.y) + abs(galaxy.location.x-otherGalaxy.location.x)
                sum += distance

                
                pathsFound[galaxy.id].append(otherGalaxy.id)

    print(sum)


if __name__ == "__main__":
    # puzzle1()
    puzzle2()