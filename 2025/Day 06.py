import API
from math import prod

example = API.get_example()
inputs = API.get_input()

# Part 1.
def part1(inputs):
    # Find all numbers.
    nums = []
    for row in inputs[:-1]:
        nums.append([])
        for val in row.split(" "):
            if val:
                nums[-1].append(int(val))
    total = 0
    i = 0
    # Perform operation on all numbers in column i.
    for char in inputs[-1]:
        if char != " ":
            if char == "+":
                total += sum(nums[row][i] for row in range(len(nums)))
            else:
                total += prod([nums[row][i] for row in range(len(nums))])
            i+=1
    return total

# Part 2.
def part2(inputs):

    # Get index of splitter columns - A splitter is a column with only space chars.
    splitters = [-1]
    for col in range(len(inputs[0])):
        if all(inputs[row][col] == " " for row in range(len(inputs))):
            splitters.append(col)
    splitters.append(len(inputs[0]))

    # Find the order of operations.
    operations = [i for i in inputs[-1] if i != " "]

    total= 0
    for i in range(1,len(splitters)):
        # Find all numbers used in operation i-1 (Vertically down a column is 1 number)
        nums = []
        max_size = splitters[i] - splitters[i-1] - 1
        for j in range(max_size):
            num = []
            for row in inputs[:-1]:
                num.append(row[splitters[i-1]+1+j])
            nums.append(int("".join(num)))

        # Perform operation on numbers.
        char = operations[i-1]
        if char == "+":
            total += sum(nums)
        else:
            total += prod(nums)
            
    return total

print(part1(example))
print(part1(inputs))
print(part2(example))
print(part2(inputs))
