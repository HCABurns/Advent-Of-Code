import API

inputs = API.get_input()

# Part 1.
def part1(inputs):
    total = 0
    for num in inputs:
        num = int(num)
        total += (num // 3) - 2
    return total

# Part 2.
def part2(inputs):
    total = 0
    for num in inputs:
        num = int(num)
        while num > 0:
            num = (num // 3) - 2
            total += num if num > 0 else 0
    return total


print(part1(inputs))
print(part2(inputs))
