
'''
35. Search Insert Position

Given a sorted array and a target value, return the index if the target is found. If not, 
return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0

'''

# Naive approach - O(n) time, O(1) space
def searchInsert(self, nums, target):
	for i in range(len(nums)):
		if nums[i] == target:
			return i
		elif nums[i] > target:
			return i
	return len(nums) - 1


# Binary search approach - O(logn) time, O(1) space
def searchInsert(self, nums, target):
	low, high = 0, len(nums) - 1
	while low <= high:
		mid = (high + low) // 2
		if nums[mid] == target:
			return mid
		elif nums[mid] < target: 
			low = mid + 1
		else:
			high = mid - 1
	return low


