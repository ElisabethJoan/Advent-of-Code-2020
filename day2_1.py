from aoc2020lib import digestInput, printClass, processInput, Password

input = digestInput("day2input.txt")


def solution():
    counter = 0
    passwords = processInput(input)
    for password in passwords:
        count = password.password.count(password.ruleChar)
        # if count in password.range:
        if count >= password.bounds[0] and count <= password.bounds[1]:
            counter += 1
    return counter


x = solution()
print(x)