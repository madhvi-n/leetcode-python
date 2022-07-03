class Solution:
    
    def backtrack(self, length, curr_target, combination):
        if curr_target < 0 or length < 0: 
            return
        
        if curr_target == 0 and length == 0:
            self.result.append(combination)
            
        start = combination[-1] + 1 if combination else 1
            
        for i in range(start, 10):
            self.backtrack(length - 1, curr_target - i, combination + [i])

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.result = []
        self.backtrack(k, n, [])
        return self.result
        
            
                