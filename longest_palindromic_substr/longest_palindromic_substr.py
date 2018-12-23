class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxs = ""
        if s:
            n = len(s)
            maxl, maxr = 0, 0
            for c in xrange(n):
                #odd length with centre at c
                l, r = c - 1, c + 1
                while l >= 0 and r < n and s[l] == s[r]:
                    if r - l + 1 > maxr - maxl + 1:
                        maxr, maxl = r, l
                    l -= 1
                    r += 1
                
                #even length with left centre at c
                l, r = c, c+1
                while l >= 0 and r < n and s[l] == s[r]:
                    if r - l + 1 > maxr - maxl + 1:
                        maxr, maxl = r, l
                    l -= 1
                    r += 1
            maxs = s[maxl:maxr+1]
        return maxs
            
        
