
'''
125. Valid Palindrome

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true

Example 2:

Input: "race a car"
Output: false

'''

# Simplest, Pythonic Approach - O(n) time, O(1) space
def isPalindrome(self, s):
    s = [i.lower() for i in s if i.isalnum()]
    return s == s[::-1]