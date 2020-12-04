from aoc2020lib import digestInput

input = [int(x) for x in digestInput("day1input.txt")]
target = 2020


def solution(nums, target):
    dict = {}
    for i in range(len(nums)):
        if target - nums[i] in dict and dict[target - nums[i]] != i:
            return (target - nums[i]) * nums[i]
        dict[nums[i]] = i


x = solution(input, target)
print(x)
