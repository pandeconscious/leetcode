class Solution(object):
    def _subsetSum(self, sum_, nums):
        n = len(nums)
        if n == 0:
            return True
        dp = [[False for _ in xrange(sum_+1)] for _ in xrange(n)]
        dp[0][0] = True
        for s in xrange(1, sum_+1):
            dp[0][s] = True if nums[0] == s else False
        for i in xrange(1, n):
            dp[i][0] = True
        for s in xrange(1, sum_+1):
            for i in xrange(1, n):
                dp[i][s] = dp[i-1][s] #don't include ith number in subset
                # if the ith number can be included
                if s - nums[i] >= 0:
                    dp[i][s] = dp[i][s] or dp[i-1][s-nums[i]]
        return dp[n-1][sum_]
    
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums)
        #if sum is odd it is not possible
        if total%2 != 0:
            return False
        #else treat it like a subset sum problem with sum being half of the total
        return self._subsetSum(total/2, nums)
