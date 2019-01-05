class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        """
        Although this does exactly what is asked in the questions
        but this solutions is more complicated then the one described here:
        https://www.geeksforgeeks.org/move-zeroes-end-array/
        """
        
        n = len(nums)
        if n <= 1:
            return
        
        try:
            left_most_zero = nums.index(0)
        except ValueError:
            return
        
        first_non_zero = left_most_zero + 1
        while first_non_zero < n and nums[first_non_zero] == 0:
            first_non_zero += 1
        
        while first_non_zero < n:
            nums[left_most_zero], nums[first_non_zero] = nums[first_non_zero], nums[left_most_zero]
            left_most_zero = nums[left_most_zero+1:].index(0) + left_most_zero + 1
            first_non_zero += 1
            while first_non_zero < n and nums[first_non_zero] == 0:
                first_non_zero += 1
            
