class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
#         n = len(arr)
#         answer = 0
        
#         for left in range(n):
#             for right in range(left, n):
#                 if (right - left + 1) % 2 == 1:
#                     current_sum = 0
#                     for index in range(left, right + 1):
#                         current_sum += arr[index]
#                     answer += current_sum

#         return answer
        
        n = len(arr)
        answer = 0
        
        for i, a in enumerate(arr):
            left, right = i, n - i - 1
            answer += a * (left // 2 + 1) * (right // 2 + 1)
            answer += a * ((left + 1) // 2) * ((right + 1) // 2)
        return answer