# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def reverse(head: ListNode):
            curHead = None
            while(head):
                nextNode = head.next
                head.next = curHead
                curHead = head
                head = nextNode
            return curHead
        
        
        if head == None:
            return None
        sub_head = head
        dummy = ListNode(0)
        dummy.next = head
        tail = dummy
        toNull = head
        while(sub_head):
            i = k
            while(i - 1 > 0):
                toNull = toNull.next
                if not toNull:
                    return dummy.next
                i = i - 1
            temp = toNull.next
            toNull.next = None
            new_sub_head = reverse(sub_head)
            tail.next = new_sub_head
            tail = sub_head
            sub_head = temp
            toNull = sub_head
            tail.next = sub_head
        return dummy.next
        