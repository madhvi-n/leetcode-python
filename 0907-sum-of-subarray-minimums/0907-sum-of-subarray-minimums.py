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

        def get_previous_large_element(nums):
            n = len(nums)
            left, stack = [-1] * n, []
            for i in range(n):
                while stack and nums[i] < nums[stack[-1]]: 
                    stack.pop()
                left[i] = stack[-1] if stack else -1
                stack.append(i)
            for i in range(n):
                left[i] =  i+1 if left[i] == -1 else i - left[i]
            return left
        
        def get_next_large_element(nums):
            n = len(nums)
            right, stack = [-1] * n, []
            for i in range(n):
                while stack and nums[i] < nums[stack[-1]]: 
                    right[stack.pop()] = i
                stack.append(i)
            for i in range(n):
                right[i] =  n - i if right[i] == -1 else right[i] - i
            return right
        
        mod = (10**9) + 7
        left = get_previous_large_element(arr)
        right = get_next_large_element(arr)

        return sum(a*l*r for a, l, r in zip(arr, left, right)) % mod