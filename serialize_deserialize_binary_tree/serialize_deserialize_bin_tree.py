# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        q = deque()
        if not root:
            return ""
        level_order = []
        q.append(root)
        while q:
            node = q.popleft()
            if node:
                level_order.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                level_order.append("null")
        #remove nulls from the end
        while level_order[-1] == "null":
            level_order.pop()
        return ",".join(level_order)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        level_order = data.split(",")
        n = len(level_order)
        q = deque()
        root = TreeNode(int(level_order[0]))
        q.append(root)
        i = 1
        while q and i < n:
            node = q.popleft()
            if level_order[i] != "null":
                left_node = TreeNode(int(level_order[i]))
                node.left = left_node
                q.append(left_node)
            i += 1
            if i >= n:
                break
            if level_order[i] != "null":
                right_node = TreeNode(int(level_order[i]))
                node.right = right_node
                q.append(right_node)
            i += 1
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
