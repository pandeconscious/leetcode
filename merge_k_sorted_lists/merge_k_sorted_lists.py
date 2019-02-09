# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwo(self, list1, list2):
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val < list2.val:
            list1.next = self.mergeTwo(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwo(list2.next, list1)
            return list2
    
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return
        n = len(lists)
        if n == 1:
            return lists[0]
        else:
            mid = n/2
            left = self.mergeKLists(lists[0:mid])
            right = self.mergeKLists(lists[mid:])
            return self.mergeTwo(left, right)
