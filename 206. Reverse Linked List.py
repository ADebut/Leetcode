# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        node = head
        while(node):
            temp = node.next
            node.next = pre
            pre = node
            node = temp
        return pre
            