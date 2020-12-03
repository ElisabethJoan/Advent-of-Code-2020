from aoc2020lib import digestInput

input = digestInput("day1input.txt")
target = 2020


def solution(nums, target):
    nums.sort()
    for i in range(len(nums) - 1):
        left = i + 1
        right = len(nums) - 1

        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum == target:
                return nums[i] * nums[left] * nums[right]
            elif sum > target:
                right -= 1
            else:
                left += 1


x = solution(input, target)
print(x)
