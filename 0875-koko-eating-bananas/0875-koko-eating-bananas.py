class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start, end = 0, max(piles)
        while start + 1 < end:
            mid = (start + end)//2
            if sum(ceil(pile/mid) for pile in piles) > h:
                start = mid
            else:
                end = mid
        return end