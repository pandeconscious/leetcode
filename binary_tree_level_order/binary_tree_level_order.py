# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        lot = []
        if root:
            Q = deque()
            Q.append((1, root))
            while(Q):
                level, node = Q.popleft()
                last_level = len(lot)
                if level == last_level:
                    lot[-1].append(node.val)
                else:
                    lot.append([node.val])
                if node.left:
                    Q.append((level+1, node.left))
                if node.right:
                    Q.append((level+1, node.right))
        return lot
