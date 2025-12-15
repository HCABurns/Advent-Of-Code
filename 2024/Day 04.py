import API

example =  API.get_example()
inputs = API.get_input()

def part1(inputs):
    h, w = len(inputs), len(inputs[0])
    grid = inputs
    count = 0
    DIRS = [
        (0, 1), (0, -1),        
        (1, 0), (-1, 0),
        (1, 1), (1, -1),
        (-1, 1), (-1, -1)
    ]
    target = "XMAS"
    count = 0
    
    for i in range(h):
        for j in range(w):
            if grid[i][j] != "X":
                continue
            
            for di, dj in DIRS:
                try:
                    if i+3*di < 0 or i+3*di >= h or j+3*dj < 0 or j+3*dj >= w:
                        continue
                    word = "".join(grid[i + k*di][j + k*dj] for k in range(4))
                except IndexError:
                    continue
                if word == "XMAS":
                    count += 1
                
    return count

def part2(inputs):
    h, w = len(inputs), len(inputs[0])
    grid = inputs
    count = 0
    directions = [(1,1),(1,-1),(1,1),(-1,1)]
    for i,row in enumerate(grid[1:-1], 1):
        for j,char in enumerate(row[1:-1], 1):
            if char == "A":
                s1 = set([grid[i+1][j+1], grid[i-1][j-1]]) == {"M","S"}
                s2 = set([grid[i+1][j-1], grid[i-1][j+1]]) == {"M","S"}  
                if s1 == s2 == True:
                    count += 1
    return count


print(part1(example))
print(part1(inputs))
print(part2(example))
print(part2(inputs))
