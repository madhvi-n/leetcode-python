class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
#         red, white, blue = 0, 0, len(nums)-1
    
#         while white <= blue:
#             if nums[white] == 0:
#                 nums[red], nums[white] = nums[white], nums[red]
#                 white += 1
#                 red += 1
#             elif nums[white] == 1:
#                 white += 1
#             else:
#                 nums[white], nums[blue] = nums[blue], nums[white]
#                 blue -= 1
        low, high = 0, len(nums) - 1
        index = 0
        
        while index <= high:
            if nums[index] == 0:
                nums[index], nums[low] = nums[low], nums[index]
                index += 1
                low += 1
            elif nums[index] == 1:
                index += 1
            else:
                nums[index], nums[high] = nums[high], nums[index]
                high -= 1
        