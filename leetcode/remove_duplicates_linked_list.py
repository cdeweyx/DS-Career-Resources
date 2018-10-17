
'''

83. Remove Duplicates from Sorted List

Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3

'''

# Standard approach - O(n) time, O(n) space
def deleteDuplicates(self, head):
	curr = head
	while curr and curr.next:
		if curr.val == curr.next.val:
			curr.next = curr.next.next
		else:
			curr = curr.next

	return head


