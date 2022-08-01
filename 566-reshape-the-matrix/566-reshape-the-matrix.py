class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        arr = []
        matrix = []

        for sublist in nums:
            for item in sublist:
                arr.append(item)

        if len(arr) != r * c:
            return nums
        else:
            for i in range(0, len(arr), c):
                matrix.append(arr[i:i+c])
            return matrix