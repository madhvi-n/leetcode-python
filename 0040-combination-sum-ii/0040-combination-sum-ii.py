class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []                                 
        candidates.sort()
        n = len(candidates)
        
        def backtrack(currentArray, currentIndex, target):                   
            if target == 0:
                result.append(currentArray[:])
                return
            
            if currentIndex >= n or target <= 0:
                return
            
            prev = -1
            
            for i in range(currentIndex, n):
                if candidates[i] == prev:
                    continue
                    
                currentArray.append(candidates[i])
                backtrack(currentArray, i + 1, target - candidates[i])
            
                currentArray.pop()            
                prev = candidates[i]
        
        backtrack([], 0, target)
        return result