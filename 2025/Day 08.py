import API

example = API.get_example()
inputs = API.get_input()

class Junction:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def weight(self, junction2):
        x,y,z = junction2.get_coords()
        weight = ((self.x-x)**2 + (self.y-y)**2 + (self.z-z)**2)**0.5
        return weight

    def get_coords(self):
        return [self.x,self.y,self.z] 


def find(parent, val):
    if parent[val] != val:
        parent[val] = find(parent, parent[val])
    return parent[val]


def union(parent, rank, u, v):
    uroot = find(parent, u)
    vroot = find(parent, v)
    if rank[uroot] < rank[vroot]:
        parent[uroot] = vroot
    elif rank[uroot] > rank[vroot]:
        parent[vroot] = uroot
    else:
        parent[vroot] = uroot
        rank[uroot] += 1

# Part 1 using Kruskal's algorithm and a limit of connections.
def part1(inputs, target):
    junctions = [Junction(*map(int,row.split(","))) for row in inputs]

    edges = []
    for i,junction in enumerate(junctions):
        for j,junction2 in enumerate(junctions):
            if j <= i:continue
            edges.append([junction.weight(junction2), i, j])   
    
    edges.sort(key = lambda x : x[0])
    parent, rank = [], []

    for node in range(len(junctions)):
        parent.append(node)
        rank.append(0)
    i = 0
    counts = 0
    while counts < target and i < len(edges):
            _, u, v = edges[i]
            i += 1

            x = find(parent, u)
            y = find(parent, v)
            if x != y:
                union(parent, rank, x, y)
            counts += 1
    
    [find(parent, i) for i in range(len(parent))]
    largest = sorted([parent.count(i) for i in range(len(parent))], reverse=True)
    return largest[0] * largest[1] * largest[2]

# Part 2 using Kruskal's algorithm
def part2(inputs):
    junctions = [Junction(*map(int,row.split(","))) for row in inputs]
    edges = []
    for i,junction in enumerate(junctions):
        for j,junction2 in enumerate(junctions):
            if j <= i:continue
            edges.append([junction.weight(junction2), i, j])   
    
    edges.sort(key = lambda x : x[0])
    parent, rank = [], []

    for node in range(len(junctions)):
        parent.append(node)
        rank.append(0)
    i = 0
    counts = 0
    
    while i < len(edges):
            _, u, v = edges[i]
            i += 1

            x = find(parent, u)
            y = find(parent, v)
            if x != y:
                union(parent, rank, x, y)
                counts += 1

            if counts == len(junctions) - 1:
                return junctions[u].get_coords()[0] * junctions[v].get_coords()[0]
    return -1

print(part1(example, 10))
print(part1(inputs, 1000))
print(part2(example))
print(part2(inputs))
