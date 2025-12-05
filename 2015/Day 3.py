import API

inputs = API.get_input()

# Part 1
seen = set()
seen.add((0,0))
i = j = 0
moves = {a:b for a,b in zip("^>v<",[(0,1),(1,0),(0,-1),(-1,0)])}
for char in inputs:
    a,b = moves[char]
    i += a
    j += b
    seen.add((i,j))
print(len(seen))

# Part 2
seen = set()
seen.add((0,0))
i = j = 0
moves = {a:b for a,b in zip("^>v<",[(0,1),(1,0),(0,-1),(-1,0)])}
for i,j,movements in [[0,0,inputs[::2]],[0,0,inputs[1::2]]]:
    for char in movements:
        a,b = moves[char]
        i += a
        j += b
        seen.add((i,j))
print(len(seen))
