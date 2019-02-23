class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n == 0:
            return []
        n_exists = False
        for el in nums:
            if abs(el) == n:
                n_exists = True
            elif nums[abs(el)] > 0:
                nums[abs(el)] *= -1
                
        ret = [i for i, el in enumerate(nums) if el > 0 and i > 0]
        
        if not n_exists:
            ret.append(n)
        return ret
