
'''
345. Reverse Vowels of a String

Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"

Example 2:
Input: "leetcode"
Output: "leotcede"

Note:
The vowels does not include the letter "y".

'''

# Initial approach - O(n) time, O(n) space
def reverseVowels(self, s):
    vowels = {'e', 'i', 'o', 'u', 'a', 'A', 'E', 'I', 'O', 'U'}
    vowel_stack = []
    for char in s:
        if char in vowels:
            vowel_stack.append(char)
    print(vowel_stack)
    s_list = list(s)
    for i in range(len(s_list)):
        if s_list[i] in vowels:
            s_list[i] = vowel_stack.pop()
                       
    return ''.join(s_list)


# Two pointer solution - O(n) time, O(n) space
def reverseVowels(self, s):
	vowels = [i for i in range(len(s)) if s[i] in 'aeiouAEIOU']
	s1 = list(s)
	for i in range(len(vowels)//2):
		s1[vowels[i]], s1[vowels[-i - 1]] = s1[vowels[-i - 1]], s1[vowels[i]]
		
	return ''.join(s1)


