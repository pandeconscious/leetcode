from itertools import accumulate # for cumulative sum
from collections import Counter

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        cum_sum = [list(accumulate(li)) for li in wall]
        cum_sum_flat = [el for li in cum_sum for el in li[:-1]]
        cntr = Counter(cum_sum_flat)
        if cntr:
            return len(wall) - cntr.most_common(1)[0][1]
        else:
            return len(wall)
        
