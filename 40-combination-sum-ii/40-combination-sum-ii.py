class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []                                 
        candidates.sort()
        
        def backtrack(currentArray, currentIndex, target):                   
            if target == 0:
                result.append(currentArray.copy())
                return
            
            if currentIndex >= len(candidates) or target <= 0:
                return
            
            prev = -1
            
            for i in range(currentIndex, len(candidates)):
                if candidates[i] == prev:
                    continue
                    
                currentArray.append(candidates[i])
                backtrack(currentArray, i + 1, target - candidates[i])
            
                currentArray.pop()            
                prev = candidates[i]
        
        backtrack([], 0, target)
        return result