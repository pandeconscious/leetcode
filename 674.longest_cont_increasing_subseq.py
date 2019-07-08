class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n
        max_ = 1
        curr_max = 1
        for j in range(1, n):
            if nums[j] > nums[j-1]:
                curr_max += 1
                max_ = max(max_, curr_max)
            else:
                curr_max = 1
        return max_
        
