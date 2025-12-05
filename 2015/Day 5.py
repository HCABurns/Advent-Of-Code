import API

inputs = API.get_input()

#Part 1
invalid = set(["ab","cd","pq","xy"])
vowels = set(i for i in "aeiou")
nice = 0

for word in inputs:
    v_count = sum(1 for i in word if i in vowels)
    double = False
    forbidden = False
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            double = True
        elif word[i]+word[i+1] in invalid:
            forbidden = True
            break
        
    if v_count >= 3 and double and not forbidden:
        nice += 1
print(nice)


#Part 2
invalid = set(["ab","cd","pq","xy"])
vowels = set(i for i in "aeiou")
nice = 0

for word in inputs:
    repeating = False
    rule1 = False
    seen = set()
    for i in range(0,len(word)-2):
        if word[i] == word[i+2]:
            repeating = True
            break
    
    seen = set()
    for i in range(0,len(word)-3):
        duo = word[i] + word[i+1]
        for j in range(i+2, len(word)-1):
            duo2 = word[j] + word[j+1]
            if duo == duo2:
                rule1 = True
                break
        
    if repeating and rule1:
        nice += 1
print(nice)
