#the O(1) space and O(n) time solution using reservoir sampling

import random
class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums
        
    def pick(self, target: int) -> int:
        count = 0
        for ind, el in enumerate(self.nums):
            if el == target:
                count += 1
                if random.random() < 1/count:
                    ret = ind
        return ret
        
# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
