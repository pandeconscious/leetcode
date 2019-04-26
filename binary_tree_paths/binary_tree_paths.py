# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import copy

class Solution:
    def __init__(self):
        self.ret = []
        
    def util(self, els: list, node: TreeNode):
        newels = copy.copy(els)
        newels.append(str(node.val))
        if not node.left and not node.right:
            self.ret.append(newels)
        if node.left:
            self.util(newels, node.left)
        if node.right:
            self.util(newels, node.right)
    
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        self.util(els=[],node=root)
        
        #do joining
        return ["->".join(els) for els in self.ret]

