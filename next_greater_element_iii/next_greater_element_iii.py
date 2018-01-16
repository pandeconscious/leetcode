MAX_INT = 2**31 - 1

class Solution(object):
    def next_greater(self, li):
        n = len(li)
        for i in range(n-1, 0, -1):
            if li[i] > li[i-1]:
                break
        if (i == 1) and (li[i] <= li[i-1]):
            return []
        else:
            j = i
            while j < n:
                if li[j] <= li[i-1]:
                    break
                j += 1
            if j == n-1 and li[j] > li[i-1]:
                li[i-1], li[j] = li[j], li[i-1]
            else:
                li[i-1], li[j-1] = li[j-1], li[i-1]
            li = li[0:i] + sorted(li[i:])
            return li
            
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 10:
            return -1
        
        elif n > 0:
            li = []
            while n > 0:
                li.append(n%10)
                n = n//10
            result_li = self.next_greater(li[::-1])
            if result_li:
                result, mult = 0, 1
                for el in result_li[::-1]:
                    result += mult*el
                    mult *= 10
                return result if result  < MAX_INT else -1
            else:
                return -1
