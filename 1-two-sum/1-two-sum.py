class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        required = dict()
        for i in range(len(nums)):
            if target - nums[i] in required:
                return [required[target - nums[i]], i]
            required[nums[i]] = i