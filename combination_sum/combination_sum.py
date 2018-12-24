class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if candidates:
            candidates = sorted(candidates)
            n = len(candidates)
            dp = []
            for i in xrange(n):
                dp.append([])
                for _ in xrange(target+1):
                    dp[i].append([])
            for i in xrange(n):
                dp[i][0].append([])
            m = 1
            while(m*candidates[0] <= target):
                dp[0][m*candidates[0]].append(m*[candidates[0]])
                m += 1
            for i in xrange(1,n):
                for t in xrange(1, target+1):
                    #case 1: ith candidate is used
                    new_t = t - candidates[i]
                    if new_t >= 0:
                        for prev_subset in dp[i][new_t]:
                            new_subset = [el for el in prev_subset]
                            new_subset.append(candidates[i])
                            dp[i][t].append(new_subset)
                    #case 2: ith candidate is not used
                    dp[i][t].extend(dp[i-1][t])
            return dp[n-1][target]
        else:
            return []

if __name__ == "__main__":
    sol = Solution()
    candidates = [2,3,5]
    target = 8
    print sol.combinationSum(candidates, target)

