import API

inputs = API.get_input()

# Part 1.
def part1(inputs):
    num = 0
    for val in inputs:
        num = eval(str(num)+"+"+val)
    return num

# Part 2.  
def part2(inputs):
    seen = set([0])
    num = 0
    while True:
        for val in inputs:
            num = eval(str(num)+"+"+val)
            if num in seen:
                return num
            seen.add(num)
    return -1

print(part1(inputs))
print(part2(inputs))
