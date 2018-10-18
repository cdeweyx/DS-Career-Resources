
'''
152. Maximum Product Subarray

Given an integer array nums, find the contiguous subarray within an array (containing at least one number) 
which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

'''

# Kandane's with a twist - O(n) time, O(1) space --> WRONG
def maxProduct(self, nums):
	count_neg = 0
	if not nums: 
		return 0

	for item in nums:
		if item < 0:
			count_neg += 1

	if count_neg % 2 == 0: 
		result = 1
		for item in nums:
			result *= item
		return result
	else: 
		curr_max = nums[0]
		total_max = nums[0]

		for item in nums[1:]:
			curr_max = max(i, i * curr_max)
			total_max = max(total_max, curr_max)
		return total_max


# Correct answer - O(n) time, O(1) space
def maxProduct(self, nums):
    min_temp = nums[0]
    max_temp = nums[0]
    total_max = nums[0]
    for i in range(1, len(nums)):
        min_temp, max_temp = min(nums[i], nums[i] * max_temp, nums[i] * min_temp), max(nums[i], 
        	nums[i] * max_temp, nums[i] * min_temp)
        total_max = max(total_max, max_temp)
    return total_max



