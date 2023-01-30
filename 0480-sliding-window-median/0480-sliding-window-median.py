class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        d = deque()
        result = []
        
        for i, n in enumerate(nums):
            if i >= k:
                d.remove(nums[i - k])
                
            insort_left(d, n)
            
            if i >= k - 1:
                if k % 2 == 0:
                    m = (d[k//2 - 1] + d[k//2]) / 2
                else:
                    m = d[k//2]
                result.append(m)
        return result