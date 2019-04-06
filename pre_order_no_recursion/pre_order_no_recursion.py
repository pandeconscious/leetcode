# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        pre_order = [root]
        stack = [root]
        while stack:
            #root becomes output and keep going to the left by pushing in stack
            while root.left:
                root = root.left
                pre_order.append(root)
                stack.append(root)
            # when can't go further to left pop from stack until right is possible
            root = stack.pop()
            while stack and not root.right:
                root = stack.pop()
            #if actually right is possible then output right and push righ to stack
            #to go back to the beginning of the loop and start the same process
            if root.right:
                root = root.right
                pre_order.append(root)
                stack.append(root)
        return [node.val for node in pre_order]
