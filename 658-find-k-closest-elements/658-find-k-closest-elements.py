class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        start = 0
        end = len(arr) - k

        while start < end:
            mid = start + (end - start) // 2

            if x - arr[mid] > arr[mid + k] - x:
                start = mid + 1
            else:
                end = mid
        return arr[start: start+k]