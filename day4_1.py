from aoc2020lib import digestInput, d4processInput

input = digestInput("day4input.txt")
requiredDelims = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])


def solution():
    passports = d4processInput(input)
    counter = 0
    for i in passports:
        if requiredDelims.issubset(i.keys()):
            counter += 1
    return counter


x = solution()
print(x)