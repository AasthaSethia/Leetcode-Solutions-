# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = ListNode(None)
        prev = l3
        while (l1 != None and l2 != None):
            if (l1.val <= l2.val):
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next	
            prev = prev.next
        if l1 == None:
        	prev.next = l2
        elif l2 == None:
            prev.next = l1

        return l3.next
