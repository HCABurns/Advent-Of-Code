import API

inputs = API.get_input()

# Part 1
print(inputs.count("(")-inputs.count(")"))

# Part 2
pos = 0
i = 0
while pos != -1:
    if inputs[i] == ")":
        pos -= 1
    else:
        pos += 1
    i+=1
print(i)
