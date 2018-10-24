
'''
258. Add Digits

Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:
Input: 38
Output: 2 
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?

'''

# Initial approach - O(n) time, O(n) space
def addDigits(self, num):
	digits = [int(x) for x in str(num)]
		while sum(digits) > 9:
			temp = sum(digits) 
			digits = [int(x) for x in str(temp)]
		return sum(digits)


# More concise approach - O(n) time, O(n) space
def addDigits(self, num):
    while num > 9:
        num = sum(list(map(int, str(num))))
    return num

 