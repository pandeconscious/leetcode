# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def binsrch(self, l, r):
        if r < l:
            return
        if l == r and isBadVersion(l):
            self.first = min(self.first, l)
            return
        m = (l+r)//2
        if isBadVersion(m):
            self.first = min(self.first, m)
            self.binsrch(l, m-1)
        else:
            self.binsrch(m+1, r)
        
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.first = n+1
        self.binsrch(1, n)
        return self.first
