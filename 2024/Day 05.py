import API
from collections import defaultdict

example = API.get_example()
inputs = API.get_input()


def part1(inputs):
    # Parse Input
    order = defaultdict(set)
    i = 0
    while inputs[i] != "":
        l , r = map(int,inputs[i].split("|"))
        i+=1
        order[l].add(r)
    
    total = 0
    i+=1
    while i < len(inputs):
        numbers = list(map(int, inputs[i].split(",")))
        i+=1
        valid = True
        for j,val in enumerate(numbers[:-1]):
            if not valid:
                break
            for val2 in numbers[j+1:]:
                if val in order[val2]:
                    valid = False
                    break
        if valid:
            total += numbers[len(numbers) // 2]

    while i < len(inputs):
        numbers = list(map(int, inputs[i].split(",")))
        i+=1
        valid = True
        for j,val in enumerate(numbers[:-1]):
            if not valid:
                break
            for val2 in numbers[j+1:]:
                if val in order[val2]:
                    valid = False
                    break
        if valid:
            total += numbers[len(numbers) // 2]

    return total

def part2(inputs):
    order = defaultdict(set)
    i = 0
    while inputs[i] != "":
        l , r = map(int,inputs[i].split("|"))
        i+=1
        order[l].add(r)
    
    total = 0
    i+=1
    while i < len(inputs):
        numbers = list(map(int, inputs[i].split(",")))
        i+=1
        valid = False
        while not valid:
            valid = True
            for j,val in enumerate(numbers[:-1]):
                if not valid:
                    break
                for k,val2 in enumerate(numbers[j+1:], start = j+1):
                    if val in order[val2]:
                        numbers[j],numbers[k] = numbers[k], numbers[j]
                        valid = False
                        break
            if valid:
                total += numbers[len(numbers) // 2]

    return total

print(v1:=part1(example))
print(v2:=part1(inputs))
print(part2(example) - v1)
print(part2(inputs) - v2)
