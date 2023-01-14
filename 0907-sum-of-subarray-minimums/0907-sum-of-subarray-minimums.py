class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
#         mod = 10 ** 9 + 7
#         stack = []
#         minSum = 0
#         n = len(arr)
        
#         for i in range(n + 1):
#             while stack and (i == len(arr) or arr[stack[-1]] >= arr[i]):
#                 mid = stack.pop()
#                 left_boundary = -1 if not stack else stack[-1]
#                 right_boundary = i
                
#                 count = (mid - left_boundary) * (right_boundary - mid)
#                 minSum += (count * arr[mid])
#             stack.append(i)
        
#         return minSum % mod

        n = len(arr)
        arr.append(0)
        res = 0
        mod = 1000000007
        stack = [-1]

        for i, num in enumerate(arr):
            while stack and arr[stack[-1]] > num: # (i)
                current = stack.pop()
                res += arr[current] * (i - current) * (current - stack[-1])

            stack.append(i)

        return res % (mod)