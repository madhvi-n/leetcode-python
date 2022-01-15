class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        indices = []
        for index, num in enumerate(sorted(nums)):
            if num == target:
                indices.append(index)
        
        return indices