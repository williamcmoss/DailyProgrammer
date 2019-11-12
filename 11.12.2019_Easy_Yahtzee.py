
def yahtzee_upper(roll):
    nums = {}
    for num in roll:
        if num in nums:
            nums[num]+=num
        else:
            nums[num]=num
    return max(nums.values())
print(yahtzee_upper([1, 1, 1, 1, 3]))
