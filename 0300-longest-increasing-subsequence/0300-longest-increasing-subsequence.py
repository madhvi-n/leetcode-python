class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        arr = [1] * len(nums)
        i = 0
        
        while i < len(nums):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    arr[i] = max(arr[j] + 1, arr[i])
            i += 1
        
        return max(arr)