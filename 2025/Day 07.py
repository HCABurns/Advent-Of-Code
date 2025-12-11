import API
from collections import deque

grid = API.get_input()

# Part 1.
def part1(inputs):
    # Define required sets, start location and queue.
    seen = set()
    start = (0,inputs[0].index("S"))
    queue = deque([start])
    splits = set()

    # Simulate the tacheon bean meeting splitters.
    h = len(inputs)
    w = len(inputs[0])
    while queue:
        # Get position.
        i,j = queue.popleft()

        # Ensure not at the bottom and not seen location before.
        if (i,j) in seen or i == h-1:
            continue
        seen.add((i,j))

        # If splitter reached, add to set and split beam left and right.
        if inputs[i][j] == "^":
            splits.add((i,j))
            if j-1 >= 0: queue.append([i,j-1])
            if j+1 < w: queue.append([i,j+1])
        else:
            # Move beam down.
            queue.append([i+1,j])
    
    return len(splits)


# Part 2 - With memoization.
cache = {}
def part2(i, j):
    # If bottom of the grid, return 1 path.
    if i == len(grid):
        return 1

    # If position is cached, return the number of routes possible from that location.
    if (i,j) in cache:
        return cache[(i,j)]

    # Store number of paths.
    paths = 0

    # Recursive search paths splitting left and right on splitters.
    if grid[i][j] == "^":
        if j > 0:
            paths += part2(i, j-1)
        if j < len(grid[0])-1:
            paths += part2(i, j+1)
    else:
        paths += part2(i+1, j)
    # Cache number of paths possible from this location.
    cache[(i,j)] = paths
    return paths

# Print results.
print(part1(grid))
print(part2(0,grid[0].index("S")))
