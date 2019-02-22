# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def get_len(self, node):
        n = 0
        while node:
            n += 1
            node = node.next
        return n
    
    def merge(self, head, head2):
        if not head:
            return head2
        if not head2:
            return head
        
        new_head = None
        if head2.val < head.val:
            new_head = head2
            head2 = head2.next
        else:
            new_head = head
            head = head.next
        to_return = new_head
        
        while head and head2:
            if head2.val < head.val:
                new_head.next = head2
                head2 = head2.next
            else:
                new_head.next = head
                head = head.next
            new_head = new_head.next
        
        if head:
            new_head.next = head
        else:
            new_head.next = head2
        
        return to_return
    
    def merge_sort(self, head, n):
        if not head:
            return
        if n == 1:
            return head
        mid = (n-1)/2
        temp = head
        i = 0
        while i < mid:
            temp = temp.next
            i += 1
        head2 = temp.next
        temp.next = None
        left_sort = self.merge_sort(head, mid+1)
        right_sort = self.merge_sort(head2, n-1-mid)
        return self.merge(left_sort, right_sort)
        
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        n = self.get_len(head)
        return self.merge_sort(head, n)
        
