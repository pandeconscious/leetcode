class Solution(object):
    def __init__(self):
        self.char2num = {"A":0, "C":1, "G":2, "T": 3}
        self.is_repeated = (2**20)*[False]
        self.base = 4
    
    def get_string_to_num(self, s):
        val = 0
        exponent = 1
        for ch in reversed(s):
            val += self.char2num[ch]*exponent
            exponent *= self.base
        return val
        
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        solutions = set()
        if len(s) > 10:
            curr_val = self.get_string_to_num(s[0:10])
            self.is_repeated[curr_val] = True
            i = 1
            while(i + 10 <= len(s)):
                curr_val = 4*curr_val - (4**10)*self.char2num[s[i-1]] + self.char2num[s[i+9]]
                if self.is_repeated[curr_val] is True:
                    solutions.add(s[i:i+10])
                else:
                    self.is_repeated[curr_val] = True
                i += 1
                
        return list(solutions)
