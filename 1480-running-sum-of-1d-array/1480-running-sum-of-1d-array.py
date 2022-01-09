class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums) + 1):
            if nums[:i]:
                result.append(sum(nums[:i]))
        return result