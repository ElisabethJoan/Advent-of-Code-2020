from aoc2020lib import digestInput

input = digestInput("day5input.txt")

def B(listt):
    return listt[len(listt)//2:]

def F(listt):
    return listt[:len(listt)//2]

options = {
    "F" : F,
    "B" : B,
    "L" : F,
    "R" : B
}

def solution(input):
    res = 0
    for i in input:
        row = list(range(128))
        col = list(range(8))
        for j in i:
            if j == "F" or j == "B":
                row = options[j](row)
                # print(j)
                # print(row)
            else:
                col = options[j](col)
        # break
        sol = row[0] * 8 + col[0]
        if sol > res:
            res = sol
    return res

x = solution(input)
print(x)