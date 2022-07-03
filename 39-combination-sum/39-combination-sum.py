class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []                                 
        combination = []
        
        def dfs(i, combination, total):
            # base cases: if total reaches target val, append a copy to result
            # if index is out of bounds, or total is higher than target, return
            if total == target:
                result.append(combination[:])
                return
            
            if i >= len(candidates) or total > target:
                return
            
            # include the current candidate in the combination and call dfs with total + candidates[i]
            combination.append(candidates[i])
            dfs(i, combination, total + candidates[i])
            
            # exclude the current candidate and call dfs over next index
            combination.pop()            
            dfs(i + 1, combination, total)
            
        dfs(0, [], 0)
        return result