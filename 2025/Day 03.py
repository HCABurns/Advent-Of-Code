import API

inputs = API.get_input()

# Part 1
def part1(inputs):
    total = 0
    for x in inputs:
        start = str(max([int(i) for i in x[:-1]]))
        idx = x.index(start)
        end = str(max([int(i) for i in x[idx+1:]]))
        val = int(start+str(end))
        total += val
    return total


#Part 2
def part2(inputs):
    total = 0
    for x in inputs:
        stack = []
        removed = 0
        for char in map(int, [i for i in x]):
            if not stack:
                stack.append(char)
            else:
                while len(x)-removed > 12 and stack and stack[-1] < char:
                    stack.pop()
                    removed += 1
                else:
                    stack.append(char)
        total += int("".join([str(i) for i in stack[:12]]))
    return total

print(part1(inputs))
print(part2(inputs))
