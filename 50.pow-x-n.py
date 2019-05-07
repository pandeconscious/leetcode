#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#
class Solution:
    def __init__(self):
        self.dp = {}
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        if n == 1:
            return x
        if n == -1:
            return 1/x
        if n in self.dp:
            return self.dp[n]
        else:
            result = self.myPow(x, n//2)*self.myPow(x, n-n//2)
            self.dp[n] = result
            return result

