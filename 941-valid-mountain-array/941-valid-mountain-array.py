class Solution:
    def findPeak(self, arr: List[int]) -> int:
        start = 0
        end = len(arr) - 1
        
        while start < end:
            mid = start + (end - start) // 2
            
            if arr[mid] > arr[mid + 1]:
                end = mid
            else:
                start = mid + 1
        return start
    
    def checkArray(self, arr: List[int], start: int, end: int) -> bool:
        asc = arr[start] < arr[end]
        
        for i in range(start, end):
            #If you are in the asc part of the array and arr[i] is not less than arr[i+1], return false
            if asc:
                if not arr[i] < arr[i+1]:
                    return False
            else:
                # If you are in the desc part of the array and arr[i] is not greater than arr[i+i], return false
                if not arr[i] > arr[i+1]:
                    return False
        return True
            
    
    def validMountainArray(self, arr: List[int]) -> bool:
        #if arr length is less than or equal to 2, return false
        if len(arr) < 3:
            return False
        
        #find peak
        peak = self.findPeak(arr)
        
        #if peak is at the start or at the end, return false ex. [5, 1, 2, 3] or [1, 2, 3, 5]
        if peak == 0 or peak == len(arr) - 1:
            return False
        
        #else check if elements before and after the peak are in asc and desc order respectively
        return self.checkArray(arr, 0, peak) and self.checkArray(arr, peak, len(arr) - 1)
        