# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> int:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start, end = 1, n
        
        while start < end:
            mid = start + (end - start) // 2
            check = isBadVersion(mid)
            if check:
                end = mid
            else:
                start = mid + 1
        return start