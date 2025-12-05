import API

inputs = API.get_input()

# Part 1
difference = 0
left = []
right = []
for i in inputs:
    l,r = map(int, i.split("   "))
    left += [l]
    right += [r]

for l,r in zip(sorted(left),sorted(right)):
    difference += abs(l-r)
print(difference)

# Part 2
left = set(left)
sim = 0
for i in list(left):
    sim += i * right.count(i)
print(sim)
