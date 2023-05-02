class Solution:
    def arraySign(self, nums: List[int]) -> int:
        countNegativeNumbers = 0
        for num in nums:
            if num == 0:
                return 0
            if num < 0:
                countNegativeNumbers = countNegativeNumbers + 1

        if countNegativeNumbers %2 == 0:
            return 1
        return -1