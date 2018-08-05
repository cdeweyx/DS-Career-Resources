''' 
Two Sum #1

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1]. 

'''

# Naive approach - O(n^2) time, O(1) space
def twoSum(self, nums, target):
	for i in range(nums):
		for j in range(nums):

			if nums[i] + nums[j] == target and i != j:
				return i, j
	return -1


# Set approach - O(n) time, O(n) space
def twoSum(self, nums, target):
    num_dict = {}
    for i in range(len(nums)):
        if target - nums[i] in num_dict:
            return num_dict.get(target - nums[i]), i
        num_dict[nums[i]] = i
    return -1