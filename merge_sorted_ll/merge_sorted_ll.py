# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 and not l2:
            return l1
        if l2 and not l1:
            return l2
        if not l1 and not l2:
            return None
        
        h1 = l1
        h2 = l2
        
        if h1.val < h2.val:
            l = ListNode(h1.val)
            h1 = h1.next
        else:
            l = ListNode(h2.val)
            h2 = h2.next
        
        h = l #the head of new list to be returned
        
        while h1 and h2:
            if h1.val < h2.val:
                l.next = ListNode(h1.val)
                h1 = h1.next
            else:
                l.next = ListNode(h2.val)
                h2 = h2.next
            l = l.next
        
        if h1:
            l.next = h1
        if h2:
            l.next = h2
            
        return h
