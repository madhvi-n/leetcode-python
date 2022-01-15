class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        indices = []
        
        nums.sort()
        
        for index, num in enumerate(nums):
            if num == target:
                indices.append(index)
        
        return indices