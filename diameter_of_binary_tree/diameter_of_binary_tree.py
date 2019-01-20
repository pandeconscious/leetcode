# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    #not the most optimum solution:
    #https://www.geeksforgeeks.org/diameter-of-a-binary-tree/
    def preprocess(self, root):
        #preprocess to store in val the tuple storing max depth of 
        # a leaf in the left subtree and right subtree 
        # assuming the root is included in the diameter
        if root:
            self.preprocess(root.left)
            self.preprocess(root.right)
            
            if not root.left and not root.right:
                root.val = (0, 0)
            if not root.left and root.right:
                root.val = (0, 1+max(*root.right.val))
            if root.left and not root.right:
                root.val = (1+max(*root.left.val), 0)
            if root.left and root.right:
                root.val = (1+max(*root.left.val), 1+max(*root.right.val))
    
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #two cases possible
        #(A) root is included in the longest path
        #(B) root is not included in the longest path
        
        #first preprocess
        self.preprocess(root)
    
        if not root:
            return 0
        
        left = self.diameterOfBinaryTree(root.left)
        right = self.diameterOfBinaryTree(root.right)
        
        return max(left, right, sum(root.val))
