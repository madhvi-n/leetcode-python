class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        
        for index, a in enumerate(nums):
            if index > 0 and a == nums[index - 1]:
                continue
            
            left, right = index + 1, len(nums) - 1
            while left < right:
                three_sum = a + nums[left] + nums[right]
                
                if three_sum > 0:
                    right -= 1
                elif three_sum < 0:
                    left += 1
                else:
                    res.add((a, nums[left], nums[right]))
                    left += 1
                    
                    # #to avoid duplicates and never letting the left pass the right pointer
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return res