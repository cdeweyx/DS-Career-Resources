
'''
189. Rotate Array

Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
Note:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?

'''


# Brute Force Approach - O(n*k) time, O(1) space
def rotate(self, nums, k):
	temp, previous = 0, 0
	for i in range(k):
		previous = nums[-1]
		for j in range(len(nums)):
			temp = nums[j]
			nums[j] = previous
			previous = temp


# Using Extra Array - O(n) time, O(n) space
def rotate(self, nums, k):
	temp = []
	for i in range(len(nums)):
		temp.append(nums[(i + k + 1) % len(nums)])
	return temp[:]


# Reverse Solution - O(n) time, O(1) space
def rotate(self, nums, k):
    if k % len(nums) != 0:
        k = k % len(nums)
        nums[:] = nums[::-1][:k][::-1] + nums[::-1][k:][::-1]





