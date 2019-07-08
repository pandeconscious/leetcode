class Solution:
    def maximumSwap(self, num: int) -> int:
        """
        need to think in correct way - otherwise corner cases
        """
        num_str = [int(el) for el in str(num)]
        num_str_rev = sorted(num_str, reverse=True)
        # as far as reverse sorting matched with the original order
        # it is fine - the first index of mismatch needs to be swapped 
        for i, (a, b) in enumerate(zip(num_str, num_str_rev)):
            if a != b:
                break
        else:
            return num
       
        # swap the first mismatch (at index i) with the 
        # the last occurrence(at index k) of the max element after index i  
        max_ = num_str[i]
        k, j = i, i
        while j < len(num_str):
            if num_str[j] >= max_:
                k = j
                max_ = num_str[j]
            j += 1
        
        num_str[i], num_str[k] = num_str[k], num_str[i]
        return int("".join(str(el) for el in num_str))
