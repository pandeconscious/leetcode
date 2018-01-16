class Solution(object):
    def twoSum(self, sorted_nums, target, i):
        j = len(sorted_nums)-1
        all_pairs = []
        while i < j:
            if sorted_nums[i] + sorted_nums[j] == target:
                all_pairs.append([sorted_nums[i], sorted_nums[j]])
                i += 1
                j -= 1
            elif sorted_nums[i] + sorted_nums[j] < target:
                i += 1
            else:
                j -= 1
        return all_pairs
    
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        solutions = set()
        sorted_nums = sorted(nums)
        for i, x in enumerate(sorted_nums):
            if (i != 0) and (x  == sorted_nums[i-1]):
                continue
            all_pairs = self.twoSum(sorted_nums, -x, i+1)
            if all_pairs is not []:
                for soln in all_pairs:
                    soln.append(x)
                    soln.sort()
                    solutions.add(tuple(soln))
        return list(solutions)
