class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        # apply the first part of operations
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                nums[i-1], nums[i] = nums[i-1]*2, 0    
        
        # 'not' of any non-zero number is equal to 0, i.e.,
        # less than 'not 0' which is 1 (here, sorting is stable)
        return sorted(nums, key=lambda x: not x)