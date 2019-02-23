# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# this solution avoids extra space
class Solution(object):
    def LCA(self, root, p, q):
        #base cases
        if not root:
            return False, False
        if not root.left and not root.right:
            if root.val == p.val:
                return True, False
            if root.val == q.val:
                return False, True
            
        #left subtree
        left_p, left_q = self.LCA(root.left, p, q)
        #if both p and q in left subtree no need to recurse on the right side
        if left_p and left_q:
            return True, True
        
        #right subtree
        right_p, right_q = self.LCA(root.right, p, q)
        if right_p and right_q:
            return True, True
        
        #cases for current node being one of p or q
        if root.val == p.val:
            if left_q or right_q:
                self.lca = root
                return True, True
            else:
                return True, False
        if root.val == q.val:
            if left_p or right_p:
                self.lca = root
                return True, True
            else:
                return False, True
        
        if (left_p and right_q) or (left_q and right_p):
            self.lca = root
            return True, True
        if left_p or right_p:
            return True, False
        if left_q or right_q:
            return False, True
        return False, False
    
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.lca = None
        self.LCA(root, p, q)
        return self.lca
