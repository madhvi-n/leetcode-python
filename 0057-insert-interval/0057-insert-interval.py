class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #append the new interval to intervals and sort interval by start
        # traverse through each interval, if current interval's end is greater or equal to the next interval's start
        # current interval's end will be max of current interval's end and next interval's end
        # del next interval
        
        intervals.append(newInterval)
        intervals = sorted(intervals, key = lambda x: x[0])
       
        i = 0
        while i < len(intervals) - 1:
            if intervals[i][1] >= intervals[i+1][0]:
                intervals[i][1] = max(intervals[i][1], intervals[i+1][1])
                del intervals[i+1]
            else:
                i += 1
        return intervals
        