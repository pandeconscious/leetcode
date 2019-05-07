#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

import bisect
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #logically all the intervals that start before the end of newInterval
        #and end after the start of beginning of newInterval 
        #are to be merged with newInterval

        #this solutions works but doesn't look very elegant
        #think of an elegant implementation later
        intervals_start = [st for st, end in intervals]
        ind = bisect.bisect(intervals_start, newInterval[1])
        to_merge = []
        not_merge = []
        for i, (_, end) in enumerate(intervals[:ind]):
            if end >= newInterval[0]:
                to_merge.append(i)
            else:
                not_merge.append(i)
        
        mergedInterval = newInterval
        for i in to_merge:
            st = min(mergedInterval[0], intervals[i][0])
            end = max(mergedInterval[1], intervals[i][1])
            mergedInterval = [st, end]
        
        if not to_merge:
            pos = bisect.bisect(intervals_start, newInterval[0])
            intervals.insert(pos, newInterval)
            return intervals
        
        if not_merge:
            k = bisect.bisect(not_merge, to_merge[0])
            result = []
            if k == len(not_merge):
                for j in not_merge:
                    result.append(intervals[j])
                result.append(mergedInterval)
            else:
                result = []
                merge_inserted = False
                for j in not_merge:
                    if j < not_merge[k]:
                        result.append(intervals[j])
                    elif merge_inserted:
                        result.append(intervals[j])
                    else:
                        result.append(merge_inserted)
                        merge_inserted = True
        else:
            result = [mergedInterval]
        result.extend(intervals[ind:])
        return result


        


