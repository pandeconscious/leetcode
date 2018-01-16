# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k <= 0:
            return head
        if head:
            temp = head
            count = 1
            while temp.next:
                count += 1
                temp = temp.next
            
            i = 0
            
            left_head, left_tail = None,  None
            while count - i >= k:
                rt_head, rt_tail = None, head 
                for _ in range(k):
                    temp = rt_head
                    rt_head = head
                    head = head.next
                    rt_head.next = temp
                
                if left_head == None:
                    left_head = rt_head
                
                if left_tail:
                    left_tail.next = rt_head
                left_tail = rt_tail
                
                i += k
            
            if head and left_head:
                rt_tail.next = head
            if left_head == None:
                return head
            else:
                return left_head
