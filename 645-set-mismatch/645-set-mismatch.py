class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        i = 0
        res = []
        while i < len(nums):
            correctIndex = nums[i] - 1
            if nums[i] != nums[correctIndex]:
                nums[i], nums[correctIndex] = nums[correctIndex], nums[i]
            else:
                i += 1
                
        for i, num in enumerate(nums):
            if not i == num - 1:
                res.append(num)
                res.append(i+1)
        return res