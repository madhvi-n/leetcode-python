class Solution:
    def is_even(self, num: int) -> int:
        count = 0
        while num > 0:
            count += 1
            num = num // 10
        return count % 2 == 0
    
    def findNumbers(self, nums: List[int]) -> int:
        evenCount = 0
        for index, num in enumerate(nums):
            if self.is_even(num):
                evenCount += 1
        return evenCount
        