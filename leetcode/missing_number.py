
'''
268. Missing Number

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

'''

# Store values - O(n) time, O(n) space
def missingNumber(self, nums):
    max_num = -1
    seen = set()

    for item in nums:
        seen.add(item)
        if item > max_num:
            max_num = item

    for i in range(max_num):
        if i not in seen:
            return i
    return max_num + 1


# Sort values - O(nlogn) time, O(1) space
def missingNumber(self, nums):
    if len(nums) == 0: return 0
    nums.sort()
    for i in range(nums):
        if nums[i] != i:
            return nums[i] - 1
    return nums[-1] + 1
