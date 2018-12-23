class Solution(object):       
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxlen = 0
        if s:
            #find all unique chars
            allChars = set(s)
            #store the last seen indices of each of the chars
            last_ind_dict = {ch: -1 for ch in allChars}
            last_ind_dict[s[0]] = 0
            l, maxlen = 0, 1
            for r in xrange(1, len(s)):
                if last_ind_dict[s[r]] == -1:
                    maxlen = max(maxlen, r-l+1)
                else:
                    last_ind = last_ind_dict[s[r]]
                    #reset all the characters that would be removed from the max length
                    for ind in xrange(l, last_ind+1):
                        last_ind_dict[s[ind]] = -1
                    l = last_ind + 1
                last_ind_dict[s[r]] = r
        return maxlen
        
