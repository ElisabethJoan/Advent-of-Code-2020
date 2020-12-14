from aoc2020lib import digestInput

input = digestInput("day6input.txt")


def solution(input):
    res = 0
    temp = []
    input.append("")
    for i in input:
        if i == "":
            setemp = set(temp)
            res += len(setemp)
            temp = []
        else:
            temp.extend(i)
    return res

x = solution(input)
print(x)