from collections import Counter
import operator
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        #this solution directly uses the Counter class in collections 
        #see other solution in the same directory for an inhouse solution
        freq = Counter(nums)
        return map(operator.itemgetter(0), freq.most_common(k))
