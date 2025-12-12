import API

example = API.get_example()
inputs = API.get_input()


def part1(inputs):
    patterns_number = 5
    patterns = []
    valid = 0
    for i in range(patterns_number):
        patterns += [[]]
        for row in range((patterns_number*i)+1,patterns_number*(1+i)-1):
            patterns[-1].append(inputs[row])

    for i in range(patterns_number*6,len(inputs)):
        l, r = inputs[i].split(":")
        w,h = map(int,l.split("x"))
        
        sum_val = sum(map(int,r.strip().split(" ")))

        # Only inputs that allow each shape a 3x3 area are valid.
        if (w//3)*(h//3) >= sum_val:
            valid += 1

    return valid

def part2(inputs):
    return "Decorate the Tree!"

print(part1(example))
print(part1(inputs))
print(part2(example))
print(part2(inputs))
