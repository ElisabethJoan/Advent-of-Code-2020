from aoc2020lib import digestInput, printClass, processInput, Password

input = digestInput("day2input.txt")


def solution():
    counter = 0
    passwords = processInput(input)
    for password in passwords:
        if (password.password[password.bounds[0]-1] == password.ruleChar) != (password.password[password.bounds[1]-1] == password.ruleChar):
            counter += 1
    return counter


x = solution()
print(x)