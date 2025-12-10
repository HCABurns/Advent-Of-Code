import API
import heapq

example = API.get_example()
inputs = API.get_input()


def part1(inputs):
    total_presses = 0
    for row in inputs: 
        # Parse input.
        indicator, *config, _ = row.split(" ")
        indicator = indicator[1:-1]
        config = [[*map(int,con[1:-1].split(","))] for con in config]

        # Define goal state.
        goal = 0
        for i,char in enumerate(indicator):
            goal += (1 << i) if char == "#" else 0
          
        min_presses = 1e9
        heap = []
        heapq.heappush(heap, [0, sum(1<<i for i in range(len(indicator))), 0]) # Unlit lights, presses, presses neg, indicator status
        cache = set()
        while heap:
            presses, remaining, status = heapq.heappop(heap)

            # If matches the lights, store and end.
            if remaining == 0:
                min_presses = presses
                break
            # Check cache if this status has been seen or not - Continue if new.
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

print(part1(example))
print(part1(inputs))
