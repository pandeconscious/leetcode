from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def calcPaths(self, root):
        if not root:
            return 
        #the second value is a dictionary storing key as a path sum 
        #and value as numer of ways to get that sum if we start at the root
        root.val = (root.val, defaultdict(int))
        root.val[1][root.val[0]] += 1
        if root.val[0] == self.sum:
            self.numpath += 1
        self.calcPaths(root.left)
        self.calcPaths(root.right)
        
        for node in (root.left, root.right):
            if node:
                for left_sum, ways in node.val[1].iteritems():
                    root.val[1][left_sum+root.val[0]] += ways
                    if left_sum+root.val[0] == self.sum:
                        self.numpath += ways
        
    
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        
        if not root:
            return 0
        self.numpath = 0
        self.sum = sum
        self.calcPaths(root)
        
        return self.numpath
