from collections import defaultdict
import random
class Solution:
    def __init__(self, nums: List[int]):
        self.num_ind = defaultdict(list)
        for ind, el in enumerate(nums):
            self.num_ind[el].append(ind)
        

    def pick(self, target: int) -> int:
        return random.choice(self.num_ind[target])
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
