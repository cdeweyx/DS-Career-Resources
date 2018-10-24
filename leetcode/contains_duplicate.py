
'''
127. Contains Duplicate

Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true

'''

# Normal approach - O(n) time, O(1) space
def containsDuplicate(self, nums):
	seen = set()
	for item in nums:
		if item in seen:
			return True
		else:
			seen.add(item)
	return False
