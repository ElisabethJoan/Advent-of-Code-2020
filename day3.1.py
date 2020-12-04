from aoc2020lib import digestInput

input = digestInput("day3input.txt")
treeDelim = "#"


def solution():
    treeCount = 0
    for i in range(1, len(input)):
        if input[i][(3 * i) % len(input[0])] == treeDelim:
            treeCount += 1
    return treeCount


x = solution()
print(x)