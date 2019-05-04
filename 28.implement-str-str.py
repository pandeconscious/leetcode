#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        even though this is tagged as easy,
        let's implement KMP for this
        """
        n, m = len(haystack), len(needle)

        if m == 0:
            return 0
        if n == 0:
            return -1
        if m > n:
            return -1
        
        #the code for preprocessing of the needle
        #suf[i] to contain the length of longest suffix of needle[:i+1] that's 
        # also a proper prefix of needle[:i+1] 
        suf = [0 for _ in needle]
        i = 1 #the index for which suf[i] to be filled
        j = 0 #the index in needle at which the matching with needle[i] to happen
        while i < m:
            if needle[i] == needle[j]:
                suf[i] = 1 + j
                i += 1
                j += 1     
            elif j > 0:
                #this is the key logic
                j = suf[j-1]
            else:
                i += 1 #as 0 already exists in suf by default
        
        #the pattern matching usinf the preprocessing doene above
        i, j = 0, 0
        while i <= n - m:
            while j < m:
                if haystack[i+j] == needle[j]:
                    j += 1
                elif j > 0:
                    i += j - suf[j-1]
                    j = suf[j-1]
                    break
                else:
                    i += 1
                    break
            if j == m:
                return i

        return -1

