#
# @lc app=leetcode id=44 lang=python3
#
# [44] Wildcard Matching
#
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        #corner cases where either of the strings is empty
        if m == 0 and n == 0:
            return True
        if m == 0 and n != 0:
            distinct = set(p)
            if len(distinct) == 1 and "*" in distinct:
                return True
            else:
                return False
        if m != 0 and n == 0:
            return False

        #run DP on the non-empty cases
        #dp[i][j] tells if s[i:] and p[j:] match
        dp = []
        for _ in range(m):
            dp.append([False for _ in range(n)])
        #base cases
        if p[n-1] == "*" or p[n-1] == "?" or p[n-1] == s[m-1]:
            dp[m-1][n-1] = True

        for r in range(m-1):
            if p[n-1] == "*":
                dp[r][n-1] = True 
        
        for c in range(n-1):
            count_star = p[c:].count("*")
            count_question = p[c:].count("?")
            count_char = p[c:].count(s[m-1])
            if count_star == n-c:
                dp[m-1][c] = True
            elif count_question == 1 and count_star == n-c-1:
                dp[m-1][c] = True
            elif count_char == 1 and count_star == n-c-1:
                dp[m-1][c] = True

            
        #the recursive case using dp
        for r in range(m-2, -1, -1):
            for c in range(n-2, -1, -1):
                if p[c] == "*":
                    dp[r][c] = dp[r+1][c] or dp[r][c+1]
                elif p[c] == "?" or p[c] == s[r]:
                    dp[r][c] = dp[r+1][c+1]

        return dp[0][0]

