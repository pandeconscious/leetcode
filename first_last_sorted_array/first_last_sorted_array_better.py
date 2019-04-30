LARGENUM = 99999999999999
SMALLNUM = -99999999999999

class Solution(object):
    def searchIndex(self, beg, end, target, leftmost = True):
        """
        searches either leftmost or right most 
        indices based on the bool leftmost
        """
        if end < beg:
            return
        m = (beg+end)/2
        if self.nums[m] == target:
            if leftmost:
                self.l = min(self.l, m)
                self.searchIndex(beg, m-1, target, leftmost)
            else:
                self.r = max(self.r, m)
                self.searchIndex(m+1, end, target, leftmost)
        elif self.nums[m] > target:
            self.searchIndex(beg, m-1, target, leftmost)
        else:
            self.searchIndex(m+1, end, target, leftmost)
                
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        self.nums = nums
        self.l = LARGENUM
        self.searchIndex(0, len(nums)-1, target, True)
        if self.l == LARGENUM:
            return [-1, -1]
        self.r = SMALLNUM
        self.searchIndex(0, len(nums)-1, target, False)
        return [self.l, self.r]
        
        
