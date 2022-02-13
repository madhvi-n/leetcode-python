class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        output = [[]]
        result = []
        
        for num in sorted(nums):
            res = [lst + [num] for lst in output]
            output += res
        
        for subset in output:
            if subset not in result:
                result.append(subset)
        
        return result