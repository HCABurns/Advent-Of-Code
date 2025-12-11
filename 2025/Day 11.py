import API
from collections import deque

inputs = API.get_input()

# Part 1.
def part1(inputs):
    # Form DAC graph.
    graph = {}
    for node in inputs:
        name, connects = node.split(":")
        graph[name] = connects.strip().split(" ")
    
    # BFS from "you" to "out" counting the number of paths.
    # (No visited list as there is no loops)
    queue = deque(["you"]) 
    paths = 0
    goal = "out"
    while queue:
        node = queue.popleft()
        if node == goal:
            paths += 1
            continue

        for next in graph[node]:
            queue.append(next)
    return paths


def part2(inputs):
    # Form DAC graph.
    graph = {}
    for node in inputs:
        name, connects = node.split(":")
        graph[name] = connects.strip().split(" ")
    
    # DFS from "svr" to "out" going through "fft" and "dac" with memoization.
    cache = {}
    def dfs(name, visited):
        # Goal state reached - Return 1 if visited both goals otherwise 0
        if name == "out":
            return 1 if visited == 2 else 0
        
        # Check if result is cached and return if so.
        if (name ,visited) in cache:
            return cache[(name,visited)]

        # DFS increasing visited if goal node are found.
        paths_total = 0
        for next in graph[name]:
            if next == "fft":
                paths_total += dfs(next, visited+1)
            elif next == "dac":
                paths_total += dfs(next, visited+1)
            else:
                paths_total += dfs(next, visited)
        cache[(name,visited)] = paths_total
        return paths_total
    return dfs("svr",0)

# Print results.
print(part1(inputs))
print(part2(inputs))
