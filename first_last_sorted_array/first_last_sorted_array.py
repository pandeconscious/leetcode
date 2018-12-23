#Find First and Last Position of Element in Sorted Array

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums:
            n = len(nums)
            if n == 1:
                if nums[0] == target:
                    return [0,0]
                else:
                    return [-1,-1]
            else:
                m = (n-1)/2
                if nums[m] == target:
                    l1, l2 = self.searchRange(nums[:m+1], target) #includes m
                    left = l1
                    r1, r2 = self.searchRange(nums[m+1:], target)
                    if r1 == -1:
                        right = l2
                    else:
                        right = r2+m+1
                    return [left, right]
                elif nums[m] < target:
                    r1, r2 = self.searchRange(nums[m+1:], target)
                    if r1 == -1:
                        return [r1, r2]
                    else:
                        return [r1+m+1, r2+m+1]
                else:
                    return self.searchRange(nums[:m], target)        
        else:
            return [-1,-1]
