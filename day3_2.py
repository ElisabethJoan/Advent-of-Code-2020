from aoc2020lib import digestInput
from day3_1 import solution as problem1


input = digestInput("day3input.txt")
treeDelim = "#"

def solution():
    prod = 1
    for i in range(1, 6):
        prod *= problem1(input, ((i * 2) - 1) % 8, 1 + (1 * (i > 4)))
    return prod

        
x = solution()
print(x)