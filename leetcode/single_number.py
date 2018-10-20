
'''
136. Single Number

Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:
Input: [2,2,1]
Output: 1

Example 2:
Input: [4,1,2,1,2]
Output: 4

'''

# Dictionary approach - O(n) time, O(n) space
def singleNumber(self, nums):
	d = {}
	for item in nums:
		if item in d:
			d[item] += 1
		else: 
			d[item] = 1

	for key, value in d.items():
		if value == 1:
			return key
