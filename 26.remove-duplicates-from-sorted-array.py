#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Example of how each iteration will run
        0|0|1,1,2,3,3,3
        0,1|0,1|2,3,3,3
        0,1,2|1,0|3,3,3
        0,1,2,3|0,1|3,3
        """
        n = len(nums)
        if n == 0 or n ==1:
            return n
        #i to point to the end element of unique sorted elements
        #j to point to the beginning of the yet to be examined region
        #note that there will be a grabage region in between which 
        # will finally end up in the end of the array
        i, j = 0, 1
        while j < n and nums[j] == nums[j-1]:
            j += 1
        #now either j == n or j points to new distinct element
        while j < n:
            nums[i+1], nums[j] = nums[j], nums[i+1]
            i += 1
            j += 1
            while j < n and nums[j] == nums[i]:
                j += 1
        return i+1
    