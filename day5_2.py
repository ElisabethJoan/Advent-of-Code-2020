from aoc2020lib import digestInput

input = digestInput("day5input.txt")

def B(list):
    return list[len(list)//2:]

def F(list):
    return list[:len(list)//2]

def find_missing(list): 
    return [x for x in range(list[0], list[-1]+1) if x not in list]

options = {
    "F" : F,
    "B" : B,
    "L" : F,
    "R" : B
}

def solution(input):
    res = []
    for i in input:
        row = list(range(128))
        col = list(range(8))
        for j in i:
            if j == "F" or j == "B":
                row = options[j](row)
            else:
                col = options[j](col)
        sol = row[0] * 8 + col[0]
        res.append(sol)
    return res

x = solution(input)
x.sort()
y = find_missing(x)
print(y)