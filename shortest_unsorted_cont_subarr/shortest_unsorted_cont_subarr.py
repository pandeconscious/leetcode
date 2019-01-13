import bisect
import operator
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        #not the most optimum solution - in fact a very bad solution
        #see better solution at: https://www.geeksforgeeks.org/minimum-length-unsorted-subarray-sorting-which-makes-the-complete-array-sorted/
        
        if not nums:
            return 0
        
        nums_ind = [(num,i) for i, num in enumerate(nums)]
        nums_sorted = sorted(nums_ind, key=operator.itemgetter(0))
        left_, right_ = 99999, -1
        for num, i in nums_ind:
            lt = bisect.bisect_left(nums_sorted, (num, i))
            rt = bisect.bisect_right(nums_sorted, (num, i))
            if not (i >= lt and i < rt):
                left_ = min(lt, left_)
                right_ = max(right_, rt)
                
        if right_ == -1:
            return 0
        return right_ - left_
