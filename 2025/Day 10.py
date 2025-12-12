import API
import heapq
from z3 import *
from math import ceil

example = API.get_example()
inputs = API.get_input()

# Part 1.
def part1(inputs):
    total_presses = 0
    for row in inputs: 
        # Parse input.
        indicator, *config, _ = row.split(" ")
        indicator = indicator[1:-1]
        config = [[*map(int,con[1:-1].split(","))] for con in config]

        min_presses = 1e9
        heap = []
        heapq.heappush(heap, [0, sum(1<<i for i in range(len(indicator))), 0]) # presses, Unlit lights, indicator status
        goal = 0
        for i,char in enumerate(indicator):
            goal += (1 << i) if char == "#" else 0
        
        cache = set()
        while heap:
            presses, remaining, status = heapq.heappop(heap)

            if remaining == 0:
                min_presses = min(min_presses,presses)
                break
            
            if status in cache:
                continue
            cache.add(status)
            
            # Sim the button presses.
            for buttons in config:
                temp = copy.deepcopy(status)
                for button in buttons:
                    temp ^= (1 << button)
                heapq.heappush(heap, [presses+1, sum((temp >> i)&1 != 1&(goal >> i) for i in range(len(indicator))) , temp])
        total_presses += min_presses
    return total_presses

def part2(inputs):
    total_presses = 0
    for row in inputs: 
        _, *config, joltage = row.split(" ")
        config = [[*map(int, con[1:-1].split(","))] for con in config]
        goal = list(map(int, joltage[1:-1].split(",")))

        # Z3 solver for linear algebra.
        s = Optimize()

        # Add buttons.
        buttons = [Int(chr(ord('a')+i)) for i in range(len(config))]
        for b in buttons:
            s.add(b >= 0)

        # Add button pressing constraints.
        for i, v in enumerate(goal):
            contributors = [buttons[j] for j, cfg in enumerate(config) if i in cfg]
            s.add(Sum(contributors) == v)

        # Minimize total presses.
        s.minimize(Sum(buttons))

        # Get the minimum number of presses.
        if s.check() == sat:
            model = s.model()
            total_presses += sum(model[b].as_long() for b in buttons)
        
    return total_presses


print(part1(inputs))
print(part2(inputs))
