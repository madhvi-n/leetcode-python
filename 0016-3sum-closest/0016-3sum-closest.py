class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) < 3: 
            return
        
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        
        for index in range(len(nums) - 2):
            left, right = index + 1, len(nums) - 1
            while left < right:
                currSum = nums[index] + nums[left] + nums[right]
                if currSum == target:
                    return currSum
                if abs(currSum - target) < abs(result - target):
                    result = currSum
                if currSum < target:
                    left += 1
                elif currSum > target:
                    right -= 1
        return result