# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def mergable(self, int1, int2):
        return int2.start <= int1.end
    
    def merge_int(self, int1, int2):
        start = int1.start
        end = max(int1.end, int2.end)
        return Interval(s=start,e=end)
    
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        sorted_intervals = sorted(intervals, key=lambda x : x.start)
        merged_intervals = [sorted_intervals[0]]
        for interval in sorted_intervals[1:]:
                merge1 = merged_intervals.pop()
                if self.mergable(merge1, interval):
                    merged_intervals.append(self.merge_int(merge1, interval))
                else:
                    merged_intervals.append(merge1)
                    merged_intervals.append(interval)
        return merged_intervals
