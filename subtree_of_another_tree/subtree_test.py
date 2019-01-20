# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def _isEqualTree(self, s, t):
        if not s and not t:
            return True
        if s and not t:
            return False
        if not s and t:
            return False
        
        if s.val != t.val:
            return False
        
        return self._isEqualTree(s.left, t.left) and self._isEqualTree(s.right, t.right)
    
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s and not t:
            return True
        if s and not t:
            return False
        if not s and t:
            return False
        
        #case 1 possibility of match
        if s.val == t.val:
            is_equal = self._isEqualTree(s, t)
            if is_equal:
                return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
