class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []                                 
        
        def dfs(i, currentArray, total):                   
            if total == target:
                result.append(currentArray.copy())
                return
            
            if i >= len(candidates) or total > target:
                return
            
            currentArray.append(candidates[i])
            dfs(i, currentArray, total + candidates[i])
            
            currentArray.pop()            
            dfs(i + 1, currentArray, total)
            
        dfs(0, [], 0)
        return result