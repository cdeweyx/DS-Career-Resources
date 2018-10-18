
'''
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.

'''

# Initial approach - O(n*i) time, O(n) space
def longestCommonPrefix(self, strs):
    if (len(strs) == 0): return ''
    prefix = strs[0]
    for item in strs[1:]:
        if len(item) < len(prefix):
            prefix = item

    for item in strs:
        for i in range(len(prefix)):
            if item[i] != prefix[i]:
                prefix = prefix[:i]
                break
    
    return prefix
