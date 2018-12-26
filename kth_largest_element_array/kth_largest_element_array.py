from collections import Counter
import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        counter_dic = Counter(nums)
        #negating since heapq makes min heap and not max heap
        vals = [-v for v in counter_dic.iterkeys()]
        heapq.heapify(vals)
        
        found = 0
        while found < k:
            val = heapq.heappop(vals)
            found += counter_dic[-val]
        return -val
