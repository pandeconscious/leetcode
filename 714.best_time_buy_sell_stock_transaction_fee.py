class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        #dp[i][0] stores that maximum profit for prices[:i] if ith state is sold state
        #dp[i][1] stores that maximum profit for prices[:i] if ith state is bought state
        
        n = len(prices)
        dp = [[None, None] for _ in range(n)]
        dp[0] = [0, -prices[0]]
        
        for i in range(1, n):
            #if sold state then either continue in previous sold state or sell from previous bought state
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i]-fee)
            #if bought state then either continue in prev bought state of buy after previous sell state
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i])
        
        max_ = float("-inf")
        
        for el in dp:
            max_ = max(max_, *el)
            
        return max_
