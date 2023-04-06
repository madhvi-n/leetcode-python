class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        maxNum = float('-inf')
        seen = set()
        
        for num in nums:
            if num < 0:
                seen.add(num)
            
            if num > 0 and -num in seen:
                maxNum = max(maxNum, num)
            
        return maxNum if maxNum != float('-inf') else -1