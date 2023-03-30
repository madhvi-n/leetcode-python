class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
#         satisfaction.sort()
        
#         n = len(satisfaction)
        
#         if satisfaction[-1] <= 0:
#             return 0
        
#         ans = float('-inf')
        
#         for i in range(n):
#             curr = 0
            
#             for j in range(i, n):
#                 curr += (satisfaction[j] * (j - i + 1))
            
#             ans = max(curr, ans)
            
#             if satisfaction[i] >= 0:
#                 break
        
#         return ans

        res = total = 0
        satisfaction.sort()
        while satisfaction and satisfaction[-1] + total > 0:
            total += satisfaction.pop()
            res += total
        return res