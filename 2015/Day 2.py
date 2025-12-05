import API

inputs = API.get_input()

# Part 1
total = 0
for i in inputs:
    l,w,h = map(int,i.split("x"))

    total += (2*l*w) + (2*w*h) + (2*h*l) + min(l*w,w*h,h*l)
    
print(total)

# Part 2
total = 0
for i in inputs:
    l,w,h = map(int,i.split("x"))

    total += (l*w*h) + min(l*2+w*2,w*2+2*h,h*2+2*l)
print(total)
