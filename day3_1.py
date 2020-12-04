from aoc2020lib import digestInput

input = digestInput("day3input.txt")
treeDelim = "#"


def solution(slope, x, y):
    treeCount = 0
    for i in range(1, len(slope)):
        try:
            if slope[i * y][(x * i) % len(slope[0])] == treeDelim:
                treeCount += 1
        except:
            return treeCount
    return treeCount


x = solution(input, 3, 1)
print(x)