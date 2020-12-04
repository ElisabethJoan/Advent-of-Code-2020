from aoc2020lib import digestInput

input = digestInput("day3input.txt")
treeDelim = "#"


def solution(slope):
    treeCount = 0
    for i in range(1, len(slope)):
        if slope[i][(3 * i) % len(slope[0])] == treeDelim:
            treeCount += 1
    return treeCount


x = solution(input)
print(x)