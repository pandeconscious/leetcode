# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        to_return = []
        if root:
            stack = [root]
            while stack:
                while root.left:
                    stack.append(root.left)
                    root = root.left
                while stack:
                    root = stack.pop()
                    to_return.append(root.val)
                    if root.right:
                        stack.append(root.right)
                        root = root.right
                        break                   
        return to_return    
