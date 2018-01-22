def add_for(nums):
    total = 0
    for i in nums:
        total += i

    return total


def add_while(nums):
    total = 0
    i = 0
    while i < len(nums):
        total += nums[i]
        i += 1

    return total
