# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def bst_check(self, root, minn, maxx):
        if root:
            if (root.val > minn) and (root.val < maxx):
                return self.bst_check(root.right, root.val, maxx) and self.bst_check(root.left, minn, root.val)
            else:
                return False
        else:
            return True
    
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.bst_check(root, float("-inf"), float("inf"))
