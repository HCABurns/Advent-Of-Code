import API

inputs = API.get_input()

# Part 1
total = 0
for i in inputs:
    vals = list(map(int,i.split(" ")))

    increase = True
    decrease = True

    #Decreasing
    for j in range(1,len(vals)):
        if vals[j] >= vals[j-1]:
            decrease = False

    #Increase
    for j in range(1,len(vals)):
        if vals[j] <= vals[j-1]:
            increase = False
            break
    
    if increase == True or decrease == True :
        valid = True
        v_b = [i for i in vals]
        vals.sort()
        for j in range(1, len(vals)):
            if vals[j] - vals[j-1] > 3 or vals[j] - vals[j-1] < 1:
                valid = False
                break
        if valid:
            total += 1
print(total)


# Part 2
total = 0
for i in inputs:
    v = list(map(int,i.split(" ")))

    ignore = 0
    for _ in range(len(v)):
        vals = v[:ignore] + v[ignore+1:]
        ignore += 1
        increase = True
        decrease = True
        dec_count = 0
        inc_count = 0

        #Decreasing
        for j in range(1,len(vals)):
            if vals[j] >= vals[j-1]:
                decrease = False

        #Increase
        for j in range(1,len(vals)):
            if vals[j] <= vals[j-1]:
                increase = False
                break
        
        if increase == True or decrease == True :
            valid = True
            v_b = [i for i in vals]
            vals.sort()
            for j in range(1, len(vals)):
                if vals[j] - vals[j-1] > 3 or vals[j] - vals[j-1] < 1:
                    valid = False
                    break
            if valid:
                total += 1
                break
print(total)
