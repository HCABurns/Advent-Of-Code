import API

example = API.get_example()
inputs = API.get_input()


def part1(inputs):
    moves = inputs.strip().split(", ")
    pos = [0,0]
    DIRS = [(-1,0),(0,1),(1,0),(0,-1)]
    current_direction = 0

    for move in moves:
        current_direction = (current_direction + [1,-1][move[0] == "R"]) % 4
        quantity = int(move[1:])
        pos[0] += DIRS[current_direction][0] * quantity
        pos[1] += DIRS[current_direction][1] * quantity

    return sum(abs(i) for i in pos)


def part2(inputs):
    moves = inputs.strip().split(", ")
    y = x = 0
    DIRS = [(-1,0),(0,1),(1,0),(0,-1)]
    current_direction = 0
    seen = set((0,0))
    for move in moves:
        current_direction = (current_direction + [1,-1][move[0] == "R"]) % 4
        quantity = int(move[1:])
        for i in range(quantity):
            y += DIRS[current_direction][0]
            x += DIRS[current_direction][1]
            pos = (y,x)
            if pos in seen:
                return abs(y) + abs(x)
            seen.add(pos)
    return -1

print(part1(example))
print(part1(inputs))
print(part2(example))
print(part2(inputs))
