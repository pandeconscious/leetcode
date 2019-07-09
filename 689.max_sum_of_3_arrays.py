from itertools import accumulate

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        #dp_1[i] to store maximum sum, index of 1-array for nums[i:]
        dp_1 = [None for _ in range(n)]
        #dp_2[i] to store maximum sum, indices of 2-array for nums[i:]
        dp_2 = [None for _ in range(n)]
        #dp_3[i] to store maximum sum, indices of 3-array for nums[i:]
        dp_3 = [None for _ in range(n)]
        
        cum_sum = list(accumulate(nums))
        
        #first solve for 1-array sum
        for i in range(n-k, -1, -1):
            if i == n-k:
                dp_1[i] = [cum_sum[n-1] - cum_sum[i-1], i]
            else:
                curr_sum = cum_sum[i+k-1] - cum_sum[i-1] if i > 0 else cum_sum[i+k-1]
                dp_1[i] = dp_1[i+1] if dp_1[i+1][0] > curr_sum else [curr_sum, i]
                
        #now solve for 2-array sum - using both 1-array sum and memoized 2-array sum for subsequent
        for i in range(n-2*k, -1, -1):
            if i == n-2*k:
                dp_2[i] = [cum_sum[n-1] - cum_sum[i-1], [i, i+k]]
            else:
                #either the curr sum along with next 1-array is maximum
                #or the subsequent 2-array itself is the maximum one
                curr_sum = cum_sum[i+k-1] - cum_sum[i-1] if i > 0 else cum_sum[i+k-1]
                curr_sum += dp_1[i+k][0]
                dp_2[i] = dp_2[i+1] if dp_2[i+1][0] > curr_sum else [curr_sum, [i, dp_1[i+k][1]]]
        
        #now solve for 3-array sum in similar fashion
        for i in range(n-3*k, -1, -1):
            if i == n-3*k:
                dp_3[i] = [cum_sum[n-1] - cum_sum[i-1], [i, i+k, i+2*k]]
            else:
                #either the curr sum along with next 2-array is maximum
                #or the subsequent 3-array itself is the maximum one
                curr_sum = cum_sum[i+k-1] - cum_sum[i-1] if i > 0 else cum_sum[i+k-1]
                curr_sum += dp_2[i+k][0]
                dp_3[i] = dp_3[i+1] if dp_3[i+1][0] > curr_sum else [curr_sum, [i]+dp_2[i+k][1]]

        return dp_3[0][1]    
        
