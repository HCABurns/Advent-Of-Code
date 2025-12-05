import API

example = API.get_example()
inputs = API.get_input()

# Part 1
def part1(inputs):
    ranges = []
    blocker = inputs.index("")
    for i in range(blocker):
        l , r = map(int, inputs[i].split("-"))
        ranges.append([l,r])
    fresh = 0
    for val in range(blocker+1,len(inputs)):
        val = int(inputs[val])
        for l , r in ranges:
            if l <= val <= r:
                fresh+=1
                break
    return fresh


# Part 2
def part2(inputs):
    ranges = []
    blocker = inputs.index("")

    for i in range(blocker):
        l , r = map(int, inputs[i].split("-"))
        ranges.append([l,r])

    ranges.sort()
    new = []
    for l , r in ranges:
        if not new or new[-1][1] < l:
            new.append([l,r])
        else:
            new[-1][1] = max(new[-1][1], r)
    return sum(r-l+1 for l , r in new)

print(part1(example))
print(part1(inputs))
print(part2(example))
print(part2(inputs))
