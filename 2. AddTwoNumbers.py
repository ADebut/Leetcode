# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        L = ListNode(l1.val + l2.val)
        c = 0
        if L.val >= 10:
            c += 1
            L.val = L.val % 10
        if l1.next != None and l2.next != None:
            if c == 1:
                l1.next.val += 1
            L.next = self.addTwoNumbers(l1.next, l2.next)

                    
        if l1.next == None and l2.next != None:
            l1.next = ListNode(0)
            if c == 1:
                l1.next.val += 1
            L.next = self.addTwoNumbers(l1.next, l2.next)

        if l1.next != None and l2.next == None:
            l2.next = ListNode(0)
            if c == 1:
                l1.next.val += 1
            L.next = self.addTwoNumbers(l1.next, l2.next)

        if l1.next == None and l2.next == None and c == 1:
            l1.next = ListNode(0)
            l2.next = ListNode(0)
            if c == 1:
                l1.next.val += 1
            L.next = self.addTwoNumbers(l1.next, l2.next)

        return L