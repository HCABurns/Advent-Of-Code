import API

inputs = API.get_input()

# Part 1
def part1(inputs):
    ids = 0
    for r in inputs:
        l, r = map(int,r.split("-"))
        for i in range(l,r+1):
            i = str(i)
            if len(i) % 2 :
                continue
            v1,v2 = i[:len(i)//2], i[len(i)//2:]
            if v1 == v2:
                ids += int(i)
    return ids

# Part 2
def part2(inputs):
    ids = 0
    for r in inputs:
        l, r = map(int,r.split("-"))

        for i in range(l,r+1):
            i = str(i)
        
            for j in range(1,len(i)//2+1):
                v1 = i[:j]
                new_id = v1 * (len(i) // j)
                if str(new_id) == i:
                    ids += int(i)
                    break
    return ids

print(part1(inputs))
print(part2(inputs))
