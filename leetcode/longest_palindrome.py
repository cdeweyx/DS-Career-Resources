
'''
409. Longest Palindrome

Given a string which consists of lowercase or uppercase letters, find the length of 
the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.

'''

# Dictionary approach - O(n) time, O(n) space
def longestPalindrome(self, s):
    d = {}
    for char in s:
        if char in d:
            d[char] += 1
        else:
            d[char] = 1
    
    result, extra = 0, 0
    for key, value in d.items():
        if value % 2 == 0:
            result += value
        else: 
            result += value - 1
            extra = 1
    return result + extra