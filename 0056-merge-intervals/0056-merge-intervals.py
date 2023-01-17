class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort intervals by start
        # traverse interval  from 0 to len(intervals) - 1
        # if current interval's end is greater than next's start
        # replace current interval's end with max of current's end or next interval's end
        # delete next interval and increment i
        
        intervals = sorted(intervals, key = lambda x: x[0])
        i = 0
        while i < len(intervals) - 1:
            if intervals[i][1] >= intervals[i+1][0]:
                intervals[i][1] = max(intervals[i][1], intervals[i+1][1])
                del intervals[i+1]
            else:
                i += 1
        return intervals