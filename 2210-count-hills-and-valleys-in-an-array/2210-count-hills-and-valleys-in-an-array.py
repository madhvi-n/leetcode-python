class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        count = 0
        
        for i in range(1, len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i-1]
                
            prev, curr, nxt = nums[i-1], nums[i], nums[i+1]
            
            if curr > prev and curr > nxt: # it's a hill
                count += 1
                
            if curr < prev and curr < nxt: # it's a valley
                count += 1
        
        return count