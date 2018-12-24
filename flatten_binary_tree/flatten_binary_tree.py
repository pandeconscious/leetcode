# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten_util(self, root):
        #flattens and returns the last node in the flattened tree
        if root:
            if not root.left and not root.right:
                return root
            if not root.left:
                return self.flatten_util(root.right)
            if not root.right:
                root.right = root.left
                root.left = None
                return self.flatten_util(root.right)
            temp = root.right
            root.right = root.left
            root.left = None
            last = self.flatten_util(root.right)
            last.right = temp
            return self.flatten_util(last.right)
    
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root:
            self.flatten_util(root)
        
        
