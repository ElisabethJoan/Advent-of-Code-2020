from aoc2020lib import digestInput

input = digestInput("day4input.txt")
requiredDelims = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
passports = []
temp = []

def processInput():
    coutner = 0
    tempDict = {}
    for i in range(len(input)):
        if input[i] == "" or i + 1 == len(input):
            passports.append(tempDict)
            if i + 1 == len(input):
                tempDict.update(dict(x.split(":") for x in input[i].split(" ")))
            tempDict = {}
            continue
        tempDict.update(dict(x.split(":") for x in input[i].split(" ")))

def solution():
    processInput()
    counter = 0
    for i in passports:
        if requiredDelims.issubset(i.keys()):
            counter += 1
    return counter


x = solution()
print(x)