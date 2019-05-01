class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        """
        fill two arrays- one tells how much max profit from the left subarray
        the second tells how much max profit from the right subarray
        treat each point as the partition between first
        and the second transaction and find the overall maximum
        """
        
        if not prices or len(prices) == 1:
            return 0
        
        left_max_profit, right_max_profit = [0], [0]
        maxProfit, minVal = 0, prices[0]
        for val in prices[1:]:
            minVal = min(val, minVal)
            maxProfit = max(maxProfit, val-minVal)
            left_max_profit.append(maxProfit)
        
        maxProfit, maxVal = 0, prices[-1]
        for val in prices[-2::-1]:
            maxVal = max(val, maxVal)
            maxProfit = max(maxProfit, maxVal-val)
            right_max_profit.append(maxProfit)
        
        right_max_profit = right_max_profit[-1::-1]
        
        maxx = 0
        for i in xrange(len(prices)-1):
            #index i becomes the partition point
            maxx = max(maxx, left_max_profit[i]+right_max_profit[i+1])
            
        #edge case of buying the first day and selling the last day
        maxx = max(maxx, prices[-1]-prices[0])
        return maxx

