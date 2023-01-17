class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        
        count = 0
        lastEnd = 0
        
        for start, end in intervals:
            if lastEnd < end:
                lastEnd = end
                count += 1
        return count
        