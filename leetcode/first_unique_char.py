
'''
387. First Unique Character in a String

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.

'''

# Dictionary Approach - O(n) time, O(n) space
def firstUniqChar(self, s):
	seen = {}
	for item in s:
		if item not in seen:
			seen[item] = 1
		else:
			seen[item] += 1

	for i in range(len(s)):
		item = s[i]
		if seen[item] == 1:
			return i
	return -1


