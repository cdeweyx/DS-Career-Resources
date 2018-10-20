
'''
5. Longest Palindromic Substring

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: "cbbd"
Output: "bb"

'''

# Brute force approach - O(n) time, O(n) space
def longestPalindrome(self, s):
	longest_str = ''
	for i in range(len(s)):
		for j in range(i, len(s) + 1):
			temp = s[s:j]
			if temp == temp[::-1] and len(temp) > len(longest_str):
				longest_str = temp
				print(temp)