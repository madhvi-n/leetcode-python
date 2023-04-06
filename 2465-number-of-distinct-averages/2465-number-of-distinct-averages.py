class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        result = set()
        
        nums.sort()
        
#         left, right = 0, len(nums) - 1
        
#         while left < right:
#             avg = (nums[left] + nums[right]) / 2
#             result.add(avg)
            
#             left += 1
#             right -= 1
        
#         return len(result)
    
        for i in range(len(nums)//2):
            result.add((nums[i] + nums[len(nums) - i -1]) / 2)
        return len(result)