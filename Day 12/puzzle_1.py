from collections import defaultdict



with open('input.txt', 'r') as f:
    data = f.read().splitlines()

# with open('sample_input.txt', 'r') as f:
#     data = f.read().splitlines()

starting_cave = None
ending_cave = None
unique_caves = []
raw_unique_caves = []
cave_nums = {}



def is_big_cave(cave_notation):

    #if cave_notation (which is .lower() version) is not in
    #raw unique caves, then it is a big cave 
    try:
        idx = raw_unique_caves.index(cave_notation)
        return False

    except ValueError:
        return True




class Graph:

    valid_paths = 0
  
    def __init__(self, vertices):
        self.V = vertices
         
        
        self.graph = defaultdict(list)
        self.paths = 0

    def addEdge(self, u, v):
        self.graph[u].append(v)
  

    def printAllPathsUtil(self, u, d, visited, path):
 
        visited[cave_nums[u]]= True
        path.append(u)
 

        if u == d:
            self.paths += 1
        else:

            for i in self.graph[u]:
                if visited[cave_nums[i]] == False or (visited[cave_nums[i]] == True and is_big_cave(i)):
                    self.printAllPathsUtil(i, d, visited, path)

        path.pop()
        visited[cave_nums[u]]= False
  
  

    def printAllPaths(self, s, d):
 
        visited =[False]*(self.V)
 
        path = []
 
        self.printAllPathsUtil(s, d, visited, path)



cave_count = 0
for connection in data:
    left, right = connection.split('-')

    if left.lower() not in unique_caves:
        unique_caves.append(left.lower())
        raw_unique_caves.append(left)
        cave_nums[left.lower()] = cave_count
        cave_count += 1

    if right.lower() not in unique_caves:
        unique_caves.append(right.lower())
        raw_unique_caves.append(right)
        cave_nums[right.lower()] = cave_count
        cave_count += 1



g = Graph(len(unique_caves))


for connection in data:
    left, right = connection.split('-')
    if right.lower() not in g.graph[left.lower()]:
        g.addEdge(left.lower(), right.lower())

    if left.lower() not in g.graph[right.lower()]:
        g.addEdge(right.lower(), left.lower())



g.printAllPaths('start', 'end')
print(g.paths)
