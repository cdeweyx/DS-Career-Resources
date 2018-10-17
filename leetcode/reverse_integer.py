
'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321

Example 3:

Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit 
signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your 
function returns 0 when the reversed integer overflows.

'''

# Pythonic solution - O(n) time, O(n) space
def reverse(self, x):
    if x > 0:
        sign = 1
    else: 
        sign = -1
    result = int(str(abs(x))[::-1]) * sign
    return result if result > -(2**31) and result < (2**31) else 0



