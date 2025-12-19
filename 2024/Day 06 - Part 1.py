import API

example = API.get_example()
inputs = API.get_input()

DIRS = ([-1,0], [0,1], [1,0], [0,-1]) #Y,X

def parse_input(inputs):

    h , w = len(inputs), len(inputs[0])
    grid = []
    for i in range(h):
        grid.append(list(inputs[i]))
        if "^" in grid[-1]:
            start = (i, grid[-1].index("^"))

    return h, w, start, grid


def part1(inputs):
    h, w, start, grid = parse_input(inputs)
    i, j = start
    moves = 1
    moves2 = 0
    direction = 0
    while True:
        ni = i+DIRS[direction][0]
        nj = j+DIRS[direction][1]
        
        if 0>ni or ni>=h or nj < 0 or nj >= w:
            break
        nxt = grid[ni][nj]

        if nxt == "#":
            direction = (direction + 1) % 4
            continue

        if grid[i][j] != "X":
            moves += 1
        else:
            moves2 += 1
        grid[i][j] = "X"

        i = ni
        j = nj

    return moves, moves2


def part2(inputs):
    

    return

print(part1(example))
print(part1(inputs))
#print(part2(example))
#print(part2(inputs))
