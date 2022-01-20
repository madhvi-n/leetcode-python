class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i = 0
        res = []
        
        while i < len(nums):
            # index = value - 1 for range(1, N)
            correctIndex = nums[i] - 1
            if nums[i] != nums[correctIndex]:
                nums[i], nums[correctIndex] = nums[correctIndex], nums[i]
            else:
                i += 1

        for index in range(len(nums)):
            # value = index + 1 for range(1, N)
            if nums[index] != index + 1:
                res.append(index + 1)
        
        return res
            