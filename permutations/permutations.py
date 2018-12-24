class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums:
            n = len(nums)
            if n == 1:
                return [[nums[0]]]
            return_val = []
            for i in xrange(n):
                nums_copy = [el for el in nums]
                nums_copy[n-1], nums_copy[i] = nums_copy[i], nums_copy[n-1]
                perm_recur = self.permute(nums_copy[:n-1])
                for el in perm_recur:
                    el.append(nums_copy[n-1])
                return_val.extend(perm_recur)
            return return_val
        else:
            return [[]]
