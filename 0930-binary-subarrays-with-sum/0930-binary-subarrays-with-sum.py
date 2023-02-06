class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        indexes = [-1] + [i for i, v in enumerate(nums) if v] + [len(nums)]
        
        ans = 0
        
        if goal == 0:
            for i in range(len(indexes) - 1):
                w = indexes[i+1] - indexes[i] - 1
                ans += w * (w + 1) / 2
            return int(ans)
        
        for i in range(1, len(indexes) - goal):
            j = i + goal - 1            
            left = indexes[i] - indexes[i-1]
            right = indexes[j+1] - indexes[j]
            ans += left * right
        return int(ans)
                