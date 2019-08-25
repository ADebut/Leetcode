# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        point = dummy
        while (point.next != None and point.next.next != None):
            swap1 = point.next
            swap2 = point.next.next
            point.next = swap2
            swap1.next = swap2.next
            swap2.next = swap1
            point = swap1
        return dummy.next