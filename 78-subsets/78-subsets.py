class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = [[]]
        
        for num in nums:
            res = [lst + [num] for lst in output]
            output += res
        
        return output