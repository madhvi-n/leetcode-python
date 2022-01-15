# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    
    def peakInArray(self, target: int, arr: 'MountainArray') -> int:
        start, end = 0, arr.length() - 1;

        while start < end:
            mid = start + (end - start) // 2;
            if arr.get(mid) > arr.get(mid+1):
                # Currently in desc part of mountain array, search in the left
                end = mid
            else:
                start = mid + 1
        return start

    def binarySearch(self, target: int, arr: 'MountainArray', start: int, end: int) -> int:
        isAscending = arr.get(start) < arr.get(end)

        while start <= end:
            mid = start + (end - start) // 2

            if arr.get(mid) == target:
                return mid

            if isAscending:
                if target < arr.get(mid):
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if target > arr.get(mid):
                    end = mid - 1
                else:
                    start = mid + 1
            
        return -1;
    
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        peak = self.peakInArray(target, mountain_arr)
        maxNum = mountain_arr.get(peak)
        
        #If num at peak is the target, return target         
        if(target == maxNum):
            return peak
    
        # Search in the left side of the peak         
        index = self.binarySearch(target, mountain_arr, 0, peak - 1)
    
        # Search in the right side of the peak         
        if index == -1:
            index = self.binarySearch(target, mountain_arr, peak + 1, mountain_arr.length() - 1)
        return index
        