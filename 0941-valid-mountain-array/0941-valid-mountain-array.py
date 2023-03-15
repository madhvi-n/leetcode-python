class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        
        left = 0
        for i in range(len(arr)-1):
            if arr[i+1] <= arr[i]:
                left = i
                break
        right = 0
        for i in range(len(arr)-1, 0, -1):
            if arr[i-1] <= arr[i]:
                right = i
                break
        if left == right and left > 0 and right+1 < len(arr):
            return True
        return False