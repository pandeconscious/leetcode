class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        out = []
        if nums:
            n = len(nums)
            if n == 1:
                out.append(1)
            else:
                prod = 1
                for el in nums:
                    prod *= el
                    out.append(prod)
                prod = 1
                for i, el in enumerate(reversed(nums)):
                    if i == 0:
                        out[n-1] = out[n-2]
                    elif i == n-1:
                        out[0] = prod
                    else:
                        out[n-1-i] = out[n-2-i]*prod
                    prod *= el
        return out
