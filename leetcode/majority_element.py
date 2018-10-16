
'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2

'''

# Dictionary approach - O(n) time, O(n) space
def majorityElement(self, nums):
	d = {}
	for item in nums:
	    if item in d:
	        d[item] += 1
	    else:
	        d[item] = 1

	max_val = max_key = -1
	for key, value in d.items():
	    if value > (len(nums) // 2):
	        return key
