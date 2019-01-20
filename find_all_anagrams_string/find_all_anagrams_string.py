from collections import Counter

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        
        n = len(s)
        m = len(p)
        if m > n:
            return []
       
        expected_counter = Counter(p) #expected unique chars count
        sum_ = sum(map(ord, p)) #expected sum

        running_counter = Counter(s[:m])
        running_sum = sum(map(ord, s[:m]))
        i = 0
        
        ans = []
        while i+m-1 < n:
            if i != 0:
                running_sum -= ord(s[i-1])
                running_sum += ord(s[i+m-1])
                running_counter[s[i-1]] -= 1
                running_counter[s[i+m-1]] += 1
                
                if running_counter[s[i-1]] == 0:
                    del running_counter[s[i-1]]
                
            
            if running_sum == sum_ and running_counter == expected_counter:
                ans.append(i)
            i += 1
            
        return ans
