from aoc2020lib import digestInput

input = digestInput("day6input.txt")


def solution(input):
    res = 0
    counter = 0
    temp = []
    input.append("")
    for i in input:

        if i == "":
            tempdict = {i:temp.count(i) for i in temp}
            temp = [k for k, v in tempdict.items() if v == counter]
            res += len(temp)
            counter = 0
            temp = []
        else:
            counter += 1
            temp.extend(i)
    return res

x = solution(input)
print(x)