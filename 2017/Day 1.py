import API
inputs = API.get_input()

# Part 1
def part1(nums):
    code = 0
    for i in range(len(nums)):
        if nums[i] == nums[(i+1)%len(nums)]:
            code += int(nums[i])
    return code


# Part 2
def part2(nums):
    code = 0
    SIZE = len(nums) // 2
    for i in range(len(nums)):
        if nums[i] == nums[(i+SIZE)%len(nums)]:
            code += int(nums[i])
    return code

print(part1(inputs))
print(part2(inputs))
