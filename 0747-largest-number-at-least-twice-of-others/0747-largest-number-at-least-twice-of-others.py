class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max1 = max2 = maxi = -1 
        for i, num in enumerate(nums):
            if num > max1:
                max2 ,max1, maxi  = max1 , num , i 
            elif num > max2:
                max2 = num
        return maxi if max1 >= 2 * max2 else -1