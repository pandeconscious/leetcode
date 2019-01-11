from collections import defaultdict

class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        dp = []
        for _ in xrange(n):
            dp.append(defaultdict(int))
        
        dp[0][nums[0]] += 1
        dp[0][-nums[0]] += 1
            
        for i in xrange(1, n):
            for prev_sum, count in dp[i-1].iteritems():
                dp[i][prev_sum+nums[i]] += count
                dp[i][prev_sum-nums[i]] += count
            
        return dp[n-1][S]
