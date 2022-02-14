class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0

        nums = []
        index = 0
        
        if len(arr) < 3:
            return False
        
        while index < len(arr):
            if len(nums) == 3:
                break
                
            if arr[index] % 2 == 1:
                nums.append(arr[index])
            else:
                nums = []
            
            index += 1
        
        return len(nums) == 3