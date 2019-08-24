# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution: 
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        tail = new_list = ListNode(0)
        while l1 or l2:
            if l2 is None or (l1 and l1.val < l2.val):
                tail.next, l1 = l1, l1.next
            else:
                tail.next, l2 = l2, l2.next
            tail = tail.next
        return new_list.next