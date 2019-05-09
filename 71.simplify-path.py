#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#
class Solution:
    def simplifyPath(self, path: str) -> str:
        li = path.split('/')
        stack = []
        for el in li:
            if el == '..':
                if stack:
                    stack.pop()
            elif el and el != '.':
                stack.append(el)
                
        return '/'+'/'.join(stack) 



