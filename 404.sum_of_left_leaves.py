# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sum_util(self, node: TreeNode, left: bool):
        if not node:
            return
        if not node.left and not node.right and left:
            self.sum += node.val
        if node.right:
            self.sum_util(node.right, False)
        if node.left:
            self.sum_util(node.left, True)
        
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.sum = 0
        self.sum_util(root.left, True)
        self.sum_util(root.right, False)
        return self.sum
        
        
