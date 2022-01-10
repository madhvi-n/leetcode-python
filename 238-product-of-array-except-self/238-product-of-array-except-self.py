class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = nums[:]
        output[0] = 1
        p = 1
        s = 1
        
        for i in range(len(nums)-1):
            p *= nums[i]
            output[i+1] = p
        
        for j in range(len(nums)-1, 0, -1):
            s *= nums[j]
            output[j-1] *= s
        return output