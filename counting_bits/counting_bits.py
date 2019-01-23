import math
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num == 0:
            return [0]
        two_power_floor = int(math.ceil(math.log(num, 2)))
        arr = [0,1]
        for pow_ in xrange(1, two_power_floor+1):
            count = int(math.pow(2, pow_))
            for i in arr[:count]:
                arr.append(i+1)
        return arr[:num+1]
