import re
import API

inputs = API.get_input()

# Part 1
total = 0
for i in re.findall(r"mul\([0-9]+,[0-9]+\)", inputs):
    l,r = i.replace("mul(","").replace(")","").split(",")
    total += int(r)*int(l)
print(total)


# Part 2
total = 0
for i in re.findall(r"mul\([0-9]+,[0-9]+\)", inputs):
    idx = inputs.index(i)
    dont = inputs[:idx].rfind("don't(")
    do = inputs[:idx].rfind("do(")
    if do >= dont:
        l,r = i.replace("mul(","").replace(")","").split(",")
        total += int(r)*int(l)
print(total)
