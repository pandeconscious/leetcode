# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def __insert(self, head, temp):
        if temp.val < head.val:
            temp.next = head
            return temp
        else:
            prev = head
            curr = head.next
            found = False
            while curr:
                if temp.val < curr.val:
                    prev.next = temp
                    temp.next = curr
                    found = True
                    break
                else:
                    prev = curr
                    curr = curr.next
            if not found:
                prev.next = temp
            return head
            
    
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head:
            curr = head.next
            head.next = None
            while curr:
                temp = curr
                curr = curr.next
                temp.next = None
                head = self.__insert(head, temp)
            return head
                
