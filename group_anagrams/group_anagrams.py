from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagram_dic = defaultdict(list)
        
        for s in strs:
            s_count = [0]*26
            for ch in s:
                s_count[ord(ch) - ord('a')] += 1
            anagram_dic[tuple(s_count)].append(s)
        return anagram_dic.values()
        
