nums = [1, 5, 6, 2, 4, 3]
for num in nums:
    for i in range(len(nums)):
        if not i + 1 == len(nums) and nums[i] > nums[i + 1]: 
            nums[i], nums[i+1] = nums[i+1], nums[i]
print(nums)