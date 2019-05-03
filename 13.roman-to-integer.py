#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#
class Solution:
    def __init__(self):
        self.mapping = {
            'I':1,  'V': 5, 'X': 10, 'L':50,
            'C': 100, 'D': 500, 'M': 1000
        }

        self.mapping_special = {
            'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90,
            'CD': 400, 'CM': 900
        }

    def romanToInt(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        if n == 1:
            return self.mapping[s]
        val, i  = 0, 0
        while i < n-1:
            if s[i:i+2] in self.mapping_special:
                val += self.mapping_special[s[i:i+2]]
                i += 2
                continue
            val += self.mapping[s[i]]
            i += 1
        
        if i == n-1:
            val += self.mapping[s[i]]

        return val
            

