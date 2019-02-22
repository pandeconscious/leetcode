# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def createTreeDP(self, root):
        # in dp we store the max linear path along left subtree and right subtree
        if root:
            node = TreeNode([root.val, root.val])
            node.left = self.createTreeDP(root.left)
            node.right = self.createTreeDP(root.right)
            return node
      
    def solve_dp(self, node):
        if node:
            self.max_ = max(self.max_, node.val[0])
            if node.left:
                self.solve_dp(node.left)
                node.val[1] = max(node.val[1], node.left.val[1] + node.val[0])
                self.max_ = max(self.max_, node.val[0] + node.left.val[1])
            if node.right:
                self.solve_dp(node.right)
                node.val[1] = max(node.val[1], node.right.val[1] + node.val[0])
                self.max_ = max(self.max_, node.val[0] + node.right.val[1])
            if node.left and node.right:
                self.max_ = max(self.max_, node.val[0] + node.right.val[1] + node.left.val[1])
    
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.max_ = -999999999
        tree_dp = self.createTreeDP(root)
        self.solve_dp(tree_dp.left)
        self.solve_dp(tree_dp.right)
        self.max_ = max(self.max_, tree_dp.val[0])
        left_, right_ = None, None
        if tree_dp.left:
            self.max_ = max(self.max_, tree_dp.val[0] + tree_dp.left.val[1])
        if tree_dp.right:
            self.max_ = max(self.max_, tree_dp.val[0] + tree_dp.right.val[1])
        if tree_dp.left and tree_dp.right:
            self.max_ = max(self.max_, tree_dp.val[0] + tree_dp.left.val[1] + tree_dp.right.val[1])
        return self.max_
    
