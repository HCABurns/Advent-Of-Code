import API

inputs = API.get_input()

# Part 1
def part1(inputs):
    prev = -1
    dial = 50
    code = 0
    for rot in inputs:
        d , val = rot[0], int(rot[1:])
        direction = 1 if d == "R" else -1
        amount = direction * val
        dial += amount
        dial %= 100 
        if dial == 0:
            code += 1
    return code

# Part 2
def part2(inputs):
    prev = -1
    dial = 50
    code = 0
    for rot in inputs:
        d , val = rot[0], int(rot[1:])
        direction = 1 if d == "R" else -1
        amount = direction * val

        for i in range(val):
            dial += direction
            dial %= 100
            
            if dial == 0:
                code += 1
    return code

print(part1(inputs))
print(part2(inputs))
