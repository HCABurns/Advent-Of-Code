import API

import matplotlib.pyplot as plt
from itertools import combinations

example = API.get_example()
inputs = API.get_input()

"""
Visualiser tool to help with understanding the structure of the inputs.
"""
def visualise(reds):
    xpoints = [i[0] for i in reds]+[reds[0][0]]
    ypoints = [i[1] for i in reds]+[reds[0][1]]
    plt.plot(xpoints, ypoints)
    plt.gca().invert_yaxis()
    plt.show()


# Part 1.
def part1(inputs):
    # Parse red corners.
    reds = [[*map(int, row.split(","))] for row in inputs]
    # Find max size and return.
    size = 0
    for i,red in enumerate(reds[:-1]):
        for red2 in reds[i+1:]:
            size = max(size,abs(red[0]-red2[0] + 1) * abs(red[1]-red2[1]+1))
    return size


def part2(inputs):
    # Parse red corners and pair corners together..
    reds = [[*map(int, row.split(","))] for row in inputs]
    pairs = [(a,b) for a,b in zip(reds, reds[1:]+[reds[0]])]

    # Find vertical and horizontal edges.
    vertical = [[x1, min(y1,y2),max(y1,y2)] for (x1,y1),(x2,y2) in pairs if x1 == x2]
    horizontal = [[y1, min(x1,x2),max(x1,x2)] for (x1,y1),(x2,y2) in pairs if y1 == y2]

    # find max area between corners.
    max_area = -1
    for (x1,y1),(x2,y2) in combinations(reds, 2):
        # Calculate area and skip if it isn't larger than highest area.
        area = ((abs(x1 - x2)+1) * (abs(y1 - y2)+1))
        if area < max_area:
            continue

        # Order coordinates x1,y1 is left and top most, x2,y2 is right and bottom most.
        x1 , y1 , x2 , y2 = min(x1,x2), min(y1,y2) , max(x1,x2), max(y1,y2)

        # Check if any edges are inside the rectangle
        valid = True
        for x,ymin,ymax in vertical:
            if x1 < x < x2 and ymax > y1 and ymin < y2:
                valid = False
                break
        else:
            for y,xmin,xmax in horizontal:
                if y1 < y < y2 and xmax > x1 and xmin < x2:
                    valid = False
                    break     
        if valid:
            max_area = area

    return max_area

print("Part 1:")
print(part1(example))
print(part1(inputs))

print("\nPart 2:")
print(part2(example))
print(part2(inputs))
