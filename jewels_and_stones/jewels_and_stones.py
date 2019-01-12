from collections import Counter

class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        j_set = set(J)
        s_counter = Counter(S)
        common = j_set & set(s_counter.keys())
        return sum(s_counter[el] for el in common)
