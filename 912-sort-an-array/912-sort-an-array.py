class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums, 0, len(nums))
    
    def mergeSort(self, nums: List[int], left: int, right: int) -> List[int]:
        
        if right - left <= 1:
            return nums[left: right]
        
        if right - left > 1:
            mid = (left + right) // 2
            first = self.mergeSort(nums, left, mid)
            second = self.mergeSort(nums, mid, right)
            return merge(first, second)
    
    def merge(self, arr1: List[int], arr2: List[int]) -> List[int]:
        i, j, k = 0, 0, 0
        
        while i < len(arr1) and j < len(arr2):
            if arr[i] < arr2[j]:
                result[k] = arr1[i]
                i += 1
            else:
                result[k] = arr2[j]
                j += 1
            k += 1

        while i < len(arr1):
            result[k] = arr1[i]
            i += 1
            k += 1

        while j < len(arr2):
            result[k] = arr2[j]
            j += 1
            k += 1
    
        return result
            