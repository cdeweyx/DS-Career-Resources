
'''
21. Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new list. The new list should be made by 
splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

'''

# Two Pointer Approach - O(n) time, O(n) space
def mergeTwoLists(self, l1, l2):
	result = currNode = ListNode(0)
	while l1 and l2:
		if l1.val > l2.val:
			currNode.next = l2
			l2 = l2.next 
		else:
			currNode.next = l1
			l1 = l1.next
		currNode = currNode.next
    currNode.next = l1 or l2
	return result.next

