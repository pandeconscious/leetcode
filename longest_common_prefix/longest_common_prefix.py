class Solution(object):
    def common_str(self, str1, str2):
        i = 0
        while i < min(len(str1), len(str2)):
            if str1[i] != str2[i]:
                break
            i += 1
        return str1[0:i]
    
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs:
            common = strs[0]
            for i in range(1, len(strs)):
                common = self.common_str(common, strs[i])
                if common == "":
                    break
            return common
        
        else:
            return ""
