import API

example = API.get_example()
inputs = API.get_input()

# Part 1
def part1(inputs):
    h = len(inputs)
    w = len(inputs[0])
    grid = []
    removed = 0
    for row in inputs:
        grid.append(list(row))
    
    directions = [[0,1],[1,0],[0,-1],[-1,0],[1,1],[-1,-1], [1,-1], [-1,1]]
    for i,row in enumerate(grid):
        for j,char in enumerate(row):
            if char == "@":
                paper = sum(1 if 0<=i+y<h and 0<=j+x<w and grid[i+y][j+x] == "@" else 0 for y,x in directions)
                if paper < 4:
                    removed += 1
    return removed

# Part 2
def part2(inputs):
    h = len(inputs)
    w = len(inputs[0])
    grid = [list(row) for row in inputs]
    total_removed = loops = 0
    removed = 1
    directions = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]
    
    while removed != 0:
        removed = 0
        for i,row in enumerate(grid):
            for j,char in enumerate(row):
                if char == "@":
                    paper = sum(0<=i+y<h and 0<=j+x<w and grid[i+y][j+x] == "@" for y,x in directions)
                    if paper < 4:
                        removed += 1
                        grid[i][j] = "."
        total_removed += removed
    return total_removed

print(part1(example))
print(part1(inputs))
print(part2(example))
print(part2(inputs))
