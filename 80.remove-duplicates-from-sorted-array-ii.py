#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        i, j, count = 0, 1, 1
        while j < n:
            #if mismatch occurs, it's time to move elements from j to i+1
            #and update count to 1
            if nums[i] != nums[j]:
                nums[i+1] = nums[j]
                i+=1
                count = 1
            else:
                if count == 1:
                    nums[i+1] = nums[j]
                    i+=1
                    count += 1
            j+=1
        return i+1
            
        

