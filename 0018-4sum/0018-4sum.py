from collections import Counter

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        res = []
        
        if length <= 3:
            return []
        
        for i in range(length):
            for j in range(i, length):
                left, right = j + 1, length - 1
                total = 0
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if nums[left] + nums[right] == target - (nums[i] + nums[j]) and i < j < left < right:
                        ans = [nums[i], nums[j], nums[left], nums[right]]
                        if ans not in res:
                            res.append(ans)
                    
                    if total < target:
                        left += 1
                    else:
                        right -= 1
        return res