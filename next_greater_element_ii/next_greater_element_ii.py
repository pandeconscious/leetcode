class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if nums:
            to_return = [-1]*len(nums)
            aug_nums = [(i, el) for i, el in enumerate(nums)]
            aug_nums += aug_nums
            aug_nums.pop()

            stack = []
            for _, (i, el) in enumerate(aug_nums):
                if (not stack) or el <= stack[-1][1]:
                    stack.append((i ,el))
                while stack and (el > stack[-1][1]):
                    if to_return[stack[-1][0]] == -1:
                        to_return[stack[-1][0]] = el
                    stack.pop()
                stack.append((i ,el))
            return to_return 
        else:
            return []
        
