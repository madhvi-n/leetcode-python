class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
#         l1, l2 = len(word1), len(word2)
#         cache = [[float('inf') for _ in range(l2 + 1)]  for _ in range(l1 + 1)]
        
#         for j in range(l2 + 1):
#             cache[l1][j] = l2 - j
        
#         for i in range(l1 + 1):
#             cache[i][l2] = l1 - i
        
#         for i in range(l1 - 1, -1, -1):
#             for j in range(l2 - 1, -1, -1):
#                 if word1[i] == word2[j]:
#                     cache[i][j] = cache[i + 1][j + 1]
#                 else:
#                     cache[i][j] = 1 + min(cache[i + 1][j], 
#                                     cache[i][j + 1], cache[i + 1][j + 1] )                  
#         return cache[0][0]
        
        memo = {}
        
        def dfs(i, j):
            if i == 0 or j == 0: 
                return j or i
                        
            if (i,j) in memo:
                return memo[(i,j)]
            
            if word1[i-1] == word2[j-1]:
                ans = dfs(i-1, j-1)
            else: 
                ans = 1 + min(dfs(i, j-1), dfs(i-1, j), dfs(i-1, j-1))
                
            memo[(i,j)] = ans
            return memo[(i,j)]
        
        return dfs(len(word1), len(word2))
        