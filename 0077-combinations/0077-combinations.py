class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.res = []
        
        def backtrack(start, combination):
            if len(combination) == k:
                self.res.append(combination[:])
            
            for i in range(start, n + 1):
                combination.append(i)
                backtrack(i + 1, combination)
                combination.pop()
        
        backtrack(1, [])
        return self.res