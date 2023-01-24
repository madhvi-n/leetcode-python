class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        
        n = len(matrix)
        
        for r in range(n):
            for c in range(n):
                
                curr = matrix[r][c]
                
                rows[r].add(curr)
                cols[c].add(curr)
        
        for key, val in rows.items():
            if len(val) != n:
                return False
        
        for key, val in cols.items():
            if len(val) != n:
                return False
        
        return True
            