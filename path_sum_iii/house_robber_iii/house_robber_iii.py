# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        #two cases - a. root is robbed, b. root is not robbed
        #do memoization by storing the max possible at nodes
        if not root:
            return 0
        
        #this means max already processed and stored in val as second element
        if type(root.val) is list:
            return root.val[1]
        
        root_robbed_max = root.val
        
        if root.left:
            root_robbed_max += self.rob(root.left.left)
            root_robbed_max += self.rob(root.left.right)
        
        if root.right:
            root_robbed_max += self.rob(root.right.left)
            root_robbed_max += self.rob(root.right.right)
            
        root_not_robbed_max = self.rob(root.left)
        root_not_robbed_max += self.rob(root.right)
        
        root.val = [root.val, max(root_robbed_max, root_not_robbed_max)]
        
        return root.val[1]
