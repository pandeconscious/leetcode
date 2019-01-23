from collections import Counter
import operator
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = Counter(nums)
        #since it is guaranteed that elements will be repeated, for an array of length n
        #there are only sqrt(n) unique elements and thus sorting is sqrt(n)log(sqrt(n))
        return map(operator.itemgetter(0), sorted(freq.iteritems(), key=operator.itemgetter(1), reverse=True))[:k]
