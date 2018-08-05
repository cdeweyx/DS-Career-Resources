
'''
53. Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

'''

# Kadane's Algorithm - O(n) time, O(1) space
    def maxSubArray(self, nums):
        total_max = nums[0]
        current_max = nums[0]
        for i in nums[1:]:
            current_max = max(i, current_max + i)
            total_max = max(total_max, current_max)
        return total_max