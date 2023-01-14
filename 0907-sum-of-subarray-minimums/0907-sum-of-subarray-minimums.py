class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod = 10 ** 9 + 7
        stack = []
        minSum = 0
        n = len(arr)
        
        for i in range(n + 1):
            while stack and (i == len(arr) or arr[stack[-1]] >= arr[i]):
                mid = stack.pop()
                left_boundary = -1 if not stack else stack[-1]
                right_boundary = i
                
                count = (mid - left_boundary) * (right_boundary - mid)
                minSum += (count * arr[mid])
            stack.append(i)
        
        return minSum % mod
