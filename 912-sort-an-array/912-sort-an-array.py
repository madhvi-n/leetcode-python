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
        result = []
        m, n = len(arr1), len(arr2)
        i, j = 0, 0
        
        while i + j < m + n:
            if i == m:
                result.append(arr1[j])
                j += 1
            elif j == m:
                result.append(arr1[i])
                i += 1
            elif arr1[i] <= arr2[j]:
                result.append(arr1[i])
                i += 1
            else:
                result.append(arr2[j])
                j += 1
        return result
            