
'''
20. Valid Parenthesis 

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}["
Output: true

'''

# Stack approach - O(n) time, O(n) space
def isValid(self, s):
    def isValid(self, s):
        d = {'{':'}', '(':')', '[':']'}
        stack = []
        for c in s:
            if c in d:
                stack.append(c)
            elif len(stack) == 0 or c != d[stack.pop()]:
                return False
        return len(stack) == 0





