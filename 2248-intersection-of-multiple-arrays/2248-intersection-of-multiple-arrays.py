class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        counter = dict()
        
        for arr in nums:
            for num in arr:
                counter[num] = 1 + counter.get(num, 0)
                
        maxLen = len(nums)
        return sorted(key for key, val in counter.items() if val == maxLen)
        