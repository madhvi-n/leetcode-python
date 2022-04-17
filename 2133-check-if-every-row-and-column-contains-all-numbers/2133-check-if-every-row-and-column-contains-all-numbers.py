class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        
        
        for r in range(len(matrix)):
            for c in range(len(matrix)):
                #If element exist in any of the three sets, return False
                if matrix[r][c] in rows[r] or matrix[r][c] in cols[c]:
                    return False
                
                #Add element if it doesn't exist
                rows[r].add(matrix[r][c])
                cols[c].add(matrix[r][c])
                
        return True