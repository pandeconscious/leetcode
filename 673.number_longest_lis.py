class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        #dp[i] to store the (length, num ways) of the longest
        # subsequence ending at i
        dp = [[1,1] for _ in range(n)]
        
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    #the case where current longest is matched
                    if dp[j][0] + 1 == dp[i][0]:
                        dp[i][1] += dp[j][1]
                    #where new longest is found
                    elif dp[j][0] + 1 >= dp[i][0]:
                        dp[i][0] = dp[j][0] + 1 
                        dp[i][1] =  dp[j][1]
        max_ = float("-inf")
        for el in dp:
            if el[0] > max_:
                max_ = el[0]
        return sum(ways for len_, ways in dp if len_ == max_)
