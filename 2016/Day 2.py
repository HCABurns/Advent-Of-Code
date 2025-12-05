import API

example = API.get_example()
inputs = API.get_input()


def part1(inputs):
    SIZE = 9
    numbers = {((i-1)//3,(i-1)%3):i for i in range(1,SIZE+1)}
    directions = {"U":[-1,0],"D":[1,0],"L":[0,-1],"R":[0,1]}
    y = x = 1
    code = 0
    for moves in inputs:
        for move in moves:
            dy, dx = directions[move]
            if y+dy >= 0 and y+dy < SIZE**0.5:
                y += dy
            if x+dx >= 0 and x+dx < SIZE**0.5:
                x += dx
        code = code*10 + numbers[(y,x)]
    return code


def part2(inputs):
    grid = ["##1##","#234#","56789","#ABC#","##D##"]
    numbers = {}
    for i,row in enumerate(grid):
        for j,char in enumerate(row):
            if char != "#":
                numbers[(i,j)] = char
    directions = {"U":[-1,0],"D":[1,0],"L":[0,-1],"R":[0,1]}
    y = 2
    x = 0
    code = []
    for moves in inputs:
        for move in moves:
            dy, dx = directions[move]
            if (y+dy, x+dx) in numbers:
                y += dy
                x += dx
        code.append(numbers[(y,x)])
    return "".join(code)


print(part1(example))
print(part1(inputs))
print(part2(example))
print(part2(inputs))
