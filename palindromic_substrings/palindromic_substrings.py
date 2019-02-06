class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        n = len(s)
        is_palindrome = [[0 for _  in s] for _ in s]
        
        for i in xrange(n):
            is_palindrome[i][i] = 1
        
        for i in xrange(n-1):
            if s[i] == s[i+1]:
                is_palindrome[i][i+1] = 1
        
        for l in xrange(3, n+1):
            for i in xrange(n-l+1):
                j = i + l - 1
                if s[i] == s[j]:
                    is_palindrome[i][j] = is_palindrome[i+1][j-1]
        
        return sum([sum(li) for li in is_palindrome])
