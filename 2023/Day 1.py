import API

inputs = API.get_input()

# Part 1
total = 0
for s in inputs.split("\n"):
    f = [i for i in s if i.isdigit()]
    total += int(f[0] + f[-1])
print(total)

# Part 2
o = "one two three four five six seven eight nine".split(" ")#[::-1]
f = "1 2 3 4 5 6 7 8 9".split()#[::-1]
trans = {str(i):j for i,j in zip(o,f)}
total = 0

for s in inputs.split("\n"):
    nums = []
    i = 0
    while i < len(s):
        char = s[i]
        if char.isnumeric():
            nums.append(char)
        else:
            for idx,word in enumerate(o):
                if len(word)+i <= len(s) and s[i:i+len(word)] == word:
                    nums.append(trans[word])
        i+=1
    total += int(nums[0]+nums[-1])
print(total)
