class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        counter = dict(Counter(nums))
        
        res = 0
        for key, val in counter.items():
            if val == 1:
                res += key
        return res 