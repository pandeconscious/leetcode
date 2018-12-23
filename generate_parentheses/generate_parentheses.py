class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        dp = []
        for _ in xrange(n+1):
            dp.append([])
        
        dp[0].append("")
        dp[1].append("()")
        
        for p in xrange(2, n+1):
            paren_p = set()
            for i in xrange(p):
                for j in xrange(p-i):
                    for k in xrange(p-i-j):
                        if i + j + k == p-1:
                            left = dp[i]
                            mid = ["".join(["(", s, ")"]) for s in dp[j]]
                            right = dp[k]
                            for s1 in left:
                                for s2 in mid:
                                    for s3 in right:
                                        paren_p.add("".join([s1, s2, s3]))
            dp[p].extend(paren_p)
        return dp[n]
        
        
