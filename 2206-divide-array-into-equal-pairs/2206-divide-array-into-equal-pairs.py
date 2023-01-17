class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        if len(nums) % 2  == 1:
            return False
        
        counter = Counter(nums)
        
        
        for key, val in counter.items():
            if val % 2 != 0:
                return False
        
        return True